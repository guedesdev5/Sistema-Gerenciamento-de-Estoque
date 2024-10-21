def formatMoney(objeto):
    for produto in objeto:
        produto['preco'] = f"{produto['preco']:.2f}".replace(',', '.')
    return objeto

def formatDate(objeto, type):
    for dates in objeto:
        data_entrada = dates[f'data_{type}']
        dates[f'data_{type}'] =  f"{data_entrada[8:10]}/{data_entrada[5:7]}/{data_entrada[0:4]}"
    return objeto

def formatTelefone(objeto):
    def formatar_telefone(telefone):
        if len(telefone) == 11:
            return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        return telefone 

    for contato in objeto['data']:
        contato['telefone'] = formatar_telefone(contato['telefone'])

    return objeto