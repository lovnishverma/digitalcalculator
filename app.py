from flask import Flask, render_template, request


app = Flask(__name__)

#number1=eval(input("Enter first number: "))

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/calc')
def calculator():
  return render_template('calc.html')
#     sign=str(input("Enter sign: "))
#     number2=eval(input("Enter another number: "))
#     if sign=='+':
#         number=number+number2
#         print(number)
#     elif sign=='-':
#         number=number-number2
#         print(number)
#     elif sign=='*':
#         number=number*number2
#         print(number)
#     elif sign=='/':
#         number=number/number2
#         print(number)
if __name__ =='__main__':
  app.run(debug=True)