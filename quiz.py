import json
import os
import topics
from common import obj_dict


class Question:
    def __init__(self,topic_name,difficulty, question, option1, option2, option3, option4, answer):
        self.topic_name=topic_name
        self.difficulty = difficulty
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.answer = answer


def read_questions(quiz_question_file_name):
    if not os.path.isfile("quiz_questions"+os.sep+quiz_question_file_name):
        return []
    fp = open("quiz_questions"+os.sep+quiz_question_file_name, 'r')
    content = fp.read()
    fp.close()
    if content is None or content == "":
        return []
    dict_content = json.loads(content)
    return list(dict_content)


def write_questions(questions, quiz_question_file_name):
    fp = open("quiz_questions"+os.sep+quiz_question_file_name, 'w+')
    dump_data = json.dumps(questions, default=obj_dict, indent=1)
    fp.write(dump_data)
    fp.close()

def print_questions(questions):
    for i in range(len(questions)):
        print(str(i + 1) + " - " + questions[i]['name'])


# =============================================================================
class Quiz():
    def __init__(self, name):
        self.name = name


def read_quizzes():
    if not os.path.isfile("quiz.json"):
        return []
    fp = open('quiz.json', 'r')
    content = fp.read()
    fp.close()
    if content is None or content == "":
        return []
    dict_content = json.loads(content)
    return list(dict_content)


def write_quizzes(quizzes):
    fp = open('quiz.json', 'w+')
    dump_data = json.dumps(quizzes, default=obj_dict, indent=1)
    fp.write(dump_data)
    fp.close()


def print_quizzes(quizzes):
    for i in range(len(quizzes)):
        print(str(i + 1) + " - " + quizzes[i]['name'])


def edit_quizzes():
    print("1. Edit quiz name.")
    print("2. Edit quiz questions.")
    quizzes = read_quizzes()
    if quizzes is None or quizzes == []:
        print("There is no quiz to be edited.")
    opt = int(input("Enter your option"))
    if opt == 1:
        print_quizzes(quizzes)
        quiz_number = int(input("Enter Quiz number to be edited: "))
        new_name = input("Enter new Quiz name: ")
        quiz_name = quizzes[quiz_number - 1]['name']
        quizzes[quiz_number - 1]['name'] = new_name
        write_quizzes(quizzes)
        os.rename(quiz_name + ".json", new_name + ".json")
    elif opt==2:
        print_quizzes(quizzes)
        quiz_number = int(input("Enter Quiz number to be edited: "))
        quiz_name = quizzes[quiz_number - 1]['name']
        print("select topic")
        topics_list = topics.read_topics()
        topics.print_topics(topics_list)
        topic_number = int(input("enter topic number"))
        topic_name = topics_list[topic_number - 1]["name"]
        difficulty = input("enter difficulty level // Easy  // Medium // Hard:  ")
        question = input("enter question: ")
        option1 = input("enter option 1: ")
        option2 = input("enter option 2: ")
        option3 = input("enter option 3: ")
        option4 = input("enter option 4: ")
        answer = input("enter answer: ")
        que = Question(topic_name, difficulty, question, option1, option2, option3, option4, answer)
        questions = read_questions(quiz_name+".json")
        questions.append(que)
        write_questions(questions, quiz_name+".json")
# =============================================================================================




def delete_quiz():
    quizzes = read_quizzes()
    print_quizzes(quizzes)
    quiz_number = int(input("Enter Quiz number to be Deleted"))
    os.remove("quiz_questions"+os.sep+quizzes[quiz_number - 1]['name']+".json")
    quizzes.remove(quizzes[quiz_number - 1])
    write_quizzes(quizzes)


def select_quiz():
    quizzes = read_quizzes()
    print_quizzes(quizzes)
    quiz_number = int(input("Enter Quiz number you want to take"))
    quiz_question_file_name=quizzes[quiz_number - 1]['name'] + ".json"
    run_quiz(quiz_question_file_name)




def create_quiz():
    quiz_name = input("enter Quiz name")
    quiz = Quiz(quiz_name)
    quiz_question_file_name = quiz_name + ".json"
    quizzes = read_quizzes()
    quizzes.append(quiz)
    write_quizzes(quizzes)
    write_questions([], quiz_question_file_name)
    quiz_menu()
    op = int(input("enter the option"))
    while op != 0:
        if op == 1:
            print("select topic")
            topics_list = topics.read_topics()
            topics.print_topics(topics_list)
            topic_number=int(input("enter topic number"))
            topic_name=topics_list[topic_number-1]["name"]
            difficulty = input("enter difficulty level // Easy  // Medium // Hard:  ")
            question = input("enter question: ")
            option1 = input("enter option 1: ")
            option2 = input("enter option 2: ")
            option3 = input("enter option 3: ")
            option4 = input("enter option 4: ")
            answer = input("enter answer: ")
            que = Question(topic_name,difficulty, question, option1, option2, option3, option4, answer)
            questions = read_questions(quiz_question_file_name)
            questions.append(que)
            write_questions(questions, quiz_question_file_name)
            quiz_menu()
            op = int(input("enter the option"))
        elif op == 2:
            print(read_questions(quiz_question_file_name))
            print("===============")
            op = int(input("enter the option"))
        else:
            break



def quiz_menu():
    print("1. Add questions.")
    print("2. list all questions")
    print("3. back")


def run_quiz(quiz_question_file_name):
    marks=0
    questions = read_questions(quiz_question_file_name)
    for i in range (len(questions)):
        topic_name=questions[i]["topic_name"]
        difficulty=questions[i]["difficulty"]
        question=questions[i]["question"]
        option1=questions[i]["option1"]
        option2 = questions[i]["option2"]
        option3 = questions[i]["option3"]
        option4 = questions[i]["option4"]
        answer = questions[i]["answer"]
        print("Topic_name = "+ topic_name)
        print("Difficulty = " + difficulty)
        print("Question.",str(i+1),"  "+  question)
        print("A   " + option1)
        print("B   "+ option2)
        print("C   " + option3)
        print("D   " + option4)
        answer_name=input("Enter your answer")
        if answer_name == answer:
            marks+=1
    print("Total Marks:  "+str(marks))