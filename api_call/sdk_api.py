# import anthropic

# client = anthropic.Anthropic()

# response = client.messages.create(
#     model="claude-sonnet-4-20250514",
#     max_tokens=256,
#     messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
# )

# print(response.content[0].text)


#----------gemini model api call using the SDK-------------------

from dotenv import load_dotenv #dotenv is used to load environment variables from a .env file
import os #os module is used to access environment variables
import google.generativeai as genai #generativeai is the SDK for Google Gemini API

load_dotenv()  # reads .env and loads variables into environment

genai.configure(api_key=os.environ["GEMINI_API_KEY"]) #configure the SDK with the API key from environment variables

# print(ModelService.list_models()) #modelService.list_models() lists all the available models in the Gemini API
model = genai.GenerativeModel("gemini-3.5-flash") #gemini-3.5-flash is the model we are using for generating content
# response = model.generate_content("What is a neural network in one sentence?")
# response = model.generate_content("From SAP associate consultant role, can I get a job at Google if I learn AI and ML? And what things i need to learn to reach there in how much time? write it in within 10lines")
response = model.generate_content("What you know about CJP? tell me in 5lines")
print(response.text)

# #1. **Core Coding & Math:** Master Python, Data Structures & Algorithms (DSA), Linear Algebra, and Statistics.
# 2. **ML/DL Fundamentals:** Study Regression, Classification, NLP, and frameworks like PyTorch or TensorFlow.
# 3. **Generative AI:** Learn Large Language Models (LLMs), Prompt Engineering, and RAG (Retrieval-Augmented Generation).
# 4. **Cloud & MLOps:** Get certified in Google Cloud Platform (GCP) and master Vertex AI for model deployment.
# 5. **Bridge Projects:** Build AI applications that solve enterprise/ERP problems, leveraging your SAP domain knowledge.
# 6. **Interview Prep:** Solve 150+ LeetCode (medium) questions and study ML System Design.

# **Time required:** **12 to 18 months** of dedicated daily study (15–20 hours/week) to build a competitive profile.