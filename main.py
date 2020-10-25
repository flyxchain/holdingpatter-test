from flask import Flask, render_template, json, request, flash
import random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    bearingToStation = random.randint(0, 360)
    inboundCourse = random.randint(0, 360)
    if (inboundCourse > 180):
        outboundCourse = inboundCourse - 180
    else:
        outboundCourse = inboundCourse + 180
        
    holdingTypes = ('Estandar' , 'No estandar')
    holding = random.choice(holdingTypes)

    if (bearingToStation + 70) > 360: 
        relativebearingplus70 = bearingToStation + 70 - 360
    else:
        relativebearingplus70 =  bearingToStation + 70

    if (bearingToStation + 10) > 360: 
        relativebearingplus10 = bearingToStation + 10 - 360
    else:
        relativebearingplus10 =  bearingToStation + 10

    if (bearingToStation + 110) > 360: 
        relativebearigplus110 = bearingToStation + 110 - 360
    else:
        relativebearigplus110 =  bearingToStation + 110

    if (bearingToStation - 70) > 360: 
        relativebearingminus70 = bearingToStation - 70 - 360
    else:
        relativebearingminus70 =  bearingToStation - 70

    if (bearingToStation - 10) > 360: 
        relativebearingminus10 = bearingToStation - 10 - 360
    else:
        relativebearingminus10 =  bearingToStation - 10

    if (bearingToStation - 110) > 360: 
        relativebearingminus110 = bearingToStation - 110 - 360
    else:
        relativebearingminus110 =  bearingToStation - 110

    # Definimos el patrón de entrada en función del holding el curso de outbound y el bearing relativo
    if outboundCourse > (relativebearingplus10) and outboundCourse < (relativebearingplus70) and holding == "Estandar":
        offsetHolding = True
        directHolding = False
        parallelHolding = False
        # print("La entrada es en gota")
    elif outboundCourse < (relativebearingminus10) and outboundCourse > (relativebearingminus110) and holding == "Estandar":
        offsetHolding = False
        directHolding = False
        parallelHolding = True
        # print("La entrada es paralela")
    elif outboundCourse > (relativebearingplus10) and outboundCourse < (relativebearigplus110) and holding == "No Estandar":
        offsetHolding = False
        directHolding = False
        parallelHolding = True
        # print("La entrada es paralela")
    elif outboundCourse < (relativebearingminus10) and outboundCourse > (relativebearingminus70) and holding == "No Estandar":
        offsetHolding = True
        directHolding = False
        parallelHolding = False
        # print("La entrada es en gota")
    elif outboundCourse > (relativebearingminus10) and outboundCourse < (relativebearingplus10):
        offsetHolding = True
        directHolding = False
        parallelHolding = True
        # print("La entrada es en gota o paralela")
    elif outboundCourse > (relativebearigplus110) and outboundCourse < (relativebearingminus70) and holding == "No Estandar":
        offsetHolding = False
        directHolding = True
        parallelHolding = False
        # print("La entrada es directa")
    else: 
        offsetHolding = False
        directHolding = True
        parallelHolding = False
        # print("La entrada es directa")

    if request.method == 'POST':
        valorseleccionado = request.form.get('holdingValueSelected')
        if valorseleccionado == "offsetHolding" and offsetHolding == True:
            return render_template('correcta.html', bearing = bearingToStation, realholding = holding, course = outboundCourse)
        elif valorseleccionado == "directHolding" and directHolding == True:
            return render_template('correcta.html', bearing = bearingToStation, realholding = holding, course = outboundCourse)
        elif valorseleccionado == "parallelHolding" and parallelHolding == True:
            return render_template('correcta.html', bearing = bearingToStation, realholding = holding, course = outboundCourse)
        else:
            return render_template('incorrecta.html', bearing = bearingToStation, realholding = holding, course = outboundCourse)
    return render_template('index.html', bearing = bearingToStation, realholding = holding, course = outboundCourse)
