import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    """add the todo_item to todo_list"""
    todo = st.session_state["new_todo"] + "\n"
    if todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)
    else:
        st.toast("you have existing todo")
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label=" ", placeholder="Add new todo...", on_change=add_todo, key="new_todo")


st.session_state





