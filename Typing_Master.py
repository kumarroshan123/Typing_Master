def choose_words(category):
    categories_words = {
        "animals": ["dog", "cat", "elephant", "giraffe", "lion", "tiger", "zebra", "penguin", "kangaroo", "koala"],
        "fruits": ["apple", "banana", "orange", "grape", "watermelon", "kiwi", "strawberry", "mango", "pineapple", "peach"],
        "countries": ["USA", "Canada", "Japan", "India", "Brazil", "Australia", "Germany", "France", "Italy", "China"],
      "Colors": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"],
      "Vegetables": ["carrot", "broccoli", "spinach", "potato", "tomato", "cucumber", "bell pepper", "onion", "garlic", "celery"],
      "Sports": ["football", "basketball", "soccer", "tennis", "golf", "baseball", "volleyball", "hockey", "swimming", "cycling"],
      "Movies": ["action", "comedy", "drama", "horror", "sci-fi", "romance", "thriller", "fantasy", "animation", "documentary"],
      "Technology": ["computer", "software", "internet", "keyboard", "mouse", "smartphone", "tablet", "laptop", "algorithm", "programming"],
      "Musical Instruments": ["piano", "guitar", "violin", "trumpet", "drums", "flute", "saxophone", "clarinet", "bass guitar", "accordion"],
      "Planets": ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "sun"],
      "Weather": ["rain", "sunshine", "clouds", "wind", "storm", "snow", "hail", "fog", "thunder", "lightning"],
      "Clothing": ["shirt", "pants", "dress", "jacket", "shoes", "hat", "socks", "gloves", "scarf", "tie"],
      "Insects": ["ant", "bee", "butterfly", "dragonfly", "mosquito", "spider", "ladybug", "grasshopper", "beetle", "caterpillar"]
    }

    return categories_words.get(category, [])
def main():
    print("Welcome to Terminal Typing Master!")
    username = input("Enter your username: ")

    while True:
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")
        if choice == "1":
          category = input("Choose a typing category (animals, fruits, countries, Colors, Vegetables, Sports, Movies, Technology, Musical Instruments, Planets, Weather, Clothing, Insects): ")
          words = choose_words(category)

          if not words:
              print(f"Error: Words for category {category} not found.")
              continue
