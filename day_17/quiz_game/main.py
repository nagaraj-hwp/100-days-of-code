from question_model import Question
from data import question_data, another_question_data
from quiz_brain import QuizBrain

question_bank = []

for question in another_question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_have_questions():
    quiz.next_question()

final_score = quiz.get_final_score()
print("--------------------------------")
print("| You have completed the Quiz! |")
print(f"| Your Final score is {final_score}/{len(question_bank)}     |")
print("--------------------------------")
