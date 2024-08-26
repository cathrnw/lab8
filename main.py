from flask import Flask, render_template, request
import math
app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('home.html')

@app.route('/ctof')
def render_ctof():
    return render_template('ctof.html')

@app.route('/ctof_result')
def render_ctof_result():
    try:
        ctemp_result = float(request.args['ctemp'])
        ftemp_result = ctof(ctemp_result)
        return render_template('ctof_result.html', 
                               ctemp=ctemp_result, 
                               ftemp=ftemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/ftoc')
def render_ftoc():
    return render_template('ftoc.html')

@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['ftemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html',
                              ftemp=ftemp_result, 
                              ctemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."
    
@app.route('/mtokm')
def render_mtokm():
    return render_template('mtokm.html')

@app.route('/mtokm_result')
def render_mtokm_result():
    try:
        miles_result = float(request.args['miles'])
        kilo_result = mtokm(miles_result)
        return render_template('mtokm_result.html',
                              kilo=kilo_result, 
                              miles=miles_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/calcarea')
def render_calcarea():
    return render_template('calcarea.html')

@app.route('/calcarea_result')
def render_calcarea_result():
    try:
        radius_result = float(request.args['r'])
        area_result = calcarea(radius_result)
        return render_template('calcarea_result.html',
                              area=area_result, 
                              radius=radius_result)
    except ValueError:
        return "Sorry: something went wrong."
    
# ------------

def ftoc(ftemp):
   return (ftemp - 32.0) * (5.0 / 9.0)

@app.route('/ftoc/<ftemp_str>')
def convert_ftoc(ftemp_str):
    ftemp = 0.0
    try:
        ftemp = float(ftemp_str)
        ctemp = ftoc(ftemp)
        return "In Fahrenheit: " + ftemp_str + " In Celsius: " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftemp_str + " to a number"

def ctof(ctemp):
    return (ctemp * 9.0 / 5.0) + 32

@app.route('/ctof/<ctemp_str>')
def convert_ctof(ctemp_str):
    ctemp = 0.0
    try:
        ctemp = float(ctemp_str)
        ftemp = ctof(ctemp)
        return "In Celsius: " + ctemp_str + " In Fahrenheit: " + str(ftemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ctemp_str + " to a number"

def mtokm(miles):
    return (miles * 0.001)

@app.route('/mtokm/<mile_str>')
def convert_mtokm(mile_str):
    miles = 0.0
    try:
        miles = float(mile_str)
        kilo = mtokm(miles)
        return "In miles: " + mile_str + " In kilometers: " + str(kilo)
    except ValueError:
        return "Sorry. Could not convert " + mile_str + " to a number"

def cirarea(r):
    return (r ** 2) * (math.pi)

@app.route('/calcarea/<radius_str>')
def calcarea(radius_str):
    r = 0.0
    try:
        r = float(radius_str)
        area = cirarea(r)
        return "Radius: " + str(radius_str) + " Area: " + str(area)
    except ValueError:
        return "Sorry. Could not convert " + radius_str + " to a number"

if __name__ == "__main__":
    app.run(host='0.0.0.0')