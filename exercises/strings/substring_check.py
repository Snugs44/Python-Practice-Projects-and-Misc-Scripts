def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False

print(contains("watermelon", "melon"))