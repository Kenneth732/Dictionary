def print_nested_dict(d, indent=0):
    for key, value in d.items():
        if isinstance(value, dict):
            print(f'{" " * indent}{key}:')
            print_nested_dict(value, indent + 2)
        elif isinstance(value, list):
            print(f'{" " * indent}{key}:')
            for item in value:
                if isinstance(item, dict):
                    print_nested_dict(item, indent + 2)
                else:
                    print(f'{" " * (indent + 2)}{item}')
        else:
            print(f'{" " * indent}{key}: {value}')

person = {
    'firstName': 'Dean',
    'lastName': 'Deo',
    'hobbies': [
        {
            'name': 'Video Games',
            'type': 'Indoor'
        },
        {
            'name': 'Hiking',
            'type': 'Outdoor'
        }
    ],
    'job': [
        {
            'company': 'Google',
            'position': 'Front End'
        },
        {
            'company': 'LinkedIn',
            'position': 'Back End'
        }
    ],
    'friends': [
        {
            'name': 'Mike'
        },
        {
            'name': 'Mary'
        }
    ]
}

print_nested_dict(person)
