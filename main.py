import sys

file_name = 'tasks.txt'
def print_usage():
    print("""

Command Line Todo application
=============================

Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task""")

def read_file(file_path):
    try:
        list_tasks = open(file_path, 'r')
        lines = list_tasks.readlines()
        list_tasks.close()
        return lines
    except IOError:
        print("cant open file")

def list_tasks():
    lines = read_file(file_name)
    if len(lines) == 0:
        print("No todos for today! :)")
    else:
        for number, line in enumerate(lines):
            goodlines = line.replace("\n", "")
            completed = goodlines[0]
            check = {'0': "[ ]", '1': "[x]"}
            print(str(number+1) + " - " + check[completed] + " " + goodlines[1:])

def add_task(task):
    try:
        fw = open(file_name, 'a')
        fw.write('\n0' + task)
        fw.close()
    except IOError:
        print("Can't open file")

def remove_task(number):
    lines = read_file(file_name)
    del lines[int(number)-1]
    write_file(file_name, lines)

def write_file(file_path, list):
    try:
        list_tasks = open(file_path, 'w')
        list_tasks.writelines(list)
        list_tasks.close()

    except IOError:
        print("cant open")

def check_task(number):
    lines = read_file(file_name)
    lines[int(number) - 1] = '1' + lines[int(number) - 1][1:]
    write_file(file_name, lines)


if len(sys.argv) == 1:
    print_usage()
elif len(sys.argv) == 2 and sys.argv[1] == "-l":
    list_tasks()
elif len(sys.argv) == 3 and sys.argv[1] == "-a":
    add_task(sys.argv[2])
elif len(sys.argv) == 3 and sys.argv[1] == "-c":
    check_task(sys.argv[2])
elif len(sys.argv) == 3 and sys.argv[1] == "-r":
    remove_task(sys.argv[2])
else:
    print("Unsupported argument")