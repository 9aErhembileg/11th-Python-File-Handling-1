# Exercise 1
def write_shopping_list(items, filename):
    file=open(filename,"w")
    c=1
    for i in items:
        file.write(f"{c}. {i}\n")
        c=c+1
    file.close()

# Exercise 2
def read_names(filename):
    file = open(filename, "r")
    lst = file.readlines()
    act = []
    for i in lst:
        if i.strip()!="":
            act.append(i.strip())
    file.close()
    return act

# Exercise 3
def append_entry(filename, text):
    file = open(filename,"a")
    file.write(f"\n{text}")
    file.close()
    file = open(filename,"r")
    file.close()
    return len(file.readlines())

# Exercise 4
def search_file(filename, word):
    file= open(filename,"r")
    con = []
    cur=1
    temp = file.readlines()
    for i in temp:
        if word in i.strip():
            con.append(cur)
        cur=cur+1
    file.close()
    return con

# Exercise 5
def number_the_lines(source, destination):
    file = open(source,"r")
    temp = file.readlines()
    file.close()
    lst = []
    cou=0
    for obj in temp:
        lst.append(obj.strip())
    file = open(destination,"w")
    for thi in lst:
        file.write(f"{cou+1}. {thi}/n")
        cou=cou+1
    file.close()
    print(cou)
