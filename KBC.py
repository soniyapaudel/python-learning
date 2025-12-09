# Create a Program Capable of displaying questions to the user like kBC
# Use list data type to store the questions and their answers 
# Display the final amount the person is taking home after playing the game 




questions = [
    {
    "question": "What is the capital city of France?",
    "options": ["a.Berlin", "b.Madrid", "c.Paris", "d.Rome"],
    "answer": "c"
    },

    {
        "question": "Which is the Largest Planet in our Solar System?",
        "options": ["a.Earth", "b.Jupiter", "c.Saturn", "d.Neptune"],
        "answer": "b"

    },
    {
        "question": "Who Created the Python Programming Language?",
        "options": ["a.James Gosling", "b.Dennis Ritchie", "c.Guido Van Rossum", "d.Tim Berners-Lee"],
        "answer": "c" 
    },
    {
        "question": "What is the value of 3+ 2 * 2? ",
        "options": ["a.7", "b.10", "c.6", "d.5"],
        "answer": "a"
    },
    {
        "question": "Which command is used to exit the Python interactive shell ",
        "options":["a.stop()", "b.exit()", "c.quit()", "d. Both B and c"],
        "answer": "b"

    },
    {
        "question": "Which is the largest ocean on the Earth?",
        "options": ["a.Indian Ocean", "B.Pacific Ocean ", "c.Atlatic Ocean", "D.Arctic Ocean"],
        "answer": "b"
    }
]

#----List of Prizes 

prizes = [1000, 2000, 5000, 10000, 25000, 50000]

def playGame():
    total_amount = 0
    print("\n \t \t Welcome to Kaun Banega Crorepati! \n")

    for i in range(len(questions)):
        q = questions[i]
        print("\n Question", i+1 , "For Rs.", prizes[i])
        print(q["question"])

        #----print Options----

        for option in q["options"]:
            print(option)

            #----Take user input-------
        user_ans = input("Your answer:").lower()

            #----Check user answer----
        if user_ans == q["answer"]:
             total_amount +=  prizes[i]
             print("Correct You won: ",prizes[i])

        else:
            print("Wrong answer")
            break

    print("Game Over! Your total Winnings:", total_amount)

playGame()
