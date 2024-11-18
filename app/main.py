from fastapi import FastAPI

from openai import OpenAI

from app.service import Question, Response, Service

API_KEY = open("app/API_KEY").read().strip()

client = OpenAI(api_key=API_KEY)

service = Service()
app = FastAPI()

@app.get("/source_info")
async def source_info():
    if service is not None:
        return service.get_source_info()

@app.post("/ask")
async def ask(question: Question):

    system_message = service.get_system_message()

    response = client.beta.chat.completions.parse(
       model='gpt-4o-mini',
       messages=[
           {
               "role": "system",
               "content": system_message
           },
           {
               "role": "user",
               "content": question.question
           }
       ],
        response_format=Response,
    )

    structured_response = response.choices[0].message.parsed

    return structured_response