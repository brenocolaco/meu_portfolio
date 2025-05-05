from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)

# Coordenadas dos vértices do quadrado
x, y = 100, 100
lado = 50

# Criando uma lista de pontos para a polilinha
pontos = [
    APoint(x, y),
    APoint(x+lado, y),
    APoint(x+lado, y+lado),
    APoint(x, y+lado),
    APoint(x, y)  # Fecha a polilinha
]

# Adicionando a polilinha ao desenho
quadrado = acad.model.add_lwpolyline(pontos, close=True)