from prettytable import PrettyTable

import requests

from banco_dados import SalvaContato, BuscarContato, BuscarNome, BuscarEmail, DeletarEmail, AtualizarContato

from agenda_nova_smith import Contato

contatos = []

def NovoContato():
    print(''' 
                ====================================
                | SEJA BEM VINDO AO MEU 1ª PROJETO |
                ====================================
                |      AGENDA SMITH EM PYTHON      |
                ====================================
                |        FELIZ 2022 A TODOS        | 
                ====================================
                ''')
    vnome = input('Digite o nome: ')
    vtelefone = input('Digite o telefone: ')
    vemail = input('Digite o email: ')

    contato = BuscarContatoEmail(vemail)

    if contato:
        print(f'O telefone {vemail} já está cadastrado.')
        return


    SalvaContato(Contato(vnome, vtelefone, vemail))

    ListaContato()

def ListaContato():
    print(''' 
            ====================================
            | SEJA BEM VINDO AO MEU 1ª PROJETO |
            ====================================
            |      AGENDA SMITH EM PYTHON      |
            ====================================
            |        FELIZ 2022 A TODOS        | 
            ====================================
            ''')
    table = PrettyTable(['Nome', 'Telefone','Email'])

    for contato in BuscarContato():
        table.add_row([contato.vnome, contato.vtelefone, contato.vemail])

    print(table)

def BuscarContatoNome(nome):
    table = PrettyTable(['Nome', 'Email', 'Telefone'])

    for contato in BuscarNome(nome):
        table.add_row([contato.vnome, contato.vemail, contato.vtelefone])

    print(table)

def BuscarContatoEmail(email):
    resultado = BuscarEmail(email)

    if not resultado:
        return

    return resultado

def AlterarContato(email):
    contato = BuscarContatoEmail(email)

    if not contato:
        print(f'Não existe nenhum contato com o email: {email}')
        return

    AtualizarContato(email)

    ListaContato()

def ExcluirContato(email):

    contato = BuscarContatoEmail(email)

    if not contato:
        print(f'Não existe nenhum contato com o email: {email}')
        return

    DeletarEmail(email)

    ListaContato()

def CarregaContato():
    response = requests.get("""
    https://randomuser.me/api""")

    if response.status_code != 200:
        print('Erro ao consumir o serviço de contatos.')
        return

    resultado = response.json()

    contato = Contato(vnome="{} {}".format(
    resultado['results'][0]['name']['first'],
    resultado['results'][0]['name']['last']),
    vemail=resultado['results'][0]['email'],
    vtelefone=resultado['results'][0]['phone'])

    SalvaContato(contato)

    ListaContato()

