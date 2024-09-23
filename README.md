# Atualização de Geometria de Pontos no QGIS

Este script em Python é desenvolvido para uso no ambiente do QGIS, utilizando a API PyQGIS. O objetivo do script é atualizar a geometria dos pontos de uma camada específica com base nos valores dos campos X e Y da camada.

## Pré-requisitos

- QGIS instalado (versão compatível com PyQGIS).
- Camada de pontos com os campos `X` e `Y`, que representam as coordenadas dos pontos a serem atualizadas.

## Como o Script Funciona

1. **Definição da camada**: O script procura por uma camada chamada `vertices_tst`. É importante que a camada esteja carregada no projeto do QGIS com este nome exato.

2. **Início da edição**: O script coloca a camada em modo de edição para permitir as alterações nas geometrias dos pontos.

3. **Atualização das geometrias**:
   - O script identifica os índices dos campos `X` e `Y`.
   - Para cada ponto (feature) na camada, ele obtém os valores dos campos `X` e `Y`, cria um novo ponto com essas coordenadas e atualiza a geometria da feature.

4. **Salvar alterações**: Após atualizar todas as geometrias, o script salva as alterações feitas na camada.

## Código

```python
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
```

## Considerações

- Verifique se a camada de pontos está carregada corretamente no projeto do QGIS com o nome especificado (`vertices_tst`).
- Os campos `X` e `Y` devem estar presentes na camada e conter coordenadas válidas.
- Sempre faça backup dos dados antes de executar scripts que alteram geometrias.

## Autor

Este script foi desenvolvido para facilitar a atualização de geometrias de pontos no QGIS de forma automatizada e eficiente.
