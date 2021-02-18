import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    numpyArray = np.array([[list[0:3]], [list[3:6]], [list[6:10]]])
    flattened = np.array([list])

    media = []
    media2 = []
    media.append(np.mean(numpyArray, axis=0).tolist()[0])
    for x in np.mean(numpyArray, axis=2).tolist():
        media2.append(x[0])
    media.append(media2)
    media.append(flattened.mean().tolist())

    varianza = []
    varianza2 = []
    varianza.append(np.var(numpyArray, axis=0).tolist()[0])
    for x in np.var(numpyArray, axis=2).tolist():
        varianza2.append(x[0])
    varianza.append(varianza2)
    varianza.append(flattened.var().tolist())

    stand = []
    stand2 = []
    stand.append(np.std(numpyArray, axis=0).tolist()[0])
    for x in np.std(numpyArray, axis=2).tolist():
        stand2.append(x[0])
    stand.append(stand2)
    stand.append(flattened.std().tolist())

    maximo = []
    maximo2 = []
    maximo.append(np.max(numpyArray, axis=0).tolist()[0])
    for x in np.max(numpyArray, axis=2).tolist():
        maximo2.append(x[0])
    maximo.append(maximo2)
    maximo.append(flattened.max().tolist())

    minimo = []
    minimo2 = []
    minimo.append(np.min(numpyArray, axis=0).tolist()[0])
    for x in np.min(numpyArray, axis=2).tolist():
        minimo2.append(x[0])
    minimo.append(minimo2)
    minimo.append(flattened.min().tolist())

    suma = []
    suma2 = []
    suma.append(np.sum(numpyArray, axis=0).tolist()[0])
    for x in np.sum(numpyArray, axis=2).tolist():
        suma2.append(x[0])
    suma.append(suma2)
    suma.append(flattened.sum().tolist())

    diccionario = {
        'mean': media,
        'variance': varianza,
        'standard deviation': stand,
        'max': maximo,
        'min': minimo,
        'sum': suma
    }
    return diccionario
