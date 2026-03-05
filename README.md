# **SMS Spam Classifier**

A **machine learning web app** built with **Python and Streamlit** to classify SMS messages as **Spam** or **Not Spam (Ham)**.  
Users can input any SMS message, and the model predicts whether it is spam along with a confidence score.

---

## **🔗 Live App**
[Open Live App](https://sms-spam-classifier-q22umx4nys3aq7zicrwkn2.streamlit.app)

---

## **Features**
- Classifies SMS messages into **Spam** or **Not Spam**.  
- Shows the **spam probability** for more insight.  
- Handles both **short and long messages**.  
- Easy-to-use **web interface** with Streamlit.  

---

## **Project Structure**


SMS-Spam-Classifier/
│
├─ app.py # Streamlit app
├─ model.pkl # Trained ML model
├─ vectorizer.pkl # TF-IDF vectorizer
├─ requirements.txt # Project dependencies
├─ sms_spam_detection.ipynb # Model training notebook
├─ dataset/ # Raw SMS dataset
└─ .gitignore


---

## **Model Training**
- Dataset: Public SMS Spam Collection  
- Preprocessing:
  - Lowercasing text  
  - Removing punctuation and special characters  
  - Tokenization & vectorization using **TF-IDF**  
- Model: **Multinomial Naive Bayes**  
- Training results:
  - Accuracy: ~97%  
  - Precision (Spam): ~99%  
  - Recall (Spam): ~82%

---
  **Why Naive Bayes works:**  
Even though the independence assumption is not strictly true for text, Naive Bayes still performs well because it captures word frequencies effectively.

---

## **⚙️Deployment on Streamlit Cloud**
**Steps:**
1. Push the project to GitHub (excluding `venv/`)  
2. Make sure `.pkl` files and `requirements.txt` are included  
3. Create a new app on [Streamlit Community Cloud](https://share.streamlit.io/)  
4. Select the repo, branch `main`, and main file `app.py`  
5. Click **Deploy**  

**Problems faced & solutions:**
| Problem | Solution |
|---------|---------|
| LF/CRLF warnings for Windows | Added `venv/` to `.gitignore` and removed it from Git tracking (`git rm -r --cached venv`) |
| App crashing due to missing modules | Made sure all dependencies are in `requirements.txt` |
| Model `.pkl` not loading | Ensured correct filenames (`model.pkl`, `vectorizer.pkl`) and same folder as `app.py` |
| Large dataset / environment files being pushed | Ignored unnecessary files via `.gitignore` |

---

## **Example Messages**
| Message | Prediction | Probability |
|---------|-----------|------------|
| "Congratulations! 🎉 You have been specially selected for a $5000 Amazon gift card! Click http://bit.ly/claim-amazon5000" | Spam | 94.9% |
| "Hey Priya, just checking in. I finished the draft of our project report and uploaded it to Google Drive..." | Not Spam | 5% |

---

## **Demo: Model Predictions**
1.<img width="1898" height="1008" alt="Screenshot 2026-03-05 163229" src="https://github.com/user-attachments/assets/9d50d594-0dc2-4127-97f1-05e4f6ddbce1" />
2.<img width="1898" height="1008" alt="Screenshot 2026-03-05 163229" src="https://github.com/user-attachments/assets/233e521e-e0b2-43ff-9a43-dec626aacdd0" />

---

## **How to Run Locally**

- Clone the repo:
 bash :git clone https://github.com/Bhagya07shree/SMS-Spam-Classifier.git
 --- 
