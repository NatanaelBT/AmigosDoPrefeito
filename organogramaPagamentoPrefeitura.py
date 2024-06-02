import tkinter as tk
from tkinter import ttk, messagebox
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
        elif self.amizade == 4:
            return self.salario * 0.70
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
            label = f'{no.nome}\n{no.cargo}\nSalário: {no.salario:.2f}\nAmizade: {no.amizade}\nAuxílio Paletó: {no.calcular_auxilio_paleto():.2f}'
            dot.node(str(id(no)), label)
            if no.esquerda is not None:
                dot.edge(str(id(no)), str(id(no.esquerda)), label="esquerda")
                self._adicionar_no_grafico(dot, no.esquerda)
            if no.direita is not None:
                dot.edge(str(id(no)), str(id(no.direita)), label="direita")
                self._adicionar_no_grafico(dot, no.direita)

    def somar_subarvore_direita(self):
        if self.raiz is None:
            return 0, 0
        return self._somar_aux(self.raiz.direita)

    def somar_auxilio_amizade_4(self):
        return self._somar_auxilio_amizade_4(self.raiz)

    def _somar_aux(self, no):
        if no is None:
            return 0, 0
        salario = no.salario
        auxilio_paleto = no.calcular_auxilio_paleto()
        soma_salarios, soma_auxilios = salario, auxilio_paleto
        if no.esquerda is not None:
            esq_salarios, esq_auxilios = self._somar_aux(no.esquerda)
            soma_salarios += esq_salarios
            soma_auxilios += esq_auxilios
        if no.direita is not None:
            dir_salarios, dir_auxilios = self._somar_aux(no.direita)
            soma_salarios += dir_salarios
            soma_auxilios += dir_auxilios
        return soma_salarios, soma_auxilios

    def _somar_auxilio_amizade_4(self, no):
        if no is None:
            return 0
        soma_auxilios = no.calcular_auxilio_paleto() if no.amizade == 4 else 0
        soma_auxilios += self._somar_auxilio_amizade_4(no.esquerda)
        soma_auxilios += self._somar_auxilio_amizade_4(no.direita)
        return soma_auxilios

def inserir_funcionario():
    nome = entry_nome.get()
    cargo = combobox_cargo.get()
    salario = float(entry_salario.get())
    amizade = int(combobox_amizade.get())

    if arvore.raiz is None:
        if cargo != "Prefeito" or amizade != 1:
            messagebox.showerror("Erro", "O primeiro funcionário deve ser o Prefeito com nível de amizade 1.")
            return
    arvore.inserir(nome, cargo, salario, amizade)
    update_tree()

    # Habilitar todos os cargos após inserir o Prefeito
    if arvore.raiz is not None:
        combobox_cargo.config(values=["Prefeito", "Vice-Prefeito", "Vereador", "Comissionado", "Tesoureiro"])

def update_tree():
    grafico = arvore.gerar_grafico()
    grafico.render("arvore_binaria_busca_amizade", format="png", cleanup=True)
    image = tk.PhotoImage(file="arvore_binaria_busca_amizade.png")
    label_tree.config(image=image)
    label_tree.image = image

def mostrar_somas():
    salarios, auxilios = arvore.somar_subarvore_direita()
    messagebox.showinfo("Somas", f"Soma dos Salários: {salarios:.2f}\nSoma dos Auxílios Paletó: {auxilios:.2f}")

def mostrar_somas_auxilio_4():
    soma_auxilios = arvore.somar_auxilio_amizade_4()
    messagebox.showinfo("Somas Auxílio Paletó", f"Soma dos Auxílios Paletó (Amizade 4): {soma_auxilios:.2f}")

# Criar a janela principal
root = tk.Tk()
root.title("Árvore Binária de Busca")

# Aviso inicial
messagebox.showinfo("Aviso", "Por favor, insira os dados do Prefeito com nível de amizade 1 primeiro.")
messagebox.showinfo("Aviso", "Insira nível de amizade 0 para um zé ninguém, 2 para um conhecido, 3 para um parente e 4 para um fantasma.")

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
combobox_cargo = ttk.Combobox(frame_inputs, values=["Prefeito"], state="readonly")
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
combobox_amizade = ttk.Combobox(frame_inputs, values=[0, 1, 2, 3, 4], state="readonly")
combobox_amizade.grid(row=3, column=1, padx=5, pady=5)
combobox_amizade.current(0)

# Botão para inserir funcionário
button_inserir = ttk.Button(frame_inputs, text="Inserir Funcionário", command=inserir_funcionario)
button_inserir.grid(row=4, columnspan=2, padx=5, pady=5)

# Botão para mostrar somas da subárvore direita
button_somas = ttk.Button(frame_inputs, text="Mostrar Somas dos Salários", command=mostrar_somas)
button_somas.grid(row=5, columnspan=2, padx=5, pady=5)

# Botão para mostrar somas dos auxílios dos funcionários com amizade 4
button_somas_auxilio_4 = ttk.Button(frame_inputs, text="Mostrar Auxilios(Amizade 4)", command=mostrar_somas_auxilio_4)
button_somas_auxilio_4.grid(row=6, columnspan=2, padx=5, pady=5)

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
