import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(f"\n{todo}")
    functions.write_todos(todos)

st.title("My Todo App")
st.header("This is my todo app.")
st.write("This app is to increase your productivity by managing your tasks.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]  # Remove the checkbox state
        st.rerun()

st.text_input(label="Enter a new todo item", placeholder="e.g. Buy groceries", 
              on_change=add_todo, key="new_todo")

st.session_state