
def main():
    bearingToStation = random.randint(0,360)
    outboundCourse = random.randint(0,360)
    holding = random.choice('Estandar', 'No estandar')
    diferenciaAngular = bearingToStation - outboundCourse
    angulo70 = 70
    angulo110 = 110
    anguloCiego = 5
    if diferenciaAngular > angulo70 and holding == 'Estandar':
