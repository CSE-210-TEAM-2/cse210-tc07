



with open("name.txt", "rt") as infile:

    # Read all the quotes in the file into a list.
    string = infile.read()
    words = string.splitlines()




    words = random.choice(words)
