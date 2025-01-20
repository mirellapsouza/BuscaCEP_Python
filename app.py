import requests

def main():
    cep = input('Informe o CEP: ')
    # tratamento
    cep = cep.replace('-', '').replace('.', '').replace(' ', '')

    if len(cep) == 8:
        requisicao = requests.get(f'https://viacep.com.br/ws/{cep}/json')
        dict_requisicao = requisicao.json()
        print(dict_requisicao['logradouro'], dict_requisicao['bairro'], dict_requisicao['uf'])
    else:
        print(f'CEP {cep} inválido... Tentar novamente? S/N')
        option = input()
        option = option.lower()
        if option == 'S':
            main()
        elif option == 'N':
            exit()
        else:
            print("?")
        
if __name__ == '__main__':
    main()