import quiz
import topics


def admin_menu():
    print("1. Create topic name.")
    print("2. View of topics.")
    print("3. Create Quiz.")
    print("4. View Quizzes")
    print("5. Edit Quiz")
    print("6. Edit topic")
    print("7. Delete topic.")
    print("8. Delete quiz")
    print("0. Logout")


def user_menu():
    print("1. Take Quiz ")
    print("0. Logout")


print("option 1 for admin ")
print("option 2 for user")
admin = 1
user = 2
a = int(input("Enter your option: "))
if a == 1:
    admin_menu()
    print("=============")

    option = int(input("enter your option"))
    while option != 0:
        if option == 1:
            topics.enter_topic_name()
        elif option == 2:
            topics.print_topics(topics.read_topics())
            print("=============")
        elif option == 3:
            quiz.create_quiz()
        elif option == 4:
            quizzes = quiz.read_quizzes()
            quiz.print_quizzes(quizzes)
        elif option == 5:
            quiz.edit_quizzes()
        elif option == 6:
            topics.edit_topic()
        elif option == 7:
            topics.delete_topic()
        elif option == 8:
            quiz.delete_quiz()
        admin_menu()
        print("==============")
        option = int(input("enter your option"))

elif a == 2:
    user_menu()
    print("===============")
    option = int(input("enter your option"))
    if option == 1:
        quiz.select_quiz()

    else:
        print("Thanks for visiting")

