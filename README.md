
# Árvore Binária de Busca com Interface Gráfica

Este projeto implementa uma árvore binária de busca  com uma interface gráfica para gerenciar funcionários municipais, considerando suas posições e níveis de amizade. A árvore é visualizada usando Graphviz, e a interface gráfica é criada com Tkinter.

## Funcionalidades

- Inserção de funcionários com informações de nome, cargo, salário e nível de amizade.
- Exibição gráfica da árvore binária de busca.
- Cálculo e exibição das somas dos salários e dos auxílios paletó dos funcionários na subárvore direita.

## Estrutura do Projeto

### Classe `No`

A classe `No` representa cada funcionário na árvore.

- **Atributos**:
  - `nome`: Nome do funcionário.
  - `cargo`: Cargo do funcionário.
  - `salario`: Salário do funcionário.
  - `amizade`: Nível de amizade com o prefeito.
  - `esquerda`: Filho esquerdo na árvore.
  - `direita`: Filho direito na árvore.

- **Métodos**:
  - `calcular_auxilio_paleto()`: Calcula o valor do auxílio paletó com base no nível de amizade.
  - `calcular_salario_com_auxilio()`: Retorna o salário somado ao auxílio paletó.
  - `__str__()`: Representação em string do nó.

### Classe `ArvoreBinariaBusca`

A classe `ArvoreBinariaBusca` gerencia a estrutura da árvore.

- **Atributos**:
  - `raiz`: Raiz da árvore.

- **Métodos**:
  - `inserir(nome, cargo, salario, amizade)`: Insere um novo nó na árvore.
  - `_inserir_aux(raiz, novo_no)`: Método auxiliar para inserir um nó na posição correta.
  - `imprimir_arvore(no, nivel)`: Imprime a árvore no console.
  - `gerar_grafico()`: Gera um gráfico da árvore usando Graphviz.
  - `_adicionar_no_grafico(dot, no)`: Adiciona um nó ao gráfico do Graphviz.
  - `somar_subarvore_direita()`: Retorna a soma dos salários e dos auxílios paletó na subárvore direita.
  - `_somar_aux(no)`: Método auxiliar para calcular as somas.

### Interface Gráfica

A interface gráfica foi construída usando Tkinter.

- **Inputs**:
  - `Nome`: Entrada de texto para o nome do funcionário.
  - `Cargo`: Combobox para selecionar o cargo (inicia apenas com "Prefeito").
  - `Salário`: Entrada de texto para o salário.
  - `Amizade`: Combobox para selecionar o nível de amizade.

- **Botões**:
  - `Inserir Funcionário`: Insere um funcionário na árvore.
  - `Mostrar Somas dos Salários`: Exibe as somas dos salários e dos auxílios paletó da subárvore direita.
  - `Soma dos Auxílios Paletó (Amizade 4)`: Exibe as somas dos Auxílios Paletó dos amizade 4.


- **Avisos**:
  - Mensagens de erro se as condições iniciais não forem atendidas (o primeiro funcionário deve ser o Prefeito com amizade nível 1).
  - Mensagens informativas sobre os níveis de amizade.

## Como Executar

1. **Instale as dependências necessárias**:
   - Tkinter (normalmente já incluído no Python padrão)
   - Graphviz e sua extensão Python (`pip install graphviz`)

2. **Execute o script**:
   ```bash
   python nome_do_script.py
   ```

3. **Insira os dados do Prefeito primeiro**:
   - Nome: Insira o nome do Prefeito.
   - Cargo: Selecione "Prefeito".
   - Salário: Insira o salário do Prefeito.
   - Amizade: Selecione nível de amizade 1.

4. **Insira outros funcionários**:
   - Após inserir o Prefeito, todos os cargos serão habilitados.

5. **Visualize a árvore e as somas**:
   - A árvore será atualizada automaticamente após cada inserção.
   - Clique no botão "Mostrar Somas dos Salários" para ver as somas da subárvore direita.

## Exemplo de Uso

```python
# Insira o prefeito
Nome: João
Cargo: Prefeito
Salário: 10000
Amizade: 1

# Insira um vereador
Nome: Maria
Cargo: Vereador
Salário: 8000
Amizade: 2

# Insira um comissionado
Nome: José
Cargo: Comissionado
Salário: 6000
Amizade: 3
```

Ao clicar em "Mostrar Somas dos Salários", uma mensagem exibirá a soma dos salários e dos auxílios paletó de todos os funcionários na subárvore direita da árvore.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Autor

- Natanael Batista - [Seu Perfil no GitHub](https://github.com/NatanaelBT)



