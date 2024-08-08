import html

import data
from question_model import Question
from quiz_brain import QuizBrain

question_data = data.main()
question_bank = []

for question in question_data["results"]:
    # This decodes the HTML symbols recieved from the API Call's questions
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score was {quiz.score}/{quiz.question_number}.")
