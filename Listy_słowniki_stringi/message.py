def message(input_dict):
    if 'movie' not in input_dict or 'name' not in input_dict or 'role' not in input_dict:
        return None
    return "In {movie}, {name} is a {role}.".format(** input_dict)
    # return "In {}, {} is a {}.".format(input_dict['movie'], input_dict['name'], input_dict['role'])


input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))  # In Star Wars, Han Solo is a smuggler.

input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))  # None