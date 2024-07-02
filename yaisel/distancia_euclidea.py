import numpy as np

def distancia_euclidiana(vector1, vector2):
    return np.sqrt(np.sum((np.array(vector1) - np.array(vector2))**2))
def determinar_clase(vector, dataset):
    distancias = []
    for dato in dataset:
        clase = dato[0]
        caracteristicas = dato[1:]
        dist = distancia_euclidiana(vector, caracteristicas)
        distancias.append((dist, clase))
    
    distancias.sort(key=lambda x: x[0])
    return distancias[0][1]