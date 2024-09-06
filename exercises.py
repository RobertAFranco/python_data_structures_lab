# 1

def manage_students():
    # Create a list of student names
    students = ['Alice', 'Bob', 'Charlie']
    
    # Assign the second student's name to first_student
    first_student = students[1]
    
    # Assign the last student's name to last_student
    last_student = students[-1]
    
    return first_student, last_student

print('Exercise 1:', manage_students())


# 2

def combine_foods():
    # Create a tuple of foods
    foods = ('pizza', 'burger', 'pasta')
    
    # Initialize an empty string
    meal = ''
    
    # Use a loop to concatenate each food item to the meal string
    for food in foods:
        meal += food + ' '
    
    return meal.strip()  # Remove trailing space

print('Exercise 2:', combine_foods())

# 3

def slice_foods():
    # Create a tuple of foods
    foods = ('pizza', 'burger', 'pasta')
    
    # Slice the tuple to get the last two food strings
    last_two_foods = foods[-2:]
    
    return last_two_foods

print('Exercise 3:', slice_foods())

# 4

def hometown_info():
    # Create a dictionary with city, state, and population
    home_town = {
        'city': 'San Francisco',
        'state': 'California',
        'population': 883305
    }
    
    # Format a string using the dictionary
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    
    return home_town_message

print('Exercise 4:', hometown_info())  

# 5

def list_home_town_items():
    # Define the home_town dictionary
    home_town = {
        'city': 'San Francisco',
        'state': 'California',
        'population': 883305
    }
    
    # Initialize an empty list
    home_town_items = []
    
    # Iterate over the dictionary items
    for key, value in home_town.items():
        # Append formatted string to the list
        home_town_items.append(f"{key} = {value}")
    
    return home_town_items

print('Exercise 5:', list_home_town_items())


