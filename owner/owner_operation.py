from flask import Flask
from flask import render_template
from flask import request, url_for, redirect, flash
import token_verification
import time
import token_reduction
import IoT_operation
import recorder_operation
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.debug = True

@app.route('/success/?<string:ID>', methods=['GET', 'POST'])
def success(ID):
    if request.method == 'POST':
        return redirect(url_for('use',ID = ID))
    return render_template('success.html')

@app.route('/fail', methods=['GET', 'POST'])
def fail():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('fail.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ID = request.form.get('ID')
        r = request.form.get('r')
        reduction_result = token_reduction.token_reduction(ID,r)
        if reduction_result == True:
            v_time1 = time.time()
            verification_result = token_verification.token_verification(ID)
            v_time2 = time.time()
            print("Verification time:" + str(v_time2-v_time1))
            if verification_result == True:
                return redirect(url_for('success',ID = ID))
            else:
                return redirect(url_for('fail'))
        else:
            return redirect(url_for('fail'))
    return render_template('index.html')

@app.route('/usage/?<string:ID>', methods=['GET', 'POST'])
def use(ID):
    if request.method == 'POST':
        if list(request.form)[0] == 'Trigger Press':
            IoT_operation.press_operation()
            recorder_operation.press_recorder(ID)
        if list(request.form)[0] == 'Trigger Down':
            IoT_operation.down_operation()
            recorder_operation.down_recorder(ID)
        if list(request.form)[0] == 'Trigger Up':
            IoT_operation.up_operation()
            recorder_operation.up_recorder(ID)
        if list(request.form)[0] == 'Read':
            iot_time1 = time.time()
            token = IoT_operation.humid_read_operation()
            iot_time2 = time.time()
            print(token)
            r_time1 = time.time()
            recorder_operation.humid_read_recorder(ID)
            r_time2 = time.time()
            print("iot operating time" + str(iot_time2-iot_time1))
            print("recoding time" + str(r_time2 - r_time1))
            return redirect(url_for('read',token = token,ID = ID))
        if list(request.form)[0] == 'Turn on':
            IoT_operation.humid_turnon_operation()
            recorder_operation.humid_turnon_recorder(ID)
        if list(request.form)[0] == 'Turn off':
            IoT_operation.humid_turnoff_operation()
            recorder_operation.humid_turnoff_recorder(ID)
        if list(request.form)[0] == 'auto':
            IoT_operation.humid_mode_operation('auto')
            recorder_operation.humid_setmode_recorder(ID,'auto')
        if list(request.form)[0] == '101':
            IoT_operation.humid_mode_operation('101')
            recorder_operation.humid_setmode_recorder(ID,r'34%')
        if list(request.form)[0] == '102':
            IoT_operation.humid_mode_operation('102')
            recorder_operation.humid_setmode_recorder(ID,r'66%')
        if list(request.form)[0] == '103':
            IoT_operation.humid_mode_operation('103')
            recorder_operation.humid_setmode_recorder(ID,r'100%')
    return render_template('use.html')

@app.route('/read/<ID>/<token>', methods=['GET', 'POST'])
def read(token,ID):
    if request.method == 'POST':
       return redirect(url_for('use',ID = ID))
    return render_template('read.html',token = token)

if __name__ == "__main__":
    app.run(host='163.221.216.107', port=8080,debug=True)
