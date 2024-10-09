import pandas as pd
import plotly.graph_objects as go

def unir_dados(dados_entrada, dados_venda):
    df_entrada = pd.DataFrame(dados_entrada).groupby("nome_produto")["quantidade_entrada"].sum().reset_index()
    df_venda = pd.DataFrame(dados_venda).groupby("nome_produto")["quantidade_vendida"].sum().reset_index()
    
    # Merge para juntar as quantidades de entrada e venda
    df = pd.merge(df_entrada, df_venda, on="nome_produto", how="outer").fillna(0)
    
    return df

def  criar_dashboard(df_relacao):
    fig = go.Figure()

    # Barras de entrada
    fig.add_trace(go.Bar(
        x=df_relacao["nome_produto"],
        y=df_relacao["quantidade_entrada"],
        name="Entrada",
        marker_color='dark blue'
    ))

    # Barras de venda
    fig.add_trace(go.Bar(
        x=df_relacao["nome_produto"],
        y=df_relacao["quantidade_vendida"],
        name="Venda",
        marker_color='pink'
    ))
    mes  = 'SETEMBRO'
    # Configurações do gráfico
    fig.update_layout(
        xaxis_title="Produto",
        yaxis_title="Quantidade (Unidade)",
        barmode='group',  # Para que as barras fiquem lado a lado
        bargap=0.2,  # Reduzir o espaço entre as barras
        bargroupgap=0.1,  # Reduzir o espaço entre os grupos de barras
        width=1500,
        plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    # Renderizar o template com o gráfico
    graph = fig.to_html(full_html=False)
    return graph