person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

# Check if 'favorite_colors' key exists in the dictionary
if 'favorite_colors' in person:
    favorite_colors = person['favorite_colors']
    
    # Loop through the list of favorite colors
    for color in favorite_colors:
        print(color)
else:
    print("No favorite colors found.")
