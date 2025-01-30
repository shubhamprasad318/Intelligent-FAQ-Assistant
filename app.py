from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import google.generativeai as genai
import os

app = Flask(__name__)

# Set up MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["faq_assistant"]
kB_collection = db["knowledge_base"]

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Error: API key not found. Set GEMINI_API_KEY as an environment variable.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def load_knowledge_base():
    """Load all FAQs from MongoDB."""
    knowledge_base = {}
    for doc in kB_collection.find():
        knowledge_base[doc["question"]] = doc["answer"]
    return knowledge_base

knowledge_base = load_knowledge_base()

@app.route("/")
def home():
    """Render HTML frontend."""
    return render_template("index.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    """Fetch answer from DB or generate using Gemini API."""
    data = request.json
    user_question = data.get("question", "").strip()

    if not user_question:
        return jsonify({"error": "No question provided"}), 400

    # Check if the answer exists in the database
    answer = knowledge_base.get(user_question)
    if answer:
        return jsonify({"answer": answer})

    try:
        # Generate answer using Gemini API
        response = model.generate_content(user_question)
        generated_answer = response.text

        # Store the new question-answer pair
        kB_collection.insert_one({"question": user_question, "answer": generated_answer})

        return jsonify({"answer": generated_answer})
    except Exception as e:
        return jsonify({"error": f"API Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
