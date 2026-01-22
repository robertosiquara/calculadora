import flet as ft
from decimal import getcontext

getcontext().prec = 10

def main(page: ft.Page):
    page.title = 'RS Calculadora'
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLACK
    page.window.height = 620
    page.window.width = 420
    page.window.resizable = False
    page.padding = 20
    page.window.icon= "calculadora_icon.ico"
    
    # --- Lógica de Funções ---
    def number_click(e):
        valor_botao = e.control.data
        if display.value == '0' or display.value == 'Error':
            display.value = '0,' if valor_botao == ',' else valor_botao
        elif valor_botao == ",":
            partes = display.value.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()
            ultimo_numero = partes[-1] if partes else ""
            if ',' in ultimo_numero: return
            display.value += '0,' if display.value[-1] in "+-*/" else ','
        else:
            display.value += valor_botao
        display.update()

    def operator_click(e):
        btn = e.control.data
        if display.value == 'Error': display.value = '0'
        if display.value[-1] in '+-*/':
            display.value = display.value[:-1] + btn
        else:
            if any(op in display.value[1:] for op in "+-*/"):
                calculate_click(None)
            display.value += btn
        display.update()

    def calculate_click(e):
        try:
            if display.value[-1] in '+-*/': return
            expressao = display.value.replace(',', '.')
            resultado_num = eval(expressao)
            resultado_str = format(resultado_num, '.10g')
            display.value = resultado_str.replace('.', ',')
        except:
            display.value = 'Error'
        display.update()

    def clear(e):
        display.value = '0'
        display.update()

    # --- UI COMPONENTS ---
    
    display = ft.TextField(color= ft.Colors.WHITE,value= "0",text_size=40, border_color=ft.Colors.RED_500, border_width=1, text_align= ft.TextAlign.RIGHT, width= 320,  height= 100, border_radius= ft.border_radius.all(5),read_only=False)

    # Função para criar botões sofisticados
    def create_button(text, color=ft.Colors.RED_500, text_color=ft.Colors.BLACK, width=65, action=None):
        return ft.Container(
            content=ft.Text(text, size=22, weight=ft.FontWeight.BOLD, color=text_color),
            # ALINHAMENTO CORRIGIDO: (0, 0) é Center
            alignment=ft.Alignment(0, 0),
            bgcolor=color,
            width=width,
            height=65,
            border_radius=15,
            ink=True,
            on_click=action,
            data=text,
        )

    # Organização das Linhas
    buttons_layout = ft.Column(
        spacing=12,
        controls=[
            ft.Row(
                spacing=12,
                controls=[
                    create_button('C', ft.Colors.RED_900, ft.Colors.WHITE, 219, clear),
                    create_button('/', ft.Colors.RED_700, ft.Colors.WHITE, 65, operator_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                spacing=12,
                controls=[
                    create_button('7', action=number_click),
                    create_button('8', action=number_click),
                    create_button('9', action=number_click),
                    create_button('*', ft.Colors.RED_700, ft.Colors.WHITE, 65, operator_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                spacing=12,
                controls=[
                    create_button('4', action=number_click),
                    create_button('5', action=number_click),
                    create_button('6', action=number_click),
                    create_button('-', ft.Colors.RED_700, ft.Colors.WHITE, 65, operator_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                spacing=12,
                controls=[
                    create_button('1', action=number_click),
                    create_button('2', action=number_click),
                    create_button('3', action=number_click),
                    create_button('+', ft.Colors.RED_700, ft.Colors.WHITE, 65, operator_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                spacing=12,
                controls=[
                    create_button('0', action=number_click),
                    create_button(',', action=number_click),
                    create_button('=', ft.Colors.WHITE, ft.Colors.RED_900, 142, calculate_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ]
    )

    footer = ft.Text(
        "Desenvolvido por: Roberto Lobo Siquara",
        color=ft.Colors.GREY_700,
        size=10,
        italic=True
    )

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                display,
                ft.Container(height=10),
                buttons_layout,
                ft.Container(height=10),
                footer
            ]
        )
    )

if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")