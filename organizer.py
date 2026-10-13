with open() as f("science-notes.txt", "r"):
    print(readline(f))


with open() as f("maths-notes.txt", "r"):
    for line in f:
        print(line.split())



merged_file= "allstudy-notes.txt"


if ospath.exists(merged_file):
    print(merged_file, "already exists")
else:
    print(merged_file, "doesnt exist yet")




if ospath.exists(merged_file):
    os.remove(merged_file)
    print( " merged file has been removed")
else:
    print(" no old merged file to remove")







