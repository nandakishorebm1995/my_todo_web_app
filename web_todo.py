import streamlit as st
import main_functions


todos = main_functions.get_todos()
print(todos)


def add_todo():
    todo = st.session_state["new_todo"] + '\n'  # session state is a dictionary type
    print(todo)
    todos.append(todo)
    main_functions.write_todo_file(todos)


st.title("My To-Do App")
st.subheader("This is my todo app.")
st.write("This app is to track your daily activities.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        main_functions.write_todo_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo here: ", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")
