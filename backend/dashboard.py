import plotly
import plotly.graph_objs as go
import json

def create_plot(vendas, entradas, mes):
    # Gráfico de Vendas (Barras)
    vendas_trace = go.Bar(
        x=vendas['meses'],
        y=vendas['valores'],
        name=f'Vendas Mẽs de {mes}',
        marker=dict(color='rgb(55, 83, 109)')
    )

    # Gráfico de Entradas (Linhas)
    entradas_trace = go.Scatter(
        x=entradas['meses'],
        y=entradas['valores'],
        mode='lines+markers',
        name=f'Entradas mês de {mes}',
        line=dict(color='rgb(26, 118, 255)', width=4)
    )

    data = [vendas_trace, entradas_trace]

    # Layout dos gráficos
    layout = go.Layout(
        title='Dashboard de Vendas e Entradas',
        xaxis=dict(title='Meses'),
        yaxis=dict(title='Valores em R$'),
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)

    # Converte o gráfico Plotly para JSON para renderizar na página HTML
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
