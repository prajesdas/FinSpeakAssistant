AI Voice Assistant for Financial Banking Operations

An intelligent voice-driven banking assistant that enables users to perform secure financial operations using Natural Language Processing (NLP), Speech Recognition, Voice Biometrics, and AI-powered automation.

⭐ Overview

The AI Voice Assistant for Financial Banking Operations is designed to make digital banking more accessible, faster, and highly secure.
It allows users to interact naturally with financial services through voice commands such as:

Checking account balance

Transferring money

Viewing transaction history

Loan and credit verification

KYC verification

Generating OTP authentication

Personalized financial alerts

This project integrates AI, NLP, Speech Recognition, Voice Biometrics, and secure backend logic, aiming to provide hands-free banking for users including elderly citizens, people with disabilities, and individuals with limited digital literacy.

🎯 Objectives

Enable core banking actions through natural voice commands

Provide secure authentication using Voice Biometrics + OTP verification

Understand user intent using NLP models

Ensure high security and compliance with financial standards

Deliver a conversational, user-friendly experience

Maintain modular architecture for easy scaling

Promote digital banking inclusion for all users

🛠️ Technology Stack
Frontend

HTML5, CSS3, JavaScript

Speech Recognition & Speech Synthesis

Bootstrap / Tailwind CSS

Backend

Python

Pandas, NumPy

Pathlib, Regex, Time

Pyttsx3 (Text-to-Speech)

Twilio API (OTP Verification)

SpeechRecognition Library (Voice → Text)

AI & NLP

Speech Recognition

NLP intent detection

Voice Biometrics using voice embeddings

Context-aware conversational logic

Database

CSV-based dummy banking dataset

Contains 100 synthetic customer profiles

Includes fields like account number, balance, credit score, KYC status, etc.

🧠 System Architecture
1️⃣ User Interaction Layer

Captures the user’s voice using browser or microphone

Converts voice to text

Returns responses through TTS (pyttsx3)

2️⃣ NLP & Processing Layer

Extracts intent (e.g., check balance, send money)

Understands entities like amount, name, date

Maintains multi-turn conversation context

3️⃣ Authentication Layer

Voice Biometrics: verifies voice print (threshold ≥ 0.80)

OTP Verification: via Twilio API

Transactions require dual authentication

4️⃣ Banking Operations Layer

Handles:

Balance inquiry

Transfers

KYC verification

Loan status

Credit score checks

Transaction history

Interest calculations

5️⃣ Data Management Layer

CSV-based storage for:

Customer details

Transaction logs

KYC/Loan info

Balances & account status

6️⃣ Response Layer

Returns confirmation via voice output

Displays details on screen

Logs every transaction securely

📂 Database Schema (Simplified)
Field	Description
Customer_ID	Unique ID
Name	Customer name
Account_No	Bank account number
Balance	Current balance
No_of_Transactions	Total completed transactions
Last_Payment	Last payment description
Loan_Status	Active/Closed
Interest_Rate	Applicable rate
Credit_Limit	Customer credit limit
Reminder_Type	Alerts/EMI reminders
Alerts_Enabled	Notification settings
Last_Transaction_Date	Timestamp
🔐 Security & Compliance
Authentication & Authorization

Voice Biometrics

OTP via Twilio

Session-based tokens

Data Protection

Masking sensitive information

Encrypted communication

Audit logs for every financial action

Regulatory Alignment

RBI Digital Banking Guidelines

GDPR Data Privacy Principles

ISO/IEC 27001 Security Standards

Fraud Prevention

OTP for every high-risk action

Voice spoof detection

Transaction validation limits

🚀 Features
✔ Voice-Driven Banking

No need for typing—just speak naturally.

✔ Voice Biometrics

Password-less secure login.

✔ Real-Time Fund Transfers

Automated balance updates.

✔ Intelligent NLP Understanding

Understands natural queries:
"Send ₹500 to Rahul"
"What is my loan status?"

✔ OTP Validation

Dual-layer authentication for safety.

✔ Financial Insights

Credit score, limits, interest rate, and more.

✔ 100-Record Dummy Banking Database

Simulates real banking system behavior.

📈 Scalability

The system supports future upgrades:

Core banking API integration

Mobile app adaptation

Cloud deployment

Multilingual voice support

Microservices architecture

Edge AI processing

🧪 AI / ML Components

Speech-to-text (ASR)

NLP intent detection

Voice similarity model

TTS engine for responses

Automated transaction workflows

📊 Flow Chart

(Include the flowchart from your PDF if needed)

📦 Project Structure
/BankAI
│── /frontend
│── /backend
│── /database
│── /voice_engine
│── OTP.py
│── Speech rec.py
│── main.py
│── requirements.txt
│── README.md

📹 Demo Video

▶ https://drive.google.com/file/d/1B7lMCwDlovtzTezydOuy-S7Y4bQhV0_J/view?usp=sharing

📁 GitHub Repository

🔗 https://github.com/prajesdas/FinSpeakAssistant.git
