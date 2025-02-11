from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyCGgZtJmO0-yruBxbAtFVJrPsdRRK9olP8")

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents="I’m doing a marketing campaign for the launch of a new food product aimed at the 18-25 demographic, search the internet for what trends affecting this demographic might be informative to my campaign design?",
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            google_search=types.GoogleSearchRetrieval(
                dynamic_retrieval_config=types.DynamicRetrievalConfig(
                    dynamic_threshold=0.001))
        )]
    )
)
print(response)