from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for information in question_data:
    # print(information)
    new_question = Question(information["text"], information["answer"])
    question_bank.append(new_question)

quiz_1 = QuizBrain(question_bank)

while quiz_1.still_has_questions():
    answer = quiz_1.next_question()

print(f"\nYou've completed the quiz"
      f"\nYour final score was: {quiz_1.score}/{quiz_1.question_number}")
