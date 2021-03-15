from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/Catalogo')
def Catalogo():
    return render_template('Catalogo.html')

@app.route('/Contactenos')
def Contactenos():
    return render_template('Contactenos.html')
 
@app.route('/Quienessomos')
def Quienessomos():
    return render_template('Quienessomos.html')
 
@app.route('/MisionVision')
def MisionVision():
    return render_template('MisionVision.html')
  
@app.route('/Portafolio')
def Portafolio():
    return render_template('Portafolio.html')
 
@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/login')
def login():
    return render_template('vista/login.html')
 
@app.route('/Registrar')
def Registrar():
    return render_template('vista/Registrar.html')

@app.route('/Recordar')
def Recordar():
    return render_template('vista/Recordar.html')

@app.route('/Usuario')
def Usuario():
    return render_template('vista/Admin/Usuario.html')

if __name__ == '__main__':
    app.run(debug=True)