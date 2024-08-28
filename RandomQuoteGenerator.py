import random

def random_quote():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
        "In the end, we only regret the chances we didn’t take. – Lewis Carroll",
        "It does not matter how slowly you go as long as you do not stop. – Confucius",
        "Your time is limited, don’t waste it living someone else’s life. – Steve Jobs",
        "Whether you think you can or you think you can’t, you’re right. – Henry Ford",
        "The best way to predict the future is to create it. – Peter Drucker"
    ]

    return random.choice(quotes)

if __name__ == "__main__":
    print(random_quote())
