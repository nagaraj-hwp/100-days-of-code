import requests

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def get_question(self):
        count = 0
        parameters = {
            "amount": 10,
            "category": 23,
            "difficulty": "easy",
            "type": "boolean",
        }

        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        # if response.status_code != 200:
        #     raise response.raise_for_status()
        response.raise_for_status()
        data = response.json()

        while count < 10:
            question = data["results"][count]["question"]
            answer = data["results"][count]["correct_answer"]
            print(question)
            print(answer)
            count += 1


