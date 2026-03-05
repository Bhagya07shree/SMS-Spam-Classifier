import streamlit as st
import pickle
import nltk
import string
import re
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download ALL required NLTK data
@st.cache_data
def download_nltk_data():
    nltk.download('punkt_tab', quiet=True)  # Fixes the main error
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    return True

# Initialize NLTK data
download_nltk_data()

# Initialize stemmer and stopwords
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Enhanced text preprocessing function (matches your notebook exactly)
def transform_text(text):
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove emojis, URLs, special characters 
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\W', ' ', text)
    
    # Tokenize
    text = nltk.word_tokenize(text)
    
    # Remove non-alphanumeric
    y = [i for i in text if i.isalnum()]
    
    # Remove stopwords and punctuation
    y = [i for i in y if i not in stop_words]
    
    # Stemming
    y = [ps.stem(i) for i in y]
    
    return " ".join(y)

# Load models with version warning suppression
@st.cache_resource
def load_models():
    try:
        tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
        model = pickle.load(open('model.pkl', 'rb'))
        return tfidf, model
    except Exception as e:
        st.error(f"Error loading models: {e}")
        st.stop()

tfidf, model = load_models()

# Streamlit UI
st.title("📩 SMS Spam Classifier")
st.markdown("---")

# Input with example
input_sms = st.text_area(
    "Enter the message to classify:",
    placeholder="e.g., 'Free entry in 2 a wkly comp to win FA Cup final...'",
    height=100
)

# Prediction button
if st.button(' Predict', type="primary"):
    if input_sms:
        with st.spinner("Processing..."):
            # Preprocess
            transformed_sms = transform_text(input_sms)
            
            # Vectorize
            vector_input = tfidf.transform([transformed_sms])
            
            # Predict with confidence
            result = model.predict(vector_input)[0]
            probability = model.predict_proba(vector_input)[0]
            spam_prob = probability[1] * 100
            ham_prob = probability[0] * 100
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                if result == 1:
                    st.error("🚨 **SPAM**")
                else:
                    st.success("✅ **Not Spam**")
            
            with col2:
                st.metric("Spam Confidence", f"{spam_prob:.1f}%")
                st.metric("Ham Confidence", f"{ham_prob:.1f}%")
            
            # Show processed text
            with st.expander("View processed text"):
                st.write(f"**Original:** {input_sms}")
                st.write(f"**Processed:** `{transformed_sms}`")
                
    else:
        st.warning("⚠️ Please enter a message to classify!")

# Instructions sidebar
with st.sidebar:
    st.header(" Instructions")
    st.markdown("""
    **How it works:**
    1. Enter SMS text
    2. Click Predict
    3. Get instant classification with confidence scores
    
    **Built with:**
    - Multinomial Naive Bayes
    - TF-IDF Vectorization
    - NLTK Preprocessing
    """)
    
    st.header("📈 Model Performance")
    st.info("✅ 97.7% Accuracy\n✅ 99% Precision")

