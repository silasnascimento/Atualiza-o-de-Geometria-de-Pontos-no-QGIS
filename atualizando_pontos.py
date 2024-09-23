from qgis.core import QgsProject, QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY

# Definir o nome da camada de pontos
nome_camada = 'vertices_tst'

# Obter a camada de pontos
camada_pontos = QgsProject.instance().mapLayersByName(nome_camada)[0]

# Iniciar edição
camada_pontos.startEditing()

# Obter o índice dos campos X e Y
indice_x = camada_pontos.fields().indexFromName('X')
indice_y = camada_pontos.fields().indexFromName('Y')

# Iterar sobre as features
for feature in camada_pontos.getFeatures():
    # Obter os valores de X e Y
    novo_x = feature.attributes()[indice_x]
    novo_y = feature.attributes()[indice_y]
    
    # Criar um novo ponto com as coordenadas atualizadas
    novo_ponto = QgsPointXY(float(novo_x), float(novo_y))
    
    # Atualizar a geometria da feature
    feature.setGeometry(QgsGeometry.fromPointXY(novo_ponto))
    
    # Salvar as mudanças na camada
    camada_pontos.updateFeature(feature)

# Finalizar edição e salvar
camada_pontos.commitChanges()
