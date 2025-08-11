from logging import PlaceHolder

import streamlit as st
from  support_func import clear_terminal , write_file, populate_todo_list , display_todo_list
# import FreeSimpleGUI as sg
import os
import time


#### Author : Parashar Bhatt
#### Code for: Web application to manage ToDo tasks

####  Local URL: http://localhost:8501
####  Network URL: http://10.252.3.223:8501
#### (.venv) PS C:\\m18_work\\udemy\\ThePythonMegaCourse\\Webapp_ToDo_Streamlit> streamlit run app1.py



current_location = os.getcwd()
# current_code_file_name = os.path.basename(__file__)
todo_file =os.path.join(current_location, 'data',"todo_file.txt")
if not os.path.exists(todo_file):
    with open(todo_file, 'w') as f:
        pass

# defining class for custom error message
class MyCustomError(Exception):
    """
    Custom exception raised for specific error scenarios.
    Attributes:
        message -- explanation of the error
        value -- optional value related to the error
    """
    def __init__(self, message, value=None):
        self.message = message
        self.value = value
        super().__init__(self.message) # Pass the message to the base Exception class

todo_list = populate_todo_list(todo_file)

def add_todo():
    try:
        todo_list = populate_todo_list(todo_file)
        todo_val = st.session_state['new_todo']
        print(todo)
        if todo_val.strip() !="":
            todo_val = todo_val.strip()+'\n'
        else:
            raise MyCustomError("Error: Blank cannot be added !")
        index_to_add = todo_list.index(todo_val)
        mesg = f"Todo item : {todo_val.strip('\n')}, is already exists!!"
        print(mesg)
        raise MyCustomError(f"Error: '{todo_val}' already exists in task list !")
        # todo_list.append(todo_val)

    except MyCustomError as e:
        print(e.message)
    except ValueError:
        # print('Index to add:', index_to_add)
        todo_list.append(todo_val)
        write_file(todo_file, todo_list)
        # window['todolist'].update(values=todo_list)
        #window['todo'].update(value='')
        print(todo_list)



st.title("ToDo WebApp")
### user = st.text_input("Enter your name")
user = "PB915's"
st.subheader(f"{user} ToDo task")



for todo in todo_list:
    st.checkbox(todo)

st.text_input(label = "", placeholder= "Add ToDo Task:", on_change=add_todo, key='new_todo')
