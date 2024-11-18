from pydantic import BaseModel

from app.crawler import Crawler


class Service:
    crawler = None
    def __init__(self):
        self.crawler = Crawler('https://tehisintellekt.ee/')

    def get_source_info(self):
        return self.crawler.get_source_info()

    def get_system_message(self):
        message = ("You are a helpful chatbot who will answer the user's "
                   "question based only on the data provided in this message. "
                   "You will also add the url's of the websites you got the information from as sources.")
        source_info = self.get_source_info()

        for key, value in source_info.items():
            message += "The website with the url " + key + " contains the following text: " + value + " "

        return message

class Question(BaseModel):
    question: str

class Usage(BaseModel):
    input_tokens: int
    output_tokens: int

class Response(BaseModel):
    user_question: str
    answer: str
    usage : Usage
    sources: list[str]