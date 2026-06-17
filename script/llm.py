import google.generativeai as genai

from prompt import schema

genai.configure(

api_key="YOUR_GEMINI_KEY"

)

model = genai.GenerativeModel(
"gemini-2.5-flash"
)

def generate_sql(question):

    prompt = schema + question

    response = model.generate_content(prompt)

    return response.text