# RS Calculadora

## Descrição do Projeto

A **RS Calculadora** é uma aplicação de calculadora simples e funcional desenvolvida em Python utilizando o framework **Flet**. O objetivo do projeto é fornecer uma interface gráfica de usuário (GUI) limpa e intuitiva para a realização de operações aritméticas básicas.

## Funcionalidades

*   **Operações Básicas:** Adição (+), Subtração (-), Multiplicação (*) e Divisão (/).
*   **Interface Intuitiva:** Design moderno com esquema de cores em preto e vermelho, e botões responsivos.
*   **Ponto Decimal:** Suporte para números decimais, utilizando a vírgula (`,`) como separador decimal, conforme o padrão brasileiro.
*   **Limpeza:** Botão 'C' para limpar o display e reiniciar a operação.
*   **Tratamento de Erros:** Exibe 'Error' para expressões inválidas ou divisão por zero.
*   **Precisão:** Configuração de precisão decimal para 10 dígitos, garantindo cálculos mais exatos.

## Tecnologias Utilizadas

O projeto foi desenvolvido com as seguintes tecnologias:

| Tecnologia | Propósito |
| :--- | :--- |
| **Python** | Linguagem de programação principal. |
| **Flet** | Framework para construção da interface de usuário (GUI) multiplataforma. |
| **Decimal** | Módulo para manipulação de aritmética de ponto flutuante com precisão. |

## Pré-requisitos

Para executar esta aplicação, você precisa ter o **Python 3.x** instalado em seu sistema.

## Instalação e Execução

Siga os passos abaixo para configurar e rodar a calculadora em sua máquina local.

### 1. Instalar o Flet

Abra seu terminal ou prompt de comando e instale a biblioteca `flet`:

```bash
pip install flet
```

### 2. Salvar o Código

Salve o código da aplicação em um arquivo chamado `calculadora.py` (ou o nome que preferir).

### 3. Executar a Aplicação

Execute o arquivo Python diretamente:

```bash
python calculadora.py
```

A aplicação será aberta em uma nova janela com as dimensões 420x620 pixels.

## Estrutura do Código

O código é organizado em uma função principal (`main`) que configura a página do Flet e define a lógica da calculadora:

*   **`main(page: ft.Page)`:** Função principal que inicializa a interface, define as propriedades da janela e adiciona os componentes.
*   **Lógica de Funções:** As funções `number_click`, `operator_click`, `calculate_click` e `clear` gerenciam a entrada de dados, a manipulação de operadores e a execução dos cálculos, utilizando a função nativa `eval()` de forma controlada.
*   **Componentes UI:** O display (`ft.TextField`) e os botões são criados e organizados em linhas (`ft.Row`) dentro de uma coluna principal (`ft.Column`). A função `create_button` é utilizada para padronizar a aparência dos botões.

## Autor

O código original foi desenvolvido por:

**Roberto Lobo Siquara**

---
*README gerado por Manus AI.*
