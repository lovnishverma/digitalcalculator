from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def calculate():
    try:
        expression = request.form['expression']
        result = eval(expression)
        return render_template('calc.html', expression=expression, result=result)
    except Exception as e:
        error_message = str(e)
        return render_template('calc.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
