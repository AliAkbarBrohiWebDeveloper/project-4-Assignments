import streamlit as st
st.title("Calculator")
st.write("This is a Simple calculator that can perform Addition,Substraction,Multiplication and Division")

def calculator(num1,num2,operation):
    if operation=="Add":
      return num1 + num2
    elif operation=="Substract":
       return num1-num2
    elif operation=="Multiply":
       return num1* num2
    elif operation=="Divide":
       return num1/num2
num1=st.number_input("Enter your first Number ", value=0)
num2=st.number_input("Enter your second Number " ,value=0)  
operation=st.radio("Select your operater",("Add","Substract","Multiply","Divide"))  
if st.button("Calculate"):
   try:
      result=calculator(num1,num2,operation)
      st.write(f"The result of {num1} {operation} {num2} is  : {result}")
   except ZeroDivisionError as e:
      st.error(e)
   except ValueError as e:
      st.error(e)
   except Exception as e:
      st.error(f"An error accured : {e}")

   
calculator(num1,num2,operation)
