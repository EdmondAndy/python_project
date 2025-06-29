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

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a new todo item", placeholder="e.g. Buy groceries", 
              on_change=add_todo, key="new_todo")

st.session_state