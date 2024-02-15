name = (input("Jackie/Sebastian/Alora/Kevin: "))
if name == ("Jackie", "Sebastian", "Alora", "Kevin"):
  print("continue")
else:
  print("Please select one of our therapists")   
#Introduction of therapist and patient
print("Hello,my name is", name)
name_2 = input("What is your name: ")
print()
print("Hello", name_2)
print("I assure you",name_2,"that everything you'll tell me will remain private. ")
print()
print("Let me introduce myself better")
if name == "Jackie":
    print("My name is Jackie Mereba and I've been a therapist for 5 years")
elif name == "Sebastian":
    print("My name is Sebastian Lamar and I've been a therapist for 4 years")
elif name == "Alora":
    print("My name is Alora Hills and I've been a therapist for 3 years")
else:
    print("My name is Kevin Tyrese and I've been a therapist for 2 years") 
#Start of session
print("So how are you", name_2, "?")
state = input("Good/bad: ")
if state == "Good":
    print("Oh really,tell me about it!")
else:
    print("What's wrong?")
print()
explanation= input()
if "love" in explanation:
    print("Tell me about your new partner!")
elif "friend" in explanation:
    print("Tell me about your new friend!")
elif "education" or "graduation" in explanation:
    print("Tell me all about it!")
elif "job" or "promotion" in explanation:
    print("Oh really I'm so happy for you tell me about it!")
else:
    print("That's nice tell me more!")
print()
explanation_2 = input()
if "friend" in explanation_2:
    print("I hope your friendship lasts if they are making you feel this good. Do you see this friendship lasting for long?")
elif "love" in explanation_2:
    print("I hope your relationship lasts for long because you seem happy about them. How do you see your relationship in the next 5 years?")
elif "studying" in explanation_2:
    print("Congratulations on finishing well. What are your plans after this?")
elif "promoted" or "job" in explanation_2:
    print("Congratulations,you earned it because of your hard work.What do you look forward to in your new position")
else:
    print("I'm proud of you!")
print()
explanation_3 = input()
if "years" in explanation_3:
    print("That's nice.It's nice you have found someone perfect for you!")
elif "plan" in explanation_3:
    print("I'm so happy to hear this. I hope you'll work on those plans and everything will go smoothly.")
else:
    print("I hope your expectations will be met.")
#End session
print()
print("It seems our time is over. I will schedule the next session and tell you the details.")
goodbye = input()
if "Ok" or "ok" or "Thank you" or "Goodbye" or "Bye" in goodbye:
    print("Ok bye and thank you for trusting me to be your therapist.See you soon.")



