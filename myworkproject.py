print("🌟 Welcome to Your Personalized Day Planner! 🌤️")
print("Plan your day based on the simulated weather. Let's get started!\n")
activities = []
num_activities = int(input("How many activities do you want to plan today? "))
print("\nGreat! Please enter the activities you'd like to plan:")

for i in range(num_activities):
    activity = input(f"Enter activity {i+1}: ")
    activities.append(activity)

print("\nYou've planned:", activities)
import random

times_of_day = ["Morning", "Afternoon", "Evening"]
weather_conditions = ["Sunny", "Cloudy", "Rainy"]

# Randomly assign weather to each part of the day
weather = {time: random.choice(weather_conditions) for time in times_of_day}

print("\nToday's Weather Forecast:")
for time, condition in weather.items():
    print(f" - {time}: {condition}")
suggestions = {}

for activity in activities:
    if "Sunny" in weather.values():
        best_time = [time for time, cond in weather.items() if cond == "Sunny"][0]
    else:
        best_time = random.choice(times_of_day)
    suggestions[activity] = best_time
print("\n🌈 Your Day Plan:")
for activity, time in suggestions.items():
    print(f" - {activity.capitalize()} is best scheduled for the {time} when it's {weather[time]}.")

print("\nEnjoy your day! 😊")
