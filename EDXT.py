import PySimpleGUI as sg 

WIN_W = 90
WIN_H = 25


menu = [["Arquivo", ['Novo', 'Abrir', 'Salvar']],
        ["Editar", ['Tornar Caixa Alta', 'Tornar Caixa Baixa', 'Inverter']],
        ["Mais", ['Editar Tema']],
        ["Sobre...", ["Criado Por"]]]


def inici(t='', tem='BlueMono'):
    sg.theme(tem)
    global temas
    temas = tem
    layout = [[sg.Menu(menu)],
    [sg.Multiline((t), size=(WIN_W, WIN_H), key='texto')],
    

    ]
    return sg.Window('Editar Texto', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)


def tema(tu, teme):
    sg.theme(tu)
    layout = [[sg.Text('Escolha um tema na lista abaixo')],
    [sg.Listbox(values=sg.theme_list(), size=(20, 10), key='list', enable_events=True), sg.Text(f'O tema padrão é Reddit. O seu tema atual é {teme} ')],
    [sg.Text(size=(20, 1), key='alert')],
    [sg.Button('Confirmar')]
    ]

    return sg.Window('Escolha o tema', layout=layout, finalize=True)




def salvar():
    if filename not in (None, ""):
        with open(filename, "w") as f:
            f.write(values.get("_BODY_"))
    else:
        save_file_as()


def save_file_as() -> str:
    try:
        filename: str = sg.popup_get_file(
            "Save File",
            save_as=True,
            no_window=True,
            default_extension=".txt",
            file_types=(("Text", ".txt"),),
        )
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "w") as f:
            f.write(values.get("texto"))
    return filename

def novo():
    window['texto'].update('')
    filename = None
    return filename


def abrir():
    try:
        filename: str = sg.popup_get_file("Open File", no_window=True)
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        try:
            with open(filename, "r") as f:
                window["texto"].update(value=f.read())
        except:
            sg.popup('Arquivo inválido.')
            abrir()
    return filename


janela1, janela2 = inici(None, 'BlueMono'), None
janela1.read(timeout=1)
janela1["texto"].expand(expand_x=True, expand_y=True)

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        janela1.close()
        break
    if window == janela1 and event == "Criado Por":
        sg.popup('Notepad Arpa, Criado por Arpanet_01')
    if window == janela1 and event == "Editar Tema":
        text = values['texto']
        janela1.close()
        janela2 = tema(temas, temas)
    if window == janela1 and event == "Tornar Caixa Alta":
        text = values['texto']
        window['texto'].update(text.upper())
    if window == janela1 and event == "Tornar Caixa Baixa":
        text = values['texto']
        window['texto'].update(text.lower())
    if window == janela1 and event == "Inverter":
        text = values['texto']
        window['texto'].update(text.swapcase())
    if window == janela2 and event == sg.WIN_CLOSED:
        janela2.close()
        janela1 = inici(text, temas)
    if window == janela2 and event == "Confirmar":
        lista = values['list']
        if len(lista) < 1:
            window['alert'].update('ESCOLHA UM TEMA')
        else:
            temav = lista[0]
            window.close()
            janela1 = inici(text, lista[0])
            janela1.read(timeout=1)
            janela1["texto"].expand(expand_x=True, expand_y=True)
    if window == janela1 and event == "Novo":
        novo()
    if window == janela1 and event == "Salvar":
        save_file_as()
    if window == janela1 and event == 'Abrir':
        abrir()


        





