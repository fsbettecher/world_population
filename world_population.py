# Importando as bibliotecas necessárias
import pandas as pd
import kaggle

# Autenticando no Kaggle
kaggle.api.authenticate()

# Baixando os dados do dataset que será utilizado
dataset_path = 'whenamancodes/world-population-live-dataset'

kaggle.api.dataset_download_files(dataset_path, path='./portfolio/', unzip=True)

# Criando um DataFrame a partir do arquivo baixado
dataset = pd.read_csv('./portfolio/World Population Live Dataset.csv')

# Renomeando as colunas do DataFrame
dataset.rename(columns={'CCA3': 'codigo_pais', 'Name': 'nome_pais',
                        'Area (km²)': 'area', 'Density (per km²)': 'densidade',
                        'GrowthRate': 'taxa_crescimento',
                        'World Population Percentage': 'porcentagem_populacional',
                        'Rank': 'rank'}, inplace=True)

# Alterando os dados de anos de colunas para linhas
dataset = pd.melt(dataset, id_vars=['codigo_pais', 'nome_pais', 'area', 'densidade',
                                    'taxa_crescimento', 'porcentagem_populacional', 'rank'],
                                    value_vars=['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970'],
                                    value_name='populacao', var_name='ano')

# Gerando um arquivo csv com o DataFrame tratado
dataset.to_csv('./portfolio/Populacao_mundial.csv')