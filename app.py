from flask import Flask, render_template, request


app = Flask(__name__)

#number1=eval(input("Enter first number: "))
@app.route('/')
def index():
    return render_template('index.html')
  


@app.route('/calc')
def calculator(number):
    sign=str(input("Enter sign: "))
    number2=eval(input("Enter another number: "))
    if sign=='+':
        number=number+number2
        print(number)
    elif sign=='-':
        number=number-number2
        print(number)
    elif sign=='*':
        number=number*number2
        print(number)
    elif sign=='/':
        number=number/number2
        print(number)
    a=int(input("enter 0 for continue and 1 for quit: "))
    if a==0:
        calculator(number)

# if b==1:
#     calculator(sign)
a=calculator(number1)