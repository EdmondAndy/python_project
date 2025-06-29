def get_todos(filepath='todos.txt'):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos, filepath='todos.txt'):
    """Write the list of to-do items to a text file."""
    with open(filepath, 'w') as file:
            file.writelines(todos)