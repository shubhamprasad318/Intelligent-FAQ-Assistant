# **Intelligent FAQ Assistant**

## **📌 Project Overview**

The **Intelligent FAQ Assistant** is a Flask-based web application that leverages **Large Language Models (LLM)** to provide dynamic responses to user queries. It integrates **MongoDB** for storing a knowledge base and logs user interactions. The system can either retrieve answers from the database or generate responses using the **Google Gemini API** when no predefined answer is found.

---

## **🚀 Features**

✅ **Knowledge Base Integration** – Stores predefined FAQs in MongoDB. ✅ **AI-Powered Responses** – Uses **Google Gemini API** for generating answers. ✅ **Flask Web Application** – Simple UI with real-time query handling. ✅ **Admin API** – Enables updating FAQs programmatically. ✅ **User Interaction Logging** – Logs queries and responses for future improvement. ✅ **Chat-style UI with Dark Mode** – Enhanced user experience. ✅ **Speech-to-Text Support** – Allows users to ask questions via voice.

---

## **🛠️ Installation & Setup**

### **1️⃣ Clone the Repository**

git clone https://github.com/shubhamprasad318/Intelligent-FAQ-Assistant  
cd Intelligent-FAQ-Assistant

### **2️⃣ Install Dependencies**

Ensure **Python 3.7+** is installed. Then, run:

pip install \-r requirements.txt

#### **`requirements.txt`**

Flask==3.0.0  
pymongo==4.5.0  
google-generativeai==0.4.0  
python-dotenv==1.0.0

### **3️⃣ Set Up Environment Variables**

Create a `.env` file and add:

GEMINI\_API\_KEY=your\_google\_gemini\_api\_key  
MONGO\_URI=mongodb://localhost:27017/

Or, set them in your terminal:

export GEMINI\_API\_KEY="your\_google\_gemini\_api\_key"  
export MONGO\_URI="mongodb://localhost:27017/"

### **4️⃣ Start MongoDB**

Ensure MongoDB is running:

mongod \--dbpath /path/to/db

### **5️⃣ Run the Flask App**

python app.py

The application runs at \`\`

---

## **🖥️ API Endpoints**

### **1️⃣ Home Page**

\*\*GET \*\*\`\` – Loads the **FAQ Assistant Web UI**.

### **2️⃣ Ask a Question**

\*\*POST \*\*\`\`

* **Request:**  
  { "question": "What is your return policy?" }  
* **Response (If found in DB):**  
  { "answer": "Our return policy allows returns within 30 days." }  
* **Response (Generated via AI):**  
  { "answer": "Our return policy allows returns within 30 days. If you need more details, visit our policy page." }

### **3️⃣ Add a New FAQ (Admin Only)**

\*\*POST \*\*\`\`

* **Request:**  
  { "question": "What are your business hours?", "answer": "We are open from 9 AM to 5 PM, Monday to Friday." }  
* **Response:**  
  { "message": "FAQ added successfully\!" }

### **4️⃣ View Logs**

\*\*GET \*\*\`\` – Fetches all logged user queries and answers from MongoDB.

---

## **🔥 Conclusion**

This project demonstrates how **AI-powered FAQ assistants** can enhance customer support by providing **instant, intelligent responses** via a simple web interface. 🚀

