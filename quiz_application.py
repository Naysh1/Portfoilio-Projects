import random
import time

maximum = 20
q1 = ["Utha le re deva! whose dialogue is it?\n1.Raju 2.kabira \n3.baburao 4.shyam"]
q2 = [
    "Who is Prime Minister of India? \n1.Narendra Modi 2.Rahul Gandhi \n3.Arvind kejarival 4.Pappu"
]
q3 = [
    "What is the fastest that exists? \n1.DC Flash 2.Turtle \n3.Space Rocket 4.Your crush Reply"
]
q4 = [
    "Which game is famous for Parkour?  \n1.Assassin's Creed 2.Minecraft \n3.Hitman 4.Need for Speed"
]
q5 = [
    "Which marvel character name is Tony Stark?\n1.Black Widow 2.Spider-Man \n3.Iron Man 4.Hulk"
]
q6 = [
    "What is full form of GTA? \n1.Global Technology Authority 2.Great Tesla's Aircraft \n3.Gussa Tanhai Alasya 4.Grand Theift Auto"
]
q7 = [
    "What is most important thing in Fast & Furious? \n1.Cars 2.Guns \n3.Family 4.Money"
]
q8 = [
    "What is a keyboard? \n1.Key of succuss 2.Key without a lock \n3.An input device 4.Key of hidden truths"
]
q9 = ["Name of which language is based on a snake? \n1.Java 2.Python \n3.Ruby 4.C++"]
q10 = [
    "How can you have lot of Money? \n1.Ambani ke ghr janam 2.Paisa to hath ka mel hai \n3.Get a tree of Money 4.Work hard,use your skills,follow your passion"
]


roll = random.randint(100, 201)


def start():
    enter_roll = int(input("Roll No.:- "))
    if enter_roll == roll:
        print(" ")
        questions()
    else:
        print("Enter valid roll no. to start quiz.")
        return start()


list_questins = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
answer_list = [3, 1, 3, 1, 3, 4, 3, 3, 2, 4]
user_answer_list = []


def questions():
    i = 0
    while i < len(list_questins):
        print(f"Q{i+1}", list_questins[i][0])
        global answer
        answer = int(input("Enter your answer (1,2,3,4) : "))
        user_answer_list.append(answer)
        print(" ")
        i = i + 1


def correct_answer():
    global total, correct, wrong
    total = 0
    correct = 0
    wrong = 0
    for i in range(0, len(list_questins)):
        if user_answer_list[i] == answer_list[i]:
            total += 2
            correct += 1
        else:
            wrong += 1


def passing(name):
    print("Wait for a while your result is being generated...")
    time.sleep(5)
    percent = (total / maximum) * 100
    if percent >= 60:
        print(
            f"""
        * Correct Answers- {correct}   
        * Wrong Answers-{wrong}   
        * Percentange- {percent}%\n"""
        )
        print(f"Congrats {name}!, You passed this quiz.")
    else:
        print(
            f"""
        * Correct Answers- {correct}   
        * Wrong Answers-{wrong}   
        * Percentange- {percent}%\n"""
        )
        print("Sorry! You failed this quiz, Try again later. ")


if __name__ == "__main__":
    print("*****Welcome to the Epic Quiz*****")
    Full_name = str(input("Enter your name :- "))
    print(
        f"""{Full_name} Your Roll no. is {roll}
        
        * Maximum Marks are - 20
        * No. of questions are - 10
        * Passing marks are 60%\n"""
    )
    print("Please enter your roll no. to start the Epic Quiz.")
    start()
    correct_answer()
    passing(Full_name)
