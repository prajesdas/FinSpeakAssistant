# **AI Voice Assistant for Financial Banking Operations**

An intelligent voice-enabled financial assistant that allows users to perform secure banking operations such as checking balances, transferring funds, viewing transactions, verifying KYC, and more — all through natural voice commands. The system integrates AI, NLP, Speech Recognition, and secure authentication to deliver a hands-free, secure, and accessible digital banking experience.



## 🚀 **Overview**

The AI Voice Assistant for Financial Banking Operations bridges the gap between humans and digital banking interfaces.
Users can naturally interact with the system using voice, eliminating the need for navigating complex menus or typing commands.

This assistant supports real banking-like workflows such as:

* Account inquiries
* Fund transfers
* Credit score & loan checks
* KYC verification
* OTP-secured transactions
* Voice biometric authentication

Built using Python, NLP, and voice processing technologies, the system ensures accuracy, security, and a smooth conversational user experience.




---

## 🎯 **Key Features**

### ✔ **Voice-Based Banking**

Perform actions such as:

* “Check my balance”
* “Transfer ₹500 to Rahul”
* “Show my last 5 transactions”

### ✔ **Voice Biometrics**

Authenticates users by matching their voiceprint against stored voice embeddings.

### ✔ **OTP-Based Secure Transactions**

Uses Twilio API to send OTP for transaction verification.

### ✔ **NLP Intent Understanding**

Identifies user intent and extracts important entities (amount, names, dates).

### ✔ **Text-to-Speech Feedback**

Provides voice responses for a complete conversational experience.

### ✔ **Dummy Banking Database**

Includes 100 synthetic customer records with:

* Account number
* Balance
* Credit score
* Loan status
* Transaction history
* KYC details

### ✔ **Modular Architecture**

Easily expandable to mobile apps, cloud systems, or real core banking APIs.

---

## 🛠️ **Technology Stack**

### **Frontend**

* HTML, CSS, JavaScript
* Speech Recognition API
* Text-to-Speech (Browser & Python)

### **Backend (Python)**

* Pandas, NumPy
* Pyttsx3
* SpeechRecognition
* Twilio (OTP API)
* Pathlib, Regex, Time

### **AI/NLP & Biometrics**

* NLP intent detection
* Voice embeddings for authentication
* Contextual conversation handling

### **Database**

* CSV-based dummy banking dataset
* Logs for transactions, KYC, loan status, etc.

---

## 🧠 **System Architecture**

### **1. User Interaction Layer**

Captures voice input → Converts to text → Sends to backend.
Responds through TTS.

### **2. NLP & Processing Layer**

Extracts action, amount, name, and context from user commands.

### **3. Authentication Layer**

* Voice biometrics
* OTP verification
* Session tokens

### **4. Banking Logic Layer**

Performs operations such as:

* Balance inquiry
* Sending money
* Loan status
* Transaction logs

### **5. Data Layer**

Stores customer profiles, balances, KYC status, and transaction history.

### **6. Response Layer**

Generates voice and text-based responses for the user.

---

## 📂 **Project Structure**

```
/BankAI
│── backend/
│── frontend/
│── database/
│── voice_engine/
│── OTP.py
│── Speech rec.py
│── main.py
│── requirements.txt
│── README.md
```

---

## 🔐 **Security Features**

* **2FA (Voice + OTP)**
* **Data masking**
* **Encrypted API interactions**
* **Fraud monitoring**
* **Audit logging**
* **Regulatory compliance (RBI, GDPR principles)**

---

## 📈 **Scalability & Future Enhancements**

* Integration with real banking APIs
* Multilingual voice assistant
* Mobile app integration
* Real-time cloud speech engines
* NoSQL storage for audit logs
* AI-powered fraud detection

---


## 🎥 **Demo Video**

🔗 [https://drive.google.com/file/d/1B7lMCwDlovtzTezydOuy-S7Y4bQhV0_J/view?usp=sharing](https://drive.google.com/file/d/1B7lMCwDlovtzTezydOuy-S7Y4bQhV0_J/view?usp=sharing)

---

## 🧪 **Installation & Setup**

### 1. Clone the repository

```
git clone https://github.com/ronitBiswas14/BankAI.git
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python main.py
```

### 4. Ensure microphone permissions are enabled.

---

## 🤝 **Contributing**

Pull requests are welcome!
Please avoid uploading real API keys — use environment variables instead.

---

