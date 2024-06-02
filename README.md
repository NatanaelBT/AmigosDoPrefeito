# AmigosDoPrefeito
# Árvore Binária de Busca de Funcionários

Este projeto é uma aplicação de interface gráfica (GUI) desenvolvida em Python usando a biblioteca Tkinter. Ele permite a inserção de funcionários em uma árvore binária de busca baseada no nível de amizade dos funcionários, e visualiza essa árvore usando a biblioteca Graphviz.

## Funcionalidades

1. **Inserção de Funcionários**: O usuário pode inserir informações de funcionários, incluindo nome, cargo, salário e nível de amizade.
2. **Cálculo de Auxílio Paletó**: O programa calcula um auxílio baseado no nível de amizade do funcionário.
3. **Visualização da Árvore**: A árvore binária de busca é gerada e visualizada graficamente.

## Requisitos

- Python 3.x
- Tkinter
- Graphviz
- Bibliotecas Python: `graphviz`, `tkinter`, `ttk`

## Instalação

1. **Instale o Python 3.x**: Certifique-se de ter o Python instalado na sua máquina. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

2. **Instale o Graphviz**:
    - **Windows**: Baixe e instale o Graphviz [aqui](https://graphviz.gitlab.io/download/).
    - **macOS**: Use Homebrew para instalar: `brew install graphviz`.
    - **Linux**: Use o gerenciador de pacotes da sua distribuição, por exemplo: `sudo apt-get install graphviz`.

3. **Instale as Bibliotecas Python**:
    ```sh
    pip install graphviz
    ```

## Uso

1. **Executar o Programa**:
    - Salve o código em um arquivo Python, por exemplo, `arvore_binaria.py`.
    - Execute o programa:
      ```sh
      python arvore_binaria.py
      ```

2. **Inserir Funcionários**:
    - Preencha os campos "Nome", "Cargo", "Salário" e "Amizade".
    - Clique no botão "Inserir Funcionário" para adicionar o funcionário à árvore.

3. **Visualizar a Árvore**:
    - A árvore será gerada e visualizada na interface gráfica. A imagem da árvore será atualizada cada vez que um novo funcionário for inserido.

## Estrutura do Código

### Classes

- **No**: Representa um nó na árvore binária de busca. Contém informações sobre o funcionário, como nome, cargo, salário e nível de amizade. Também possui métodos para calcular o auxílio paletó e o salário com auxílio.
- **ArvoreBinariaBusca**: Implementa a árvore binária de busca. Permite a inserção de novos nós e a visualização da árvore.

### Funções

- **inserir_funcionario**: Coleta os dados do formulário e insere um novo funcionário na árvore.
- **update_tree**: Gera a visualização gráfica da árvore e a atualiza na interface gráfica.

### Interface Gráfica

- **Tkinter**: Usado para criar a interface gráfica. Contém entradas para o nome, cargo, salário e nível de amizade do funcionário, além de um botão para inserir o funcionário na árvore e um label para exibir a árvore.

### Execução

- O código inicia a interface gráfica Tkinter e aguarda a inserção de funcionários.

## Exemplo de Uso

1. **Preencha os dados do funcionário**:
    - Nome: "João"
    - Cargo: "Prefeito"
    - Salário: "5000.00"
    - Amizade: "1"

2. **Clique em "Inserir Funcionário"**: O funcionário será adicionado à árvore e a visualização será atualizada.


## Conclusão

Este projeto demonstra como combinar estruturas de dados (árvore binária de busca) com uma interface gráfica para criar uma aplicação interativa. 
