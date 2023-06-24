from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc', methods=['GET','POST'])
def calc():
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            operator = request.form['operator']
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                error_message = "Invalid operator selected."
                return render_template('calc.html', error=error_message)
                
            return render_template('calc.html', result= result)
        
        except (KeyError, ValueError):
            error_message = "Invalid input. Please enter valid numbers."
            return render_template('calc.html', error=error_message)
    
    return render_template('calc.html')

if __name__ =='__main__':
    app.run(debug=True)
