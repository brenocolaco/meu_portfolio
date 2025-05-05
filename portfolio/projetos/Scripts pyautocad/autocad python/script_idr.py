import pyautocad

# Conectar ao AutoCAD
acad = pyautocad.Autocad()

# Definir as dimensões e posições (ajustar conforme a sua imagem)
largura_caixa = 100
altura_caixa = 50
raio_canto = 10
x_centro = 100
y_centro = 100
raio_botao = 15
espessura_texto = 2

# Criar a caixa principal
rect = acad.model.add_rectangle(x_centro-largura_caixa/2, y_centro-altura_caixa/2, largura_caixa, altura_caixa)
acad.model.fillet(rect, raio_canto)

# Criar o botão
circulo_botao = acad.model.add_circle(x_centro-largura_caixa/4, y_centro-altura_caixa/2+raio_botao, raio_botao)

# Adicionar texto
texto_sdr = acad.model.add_text("SDR", x_centro-largura_caixa/2+10, y_centro+10, height=5)
# ... adicionar outros textos

# Criar terminais (ajustar as coordenadas conforme a imagem)
linha1 = acad.model.add_line(x_centro-largura_caixa/2, y_centro, x_centro-largura_caixa/2-20, y_centro)
# ... adicionar outras linhas

# Criar um bloco (opcional)
acad.model.block(name="disjuntor", base_point=(x_centro, y_centro), objects=[rect, circulo_botao, texto_sdr, linha1])