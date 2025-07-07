<div align="center">
    <h1>SIGNATURE VERIFICATION SYSTEM!</h1>
</div>

The **Signature Verification System** is an advanced solution designed to detect and verify genuine and forged signatures. Leveraging Deep Learning techniques integrated with the **MERN Stack**, this system is a scalable and efficient tool for secure signature authentication in digital workflows.
________________________________________
**🌟 Project Highlights:**
1.	**Deep Learning Integration:** Utilizes a Convolutional Neural Network (CNN) for accurate and robust signature verification.
  
3.	**React.js Frontend:** Provides a modern, responsive, and user-friendly interface for users to upload signatures and view results.
4.	**Express.js API:** Backend API handles user requests, processes data, and interfaces with the CNN model for prediction.
5.	**MongoDB Database:** Stores user data, logs, and signature metadata for improved management and traceability.
6.	**Scalability:** Designed to handle high volumes of signature data with consistent performance.
________________________________________ 
## 📁 Folder Structure
SignatureVerification/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── uploads/ # Uploaded signature images
│ └── cnn_model/
│ └── signature_verification_cnn_model.h5
│
├── frontend/
│ ├── package.json
│ └── src/
│ └── components/
│ └── Upload.js
│
├── .gitignore
├── README.md
________________________________________ 
## 🔧 Tech Stack

| Layer     | Technology               |
|-----------|---------------------------|
| Frontend  | React (JavaScript, CSS)   |
| Backend   | Flask (Python), Flask-CORS|
| ML Model  | CNN using TensorFlow/Keras|
| Image Ops | OpenCV, Pillow, NumPy     |
| Network   | Axios                     |

---

## 🚀 Getting Started
________________________________________

flask
flask-cors
tensorflow
opencv-python
numpy
pillow
________________________________________ 
### 🐍 Backend Setup

cd backend
python -m venv env           # optional
env\Scripts\activate         # on Windows
python app.py
________________________________________
### Frontend Setup

cd frontend
npm install
npm start
________________________________________



