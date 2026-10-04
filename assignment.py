# ANSWER KEY - Python File Handling Lab
# Only uses open / read / readline / readlines / write / close

# Exercise 1 -----------------------------------------------------------------

def write_shopping_list(items, filename):
    file = open(filename, "w")
    number = 1
    for item in items:
        file.write(str(number) + ". " + item + "\n")
        number = number + 1
    file.close()


# Exercise 2 -----------------------------------------------------------------

def read_names(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    names = []
    for line in lines:
        name = line.strip()
        if name != "":
            names.append(name)
    return names


# Exercise 3 -----------------------------------------------------------------

def append_entry(filename, text):
    file = open(filename, "a")
    file.write(text + "\n")
    file.close()

    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return len(lines)


# Exercise 4 -----------------------------------------------------------------

def highest_score(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    best_name = ""
    best_score = -1
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        name = parts[0]
        score = int(parts[1])
        if score > best_score:
            best_score = score
            best_name = name
    return [best_name, best_score]


# Exercise 5 -----------------------------------------------------------------

def search_file(filename, word):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    found = []
    number = 1
    for line in lines:
        if word.lower() in line.lower():
            found.append(number)
        number = number + 1
    return found


# Exercise 6 -----------------------------------------------------------------

def number_the_lines(source, destination):
    file = open(source, "r")
    lines = file.readlines()
    file.close()

    out = open(destination, "w")
    count = 0
    for line in lines:
        count = count + 1
        out.write(str(count) + ": " + line.strip() + "\n")
    out.close()
    return count
