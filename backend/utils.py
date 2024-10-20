def formatMoney(objeto):
    for produto in objeto:
        produto['preco'] = f"{produto['preco']:.2f}".replace(',', '.')
    return objeto

def formatDate(objeto, type):
    for dates  in objeto:
        data_entrada = dates[f'data_{type}']
        dates[f'data_{type}'] =  f"{data_entrada[8:10]}/{data_entrada[5:7]}/{data_entrada[0:4]}"
    return objeto
    