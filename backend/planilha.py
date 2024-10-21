import pandas as pd
import io

def criar_planilhas_por_mes(dados_vendas, dados_produtos):
    precos_produtos = {produto["id"]: produto["preco"] for produto in dados_produtos["data"]}
    
    meses = {}

    for venda in dados_vendas["data"]:
        mes = pd.to_datetime(venda["data_venda"]).strftime('%B-%Y')

        preco_produto = precos_produtos.get(venda["id_produto"], 0)
        total_venda = venda["quantidade_vendida"] * preco_produto
        venda["total_venda"] = total_venda

        if mes not in meses:
            meses[mes] = []
        meses[mes].append(venda)

    output = io.BytesIO()

    meses_portugues = {
        'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
        'April': 'Abril', 'May': 'Maio', 'June': 'Junho',
        'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro',
        'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'
    }

    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        for mes, vendas in meses.items():

            df = pd.DataFrame(vendas)

            df.rename(columns={
                'data_venda': 'Data da Venda',
                'quantidade_vendida': 'Quantidade Vendida',
                'nome_produto': 'Produto',
                'nome_vendedor': 'Vendedor',
                'total_venda': 'Total (R$)'
            }, inplace=True)

            df.drop(columns=["id_produto", "id_vendedor"], inplace=True)

            df['Data da Venda'] = pd.to_datetime(df['Data da Venda']).dt.strftime('%d/%m/%Y')

            mes_portugues = meses_portugues[pd.to_datetime(vendas[0]["data_venda"]).strftime('%B')]
            nome_planilha = f"{mes_portugues}-{pd.to_datetime(vendas[0]['data_venda']).strftime('%Y')}"

            df.to_excel(writer, sheet_name=nome_planilha, index=False)

            total_arrecadado = df['Total (R$)'].sum()

            workbook = writer.book
            worksheet = writer.sheets[nome_planilha]

            format_rosa = workbook.add_format({'bg_color': '#FFC0CB'})  

            row_total = len(df) + 1  
            worksheet.write(row_total, 5, total_arrecadado, format_rosa) 

    output.seek(0)

    return output
