#Task 1: Your Mood Today 

# mood_responses.py

def mood_response(mood):
    if mood.lower() == "happy":
        return "Glad to hear that you're happy today!"
    elif mood.lower() == "sad":
        return "I'm sorry that you're feeling sad. Cheer up!"
    elif mood.lower() == "excited":
        return "Awesome! I hope you have a fantastic day!"
    else:
        return "I'm not sure how to respond to that mood. Let's hope for the best!"

def main():
    mood = input("How are you feeling today? ")
    response = mood_response(mood)
    print(response)

if __name__ == "__main__":
    main()