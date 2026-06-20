import google.generativeai as genai

genai.configure(
    api_key="AQ.Ab8RN6I0v0ab4G2IfbWwNGWDLr7nzwicUsDpI6zH-KeaZET9Mg"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

response = model.generate_content(
    "Say hello in one sentence."
)

print(response.text)