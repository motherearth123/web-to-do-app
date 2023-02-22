FILEPATH = "todos.txt"



def get_todos(filepath=FILEPATH):
    """ Reads  a text file and return list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local =\
            file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """  Write a to-do items list in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)
print("I am outside")

if __name__ == "__main__":
    print("Hello from  funtions")
    print(get_todos())