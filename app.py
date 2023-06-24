from flask import Flask, render_template, request


app = Flask(__name__)

#number1=eval(input("Enter first number: "))

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/calc')
def calculator():
  return render_template('calc.html')
num1= int(request.form['num1'])
num2= int(request.form['num2'])
add= int(request.form['add'])
sub= int(request.form['sub'])
mul= int(request.form['mul'])
div= int(request.form['div'])
result = num1

    
if __name__ =='__main__':
  app.run(debug=True)