responses = {
    "hello": "Hi there!",
    "how are you": "I am doing well!",
    "what is your name": "My name is AI Bot.",
    "thanks": "You are welcome!",
    "bye": "Goodbye!"
}

print("=== Rule Based Chatbot ===")

while True:
    user = input("You: ").lower().strip()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    reply = responses.get(
        user,
        "Sorry, I don't understand that."
    )

    print("Bot:", reply)