import PySimpleGUI as sg

OUTPUT_FILENAME = 'Selecione o arquivo que deseja criptografar!'

arquivo = sg.popup_get_file(
    '%s' % OUTPUT_FILENAME, title="Cripto Legal", background_color='blue', button_color='black', font='Courier 14 italic bold' )


def tradutor():
    i = 0
    while i < len(palavra_lista):
        letra = palavra_lista[i]
        if palavra_lista[i] == 'P':
            palavra_lista[i] = 'M'
        elif palavra_lista[i] == 'I':
            palavra_lista[i] = 'A'
        elif palavra_lista[i] == 'N':
            palavra_lista[i] = 'R'
        elif palavra_lista[i] == 'D':
            palavra_lista[i] = 'T'
        elif palavra_lista[i] == 'O':
            palavra_lista[i] = 'E'
        elif palavra_lista[i] == 'M':
            palavra_lista[i] = 'P'
        elif palavra_lista[i] == 'A':
            palavra_lista[i] = 'I'
        elif palavra_lista[i] == 'R':
            palavra_lista[i] = 'N'
        elif palavra_lista[i] == 'T':
            palavra_lista[i] = 'D'
        elif palavra_lista[i] == 'E':
            palavra_lista[i] = 'O'
        else:
            palavra_lista[i] = palavra_lista[i]
        i = i + 1
with open(arquivo, "r+") as palavra:
    palavra = palavra.read()
palavra = str(palavra)
palavra = palavra.upper()

palavra_lista = list(palavra)
tradutor()
palavra_nova = "".join(palavra_lista)
palavra_nova = palavra_nova.capitalize()
with open(arquivo, "w") as palavra:
    palavra.write(palavra_nova)
