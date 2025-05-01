from flask import Flask, render_template, jsonify, request, redirect, url_for
import subprocess

###app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

##@app.route('/')
##def index():
##    return render_template('reconocimiento.html')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index2')
def index2():
    return render_template('index2.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/reconocimiento')
def reconocimiento():
    return render_template('reconocimiento.html')
@app.route('/tiempoReal')
def tiempoReal():
    return render_template('tiempoReal.html')
@app.route('/estadisticas')
def estadisticas():
    return render_template('estadisticas.html')
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')
@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    
    try:
        # Ejecuta el script de Python
        subprocess.Popen(['python', 'reconocimientoEmociones.py'])
        return jsonify({'status': 'success', 'message': 'Script ejecutado'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/run_script1', methods=['POST'])
def run_script1():
    try:
        # Ejecuta el script de Python
        subprocess.Popen(['python', 'capturandoRostrosF.py'])
        return jsonify({'status': 'success', 'message': 'Script ejecutado'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
@app.route('/run_script2', methods=['POST'])
def run_script2():
    try:
        # Ejecuta el script de Python
        subprocess.Popen(['python', 'capturandoRostrosE.py'])
        return jsonify({'status': 'success', 'message': 'Script ejecutado'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
@app.route('/run_script3', methods=['POST'])
def run_script3():
    try:
        # Ejecuta el script de Python
        subprocess.Popen(['python', 'capturandoRostrosS.py'])
        return jsonify({'status': 'success', 'message': 'Script ejecutado'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
@app.route('/run_script4', methods=['POST'])
def run_script4():
    try:
        # Ejecuta el script de Python
        subprocess.Popen(['python', 'capturandoRostrosT.py'])
        return jsonify({'status': 'success', 'message': 'Script ejecutado'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
    
@app.route('/run_script5', methods=['POST'])
def run_script5():
    try:
        # Ejecuta el script de Python
        subprocess.Popen(['python', 'entrenando.py'])
        return jsonify({'status': 'success', 'message': 'Script ejecutado'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)