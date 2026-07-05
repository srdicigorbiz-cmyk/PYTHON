from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def check(self, answer):
        pass

class YesNoQuestion(Question):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def print(self):
        print(f"[?] {self.question} (yes/no)")
    
    def check(self, player_answer):
        if self.answer == player_answer:
            return True
        else:
            return False
        

class OpenQuestion(Question):
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
    
    def print(self):
        print(f"[?] {self.question}")

    def check(self, player_answer):
        if player_answer in self.answers:
            return True
        else:
            return False    


class MultiOptionsQuestion(Question):
    def __init__(self, question, options, answer_index):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f"[?] {self.question}\n")
        for idx, q in enumerate(self.options, 1):
            print(f"[{idx}] {q}")

    def check(self, player_answer):
        if int(player_answer) == int(self.answer_index) + 1:
            return True
        else:
            return False


class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def start(self):
        results = []
        for q in self.questions:
            q.print()
            print("")
            user_answer = input('[+] ')
            print("\n")
            results.append(q.check(user_answer))
        
        self.print_results(results)

            #q.check(answer)
    def print_results(self, results):
        result = len(list(filter(lambda x: x == True, results)))
        print(f"Your score is {result}/{len(results)}\n")
        for idx, r in enumerate(results, 1):
            print(f"[{idx}] {'Pass' if r == True else 'Fail'}")
        
        
yesnoq1 = YesNoQuestion("Am I fine?", "yes")
yesnoq2 = YesNoQuestion("Am I Serbian?", "yes")
yesnoq3 = YesNoQuestion("Am I Hungarian?", "yes")
openq4 = OpenQuestion("Capital of Hungary or Serbia?", "Budapest Belgrade")
multiq = MultiOptionsQuestion("Which is the best currency?", ["USD", "GBP", "CHF", "DIN"], 2 )
q = Quiz([yesnoq1, yesnoq2, yesnoq3, openq4, multiq])
q.start()