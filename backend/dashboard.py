import pandas as pd
import plotly.graph_objects as go
import requests
import plotly.offline as pyo
from datetime import datetime

def unir_dados(dados_entrada, dados_venda):
    df_entrada = pd.DataFrame(dados_entrada).groupby("nome_produto")["quantidade_entrada"].sum().reset_index()
    df_venda = pd.DataFrame(dados_venda).groupby("nome_produto")["quantidade_vendida"].sum().reset_index()
    
    df = pd.merge(df_entrada, df_venda, on="nome_produto", how="outer").fillna(0)
    
    return df

def criarDashboardLucro():
    labels = ['Categoria A', 'Categoria B', 'Categoria C']
    values = [30, 50, 20]

    pie_data = [go.Pie(labels=labels, values=values, textinfo='label+percent')]
    pie_layout = go.Layout(
        plot_bgcolor='rgba(0,0,0,0)',  
        paper_bgcolor='rgba(0,0,0,0)',  
        margin=dict(l=0, r=0, t=40, b=0)  
    )
    pie_fig = go.Figure(data=pie_data, layout=pie_layout)

    return pyo.plot(pie_fig, include_plotlyjs=False, output_type='div')
    

def calcularLucro(dados_entrada, dados_venda, produtos):
    lucro_total = 0
    lucro_categoria = {}

    for venda in dados_venda:
        id_produto = venda['id_produto']
        quantidade_vendida = venda['quantidade_vendida']
        
        preco_venda = produtos[id_produto]['preco']
        
        entradas_produto = [entrada for entrada in dados_entrada if entrada['id_produto'] == id_produto]
        custo_total = 0
        quantidade_faltante = quantidade_vendida
        
        for entrada in entradas_produto:
            if quantidade_faltante <= 0:
                break
            if entrada['quantidade_entrada'] <= quantidade_faltante:
                custo_total += entrada['preco'] * entrada['quantidade_entrada']
                quantidade_faltante -= entrada['quantidade_entrada']
            else:
                custo_total += entrada['preco'] * quantidade_faltante
                quantidade_faltante = 0
        
        receita_total = preco_venda * quantidade_vendida
        lucro = receita_total - custo_total
        lucro_total += lucro
        
        tipo_produto = produtos[id_produto]['tipo_produto']
        if tipo_produto not in lucro_categoria:
            lucro_categoria[tipo_produto] = 0
        lucro_categoria[tipo_produto] += lucro

    porcentagem_categoria = {categoria: (lucro / lucro_total) * 100 for categoria, lucro in lucro_categoria.items()}
    return porcentagem_categoria


def  criar_dashboard(df_relacao):
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_relacao["nome_produto"],
        y=df_relacao["quantidade_entrada"],
        name="Entrada",
        marker_color='dark blue'
    ))

    fig.add_trace(go.Bar(
        x=df_relacao["nome_produto"],
        y=df_relacao["quantidade_vendida"],
        name="Venda",
        marker_color='pink'

    ))
    mes  = 'SETEMBRO'
    fig.update_layout(
        xaxis_title="Produto",
        yaxis_title="Quantidade (Unidade)",
        barmode='group',  
        bargap=0.2,  #
        bargroupgap=0.1,  
        width=800,
        plot_bgcolor='rgba(0,0,0,0)',  
        paper_bgcolor='rgba(0,0,0,0)',  
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
   
    graph = fig.to_html(full_html=False)
    return graph

def filtrarDados(response, data, tipo):
    filtered_data = [item for item in response['data'] if item[f'data_{tipo}'].startswith(data)]
    if filtered_data:
        return filtered_data
    return 1

def pegarDataAtual():
    response = requests.get('http://worldtimeapi.org/api/timezone/Etc/UTC')
    data = response.json()
    current_time = data['datetime']
    data_atual = str(current_time)
    dt = datetime.fromisoformat(data_atual)
    data = dt.date()
    dataN = str(data)
    return dataN[:7]