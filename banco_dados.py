import sqlite3

from agenda_nova_smith import Contato


def cria_db():
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE contatos(
        id INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT);""")

    print('Banco e Tabela criados com sucesso')

    conn.close()

def SalvaContato(contato):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    lista = [(contato.vnome, contato.vtelefone, contato.vemail)]

    if contato.vid_contato:
        cursor.execute("""
        UPDATE contatos
        SET nome = ?, telefone = ?
        WHERE id = ?""", (contato.vnome,
        contato.vtelefone, contato.vid_contato))

    else:
        cursor.executemany("""
        INSERT INTO contatos(nome, telefone, 
        email) VALUES (?, ?, ?)""", lista)

        conn.commit()

        print('Dados Salvos com sucesso!')

        conn.close()

def BuscarContato():
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    contatos = []

    cursor.execute("""
    SELECT id, nome, email, telefone FROM 
    contatos""")

    for linha in cursor.fetchall():
        contatos.append(Contato(vid_contato=linha[0], vnome=linha[1], vemail=linha[2], vtelefone=linha[3]))

    conn.commit()
    conn.close()

    return contatos

def BuscarNome(nome):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    contatos = []

    cursor.execute("""
    SELECT id, nome, email, telefone FROM 
    contatos WHERE nome = ?""", [nome])

    for linha in cursor.fetchall():
        contatos.append(Contato(vid_contato=linha[0], vnome=linha[1], vemail=linha[2], vtelefone=linha[3]))

    conn.commit()
    conn.close()

    return contatos

def BuscarEmail(email):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, nome, email, telefone FROM 
    contatos WHERE email = ?""", [email])

    contato = None

    for linha in cursor.fetchall():
        contato = [Contato(vid_contato=linha[0], vnome=linha[1], vemail=linha[2], vtelefone=linha[3])]

    conn.commit()
    conn.close()

    return contato

def DeletarEmail(email):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    cursor.execute("DELETE FROM contatos WHERE email = ?", [email])

    conn.commit()
    conn.close()

def AtualizarContato(vemail):
    conn = sqlite3.connect('agenda.db')

    cursor = conn.cursor()

    vnome = input('Digite o nome: ')
    vtelefone = input('Digite o telefone: ')

    cursor.execute("""
    UPDATE contatos
    SET nome = ?, telefone = ?
    WHERE email == ?""", ([vnome,
    vtelefone, vemail]))

    conn.commit()
    conn.close()
