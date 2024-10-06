import plotly.graph_objs as go
import plotly  # Certifique-se de importar o módulo plotly
import json
def dashboard(dias,  entradas, vendas):
    # Criando os gráficos de barra
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=dias,
        y=entradas,
        name='Entradas',
        marker_color='blue'
    ))

    fig.add_trace(go.Bar(
        x=dias,
        y=vendas,
        name='Vendas',
        marker_color='orange'
    ))

    fig.update_layout(
        title='Dados de Entrada e Venda - Agosto',
        xaxis_title='Dias',
        yaxis_title='Quantidade',
        barmode='group',
        width=700,   # Ajuste da largura do gráfico
        height=400 
    )

    # Converte o gráfico Plotly para JSON para renderizar na página HTML
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON