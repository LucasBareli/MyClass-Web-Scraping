import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Simulação de preços dos celulares
data = {
    'Celular': ['iPhone 15', 'iPhone 15', 'iPhone 15'],
    'Site': ['Magazine Luiza', 'Casas Bahia', 'Amazon'],
    'Preço': [2000, 2100, 2200]
}

# Criando um DataFrame
df = pd.DataFrame(data)

# Criando o app do Dash
app = dash.Dash(__name__)

# Layout do Dash
app.layout = html.Div([
    html.H1("Comparação de Preços do iPhone 15"),

    # Dropdown para escolher o produto
    dcc.Dropdown(
        id='produto-dropdown',
        options=[{'label': 'iPhone 15', 'value': 'iPhone 15'}],
        value='iPhone 15',
        style={'width': '50%'}
    ),

    # Gráfico de barras para comparar preços
    dcc.Graph(id='grafico-precos'),

    # Tabela para mostrar detalhes
    html.Div([
        html.H4('Tabela de Preços'),
        html.Div(id='tabela-precos')
    ])
])

# Função para atualizar o gráfico e a tabela
@app.callback(
    [dash.dependencies.Output('grafico-precos', 'figure'),
     dash.dependencies.Output('tabela-precos', 'children')],
    [dash.dependencies.Input('produto-dropdown', 'value')]
)
def atualizar_comparacao(produto):
    # Filtrando os dados com base no produto escolhido
    dados_filtrados = df[df['Celular'] == produto]

    # Criando o gráfico de barras
    fig = px.bar(dados_filtrados, x='Site', y='Preço', 
                 title=f'Comparação de Preços do {produto}', 
                 labels={'Preço': 'Preço em R$', 'Site': 'Loja'})

    # Criando a tabela
    tabela = html.Table([
        html.Thead(html.Tr([html.Th('Site'), html.Th('Preço (R$)')])),
        html.Tbody([
            html.Tr([html.Td(row['Site']), html.Td(f"R$ {row['Preço']:.2f}")]) 
            for _, row in dados_filtrados.iterrows()
        ])
    ])

    return fig, tabela

# Rodando o app
if __name__ == '__main__':
    app.run_server(debug=True)
