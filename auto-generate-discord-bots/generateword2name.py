import random

def generate_random_name():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    name_length = random.randint(1, 5)
    name = 'word2' + ''.join(random.choice(letters) for _ in range(name_length))
    return name

# Generate 10 random names
print("generating 100000 word2 names")
num_names = 100000
names = [generate_random_name() for _ in range(num_names)]
print("succussfully generated 100000 word2 names")
# Save names in usernames.txt
print("saving names")
with open("names.txt", "w") as file:
    file.write('\n'.join(names))
    print("succussfully saved names")
    input("press enter to exit")
