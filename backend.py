import openai, os
from dotenv import load_dotenv

class ChatBot:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("openaipw")
    def getresponse(self, chat_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=chat_input,
            max_tokens=1000,
            temperature=0.5 #measures accuracy of answer (breadth vs depth)
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.getresponse("write a poem about cheetahs and kangaroos")
    print(response)