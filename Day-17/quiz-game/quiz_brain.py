class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = question_list

    def next_question(self):
        current_question = self.questions_list[self.question_number].text
        current_answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question} (True/False)?: "
        )
        self.check_answer(user_answer, current_answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"That is correct! Your score is {self.score}/{self.question_number}")
        else:
            print(
                f"That is incorrect! Your score is {self.score}/{self.question_number}"
            )
        print(f"The correct answer was: {correct_answer}.\n\n")
