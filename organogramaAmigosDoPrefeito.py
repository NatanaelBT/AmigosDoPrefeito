import tkinter as tk
from tkinter import ttk
from graphviz import Digraph

class No:
    def __init__(self, nome, cargo, salario, amizade):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.amizade = amizade
        self.esquerda = None
        self.direita = None
    
    def calcular_auxilio_paleto(self):
        if self.amizade == 1:
            return self.salario * 0.10
        elif self.amizade == 2:
            return self.salario * 0.05
        elif self.amizade == 3:
            return self.salario * 0.06
        return 0

    def calcular_salario_com_auxilio(self):
        return self.salario + self.calcular_auxilio_paleto()

    def __str__(self):
        auxilio_paleto = self.calcular_auxilio_paleto()
        return f'Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario:.2f}, Amizade: {self.amizade}, Auxílio Paletó: {auxilio_paleto:.2f}'

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, nome, cargo, salario, amizade):
        novo_no = No(nome, cargo, salario, amizade)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_aux(self.raiz, novo_no)
    
    def _inserir_aux(self, raiz, novo_no):
        if novo_no.amizade <= raiz.amizade:
            if raiz.esquerda is None:
                raiz.esquerda = novo_no
            else:
                self._inserir_aux(raiz.esquerda, novo_no)
        else:
            if raiz.direita is None:
                raiz.direita = novo_no
            else:
                self._inserir_aux(raiz.direita, novo_no)
    
    def imprimir_arvore(self, no, nivel=0):
        if no is not None:
            self.imprimir_arvore(no.esquerda, nivel + 1)
            print(' ' * nivel * 4 + str(no))
            self.imprimir_arvore(no.direita, nivel + 1)

    def gerar_grafico(self):
        dot = Digraph()
        self._adicionar_no_grafico(dot, self.raiz)
        return dot

    def _adicionar_no_grafico(self, dot, no):
        if no is not None:
            label = f'{no.nome}\n{no.cargo}\nSalário: {no.salario:.2f}\nAmizade: {no.amizade}\nAuxílio: {no.calcular_auxilio_paleto():.2f}'
            dot.node(str(id(no)), label)
            if no.esquerda is not None:
                dot.edge(str(id(no)), str(id(no.esquerda)), label="esquerda")
                self._adicionar_no_grafico(dot, no.esquerda)
            if no.direita is not None:
                dot.edge(str(id(no)), str(id(no.direita)), label="direita")
                self._adicionar_no_grafico(dot, no.direita)

def inserir_funcionario():
    nome = entry_nome.get()
    cargo = combobox_cargo.get()
    salario = float(entry_salario.get())
    amizade = int(combobox_amizade.get())
    arvore.inserir(nome, cargo, salario, amizade)
    update_tree()

def update_tree():
    grafico = arvore.gerar_grafico()
    grafico.render("arvore_binaria_busca_amizade", format="png", cleanup=True)
    image = tk.PhotoImage(file="arvore_binaria_busca_amizade.png")
    label_tree.config(image=image)
    label_tree.image = image

# Criar a janela principal
root = tk.Tk()
root.title("Árvore Binária de Busca")

# Criar o frame para os inputs
frame_inputs = ttk.Frame(root)
frame_inputs.pack(pady=10)

# Entrada para o nome
label_nome = ttk.Label(frame_inputs, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = ttk.Entry(frame_inputs)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

# Entrada para o cargo
label_cargo = ttk.Label(frame_inputs, text="Cargo:")
label_cargo.grid(row=1, column=0, padx=5, pady=5)
combobox_cargo = ttk.Combobox(frame_inputs, values=["Prefeito", "Vice-Prefeito", "Vereador", "Comissionado", "Tesoureiro"], state="readonly")
combobox_cargo.grid(row=1, column=1, padx=5, pady=5)
combobox_cargo.current(0)



# Entrada para o salário
label_salario = ttk.Label(frame_inputs, text="Salário:")
label_salario.grid(row=2, column=0, padx=5, pady=5)
entry_salario = ttk.Entry(frame_inputs)
entry_salario.grid(row=2, column=1, padx=5, pady=5)

# Dropdown para a amizade
label_amizade = ttk.Label(frame_inputs, text="Amizade:")
label_amizade.grid(row=3, column=0, padx=5, pady=5)
combobox_amizade = ttk.Combobox(frame_inputs, values=[0, 1, 2, 3], state="readonly")
combobox_amizade.grid(row=3, column=1, padx=5, pady=5)
combobox_amizade.current(0)

# Botão para inserir funcionário
button_inserir = ttk.Button(frame_inputs, text="Inserir Funcionário", command=inserir_funcionario)
button_inserir.grid(row=4, columnspan=2, padx=5, pady=5)

# Frame para exibir a árvore
frame_tree = ttk.Frame(root)
frame_tree.pack()

# Label para exibir a árvore
label_tree = ttk.Label(frame_tree)
label_tree.pack(padx=10, pady=10)



# Criar uma instância da árvore
arvore = ArvoreBinariaBusca()

# Iniciar a interface gráfica
root.mainloop()