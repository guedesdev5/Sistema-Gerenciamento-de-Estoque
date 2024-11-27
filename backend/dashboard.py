import pandas as pd
import plotly.graph_objects as go
import requests
import plotly.offline as pyo
from datetime import datetime, timedelta

data_cache = None
ultima_atualizacao = None

def getStringMes(date):
    mes = int(date.split('-')[1])
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", 
        "Maio", "Junho", "Julho", "Agosto", 
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    if 1 <= mes <= 12:
        return meses[mes - 1]
    else:
        return "Número do mês inválido"

def unir_dados(dados_entrada, dados_venda):
    df_entrada = pd.DataFrame(dados_entrada).groupby("nome_produto")["quantidade_entrada"].sum().reset_index()
    df_venda = pd.DataFrame(dados_venda).groupby("nome_produto")["quantidade_vendida"].sum().reset_index()
    
    df = pd.merge(df_entrada, df_venda, on="nome_produto", how="outer").fillna(0)
    
    return df

def calcularLucro(dados_entrada, dados_venda, produtos, categorias):
    gastoEntrada = 0
    for valorEntrada in dados_entrada:
        gastoEntrada += int(valorEntrada['preco'])
        
    ganhoVenda = 0
    for valorVenda in dados_venda:
        for idProduto in produtos['data']:
            if (int(valorVenda['id_produto']) == int(idProduto['id'])):
                ganhoVenda += int(valorVenda['quantidade_vendida']) * int(idProduto['preco'])

    lucroCategorias = {}
    for categoria in categorias['data']:
        if categoria['nome'] not in lucroCategorias:
            lucroCategorias[categoria['nome']] = 0
        for idProduto in produtos['data']:
            for valorVenda in dados_venda:
                if(categoria['nome'] == idProduto['tipo_produto'] and idProduto['nome'] == valorVenda['nome_produto']):
                    lucroCategorias[categoria['nome']] += int(valorVenda['quantidade_vendida']) * int(idProduto['preco'])

    pocentagemcategoria = {}
    for valorCategorias in lucroCategorias.keys():
        lucroCategorias[valorCategorias] = (lucroCategorias[valorCategorias]/ganhoVenda) * 100

    return lucroCategorias

def filtrarDados(response, data, tipo):
    filtered_data = [item for item in response['data'] if item[f'data_{tipo}'].startswith(data)]
    if filtered_data:
        return filtered_data
    response['data'][0]['erro'] =1
    return response['data']

def pegarDataAtual():
    data_atual = datetime.utcnow().date()  # Usa UTC
    return str(data_atual)[:7]


def criarDashboardLucro(labels, values):
    pie_data = [go.Pie(labels=labels, values=values, textinfo='label+percent', textfont=dict(size=18) )]
    pie_layout = go.Layout(
        plot_bgcolor='rgba(0,0,0,0)',  
        paper_bgcolor='rgba(0,0,0,0)',  
        margin=dict(l=0, r=0, t=40, b=0),
        legend=dict(font=dict(size=20))
    )
    pie_fig = go.Figure(data=pie_data, layout=pie_layout)

    return pyo.plot(pie_fig, include_plotlyjs=False, output_type='div')

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
        margin=dict(l=0, r=0, t=0, b=0),
        font=dict(size=18),  
        legend=dict(font=dict(size=20))     )
    
   
    graph = fig.to_html(full_html=False)
    return graph