import os

# Check if the file exists and is not empty
file_path = "weather.txt"
if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    print(f"Error: The file '{file_path}' does not exist or is empty.")
    exit()

# Prompt the user for weather input
weather = input("Enter the weather (sunny, rainy, cold): ").strip().lower()

# Check the weather condition
if weather == "sunny":
    print("It's a bright and beautiful day! Don't forget your sunglasses.")
elif weather == "rainy":
    print("It's wet outside. Don't forget your umbrella!")
elif weather == "cold":
    print("It's chilly. Wear a warm coat.")
else:
    print("Invalid weather input. Please enter 'sunny', 'rainy', or 'cold'.")
