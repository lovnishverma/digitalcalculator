from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/calc', methods=['POST'])
def calc():
  if request.method == 'POST':
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    #add= int(request.form['add'])
    # sub= int(request.form['sub'])
    # mul= int(request.form['mul'])
    # div= int(request.form['div'])
    result = ([[num1 + num2]])
    return render_template('calc.html', result)
    
if __name__ =='__main__':
  app.run(debug=True)