from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('main.html')

@app.route('/10sec', methods = ['POST', 'GET'])
def minimum():
    print("works #1")
    return render_template('main.html')
    
@app.route('/15sec', methods = ['POST', 'GET'])
def low():
    print("works #2")
    return render_template('main.html')

@app.route('/20sec', methods = ['POST', 'GET'])
def medium():
    print("works #3")
    return render_template('main.html')

@app.route('/25sec', methods = ['POST', 'GET'])
def high():
    print("works #4")
    return render_template('main.html')



@app.route('/post',methods = ['POST', 'GET'])
def CustomTime():
   if request.method == 'POST':
        first_name = request.form.get("DelayTime")
        print(first_name)
        return render_template('main.html')
   

if __name__ == '__main__':
    app.run()