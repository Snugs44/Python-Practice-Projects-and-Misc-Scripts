def username_generator(first_name, last_name):
    username = first_name[:3] + last_name[:4]

    if len(first_name) < 3 or len(last_name) < 4:
        return first_name + last_name
    else:
        return username


print(username_generator("Abe", "Simpson"))