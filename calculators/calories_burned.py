# Workout Calorie's Burned Calculator


age = float(input('Enter your age in years: '))

weight = float(input('Enter your weight in pounds: '))

heart_rate = float(input('Enter your average heart rate from your workout in beats per minute: '))

time = float(input('How long did you exercise for in minutes?: '))


Calories = (age * 0.2757) + (weight * 0.03295) + ((heart_rate * 1.0781) - 75.4991) * (time / 8.368)

print('Calories: {:.2f} calories'.format(Calories))