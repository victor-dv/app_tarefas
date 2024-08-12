import tkinter as tk 
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criando janela
janela = tk.Tk()
janela.title("APP DE TAREFAS") #--> configurando o título da janela
janela.configure(bg="#F0F0F0") #--> definindo uma cor padrão para o fundo da janela
janela.geometry("650x600") #--> Passando as dimensões da janela 

frameEdicao = None # --> Toda vez que vamos editar a tarefa, precisamos de um frame

# Função para adicionar tarefa
def adicionarTarefa():
    global frameEdicao
    tarefa = adicionaTarefas.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frameEdicao is not None:
            atualizarTarefa(tarefa)
            frameEdicao = None
        else:
            adicionarItemTarefa(tarefa)
            adicionaTarefas.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira uma tarefa.")

def adicionarItemTarefa(tarefa):
    frameTarefa = tk.Frame(canvasInterior, bg="White", bd=1, relief=tk.SOLID)     
       
    labelTarefa = tk.Label(frameTarefa, text=tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")
    labelTarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)
    
    botaoEditar = tk.Button(frameTarefa, image=iconEditar, command=lambda f=frameTarefa, l=labelTarefa: prepararEdicao(f, l), bg="white", relief=tk.FLAT)
    botaoEditar.pack(side=tk.RIGHT, padx=5)
    
    botaoDeletar = tk.Button(frameTarefa, image=iconDeletar, command=lambda f=frameTarefa: deletarTarefa(f), bg="white", relief=tk.FLAT)
    botaoDeletar.pack(side=tk.RIGHT, padx=5)
    
    frameTarefa.pack(fill=tk.X, padx=5, pady=5)
    
    checkButton = ttk.Checkbutton(frameTarefa, command=lambda label=labelTarefa: alterarSublinhado(label))
    checkButton.pack(side=tk.RIGHT, padx=5)
    
    canvasInterior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def prepararEdicao(frameTarefa, labelTarefa):
    global frameEdicao
    frameEdicao = frameTarefa
    adicionaTarefas.delete(0, tk.END)    
    adicionaTarefas.insert(0, labelTarefa.cget("text"))

def atualizarTarefa(novaTarefa):
    global frameEdicao
    for widget in frameEdicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=novaTarefa)

def deletarTarefa(frameTarefa):
    frameTarefa.destroy()
    canvasInterior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def alterarSublinhado(label):
    fontAtual = label.cget("font")
    if "overstrike" in fontAtual:
        novaFonte = fontAtual.replace("overstrike", "")
    else:
        novaFonte = fontAtual + " overstrike"
    label.config(font=novaFonte)

iconEditar = PhotoImage(file="./img/edit.png").subsample(10, 10)
iconDeletar = PhotoImage(file="./img/delete.png").subsample(10, 10)

fonteCabecalho = font.Font(family="Garamond", size=24, weight="bold") #--> Estou especificando a fonte do título
tk.Label(janela, text="APP DE TAREFAS", font=fonteCabecalho, bg="#F0F0F0", fg="#333").pack(pady=20) #--> passando as especificações do que será escrito 

frame = tk.Frame(janela, bg="#F0F0F0") #--> passando as especificações do local onde armazena o adicionarTarefa e o botaoAdicionar
frame.pack(pady=10) 

adicionaTarefas = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
adicionaTarefas.pack(side=tk.LEFT, padx=10) #--> Local onde o usuário passa a tarefa

botaoAdiciona = tk.Button(frame, command=adicionarTarefa, text="Adicionar Tarefa", bg="#038C3E", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botaoAdiciona.pack(side=tk.LEFT, padx=10) #--> botão utilizado para gerar uma tarefa

# Frame para lista de tarefas, com scroll
frameListaTarefas = tk.Frame(janela, bg="white")
frameListaTarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10) 

canvas = tk.Canvas(frameListaTarefas, bg="White")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) #--> Primeiras especificações da tela onde aparecerão as tarefas

scrollBar = ttk.Scrollbar(frameListaTarefas, orient="vertical", command=canvas.yview)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y) # --> Gerando um scroll para navegação nas tarefas
canvas.configure(yscrollcommand=scrollBar.set) 
canvasInterior = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvasInterior, anchor="nw")
canvasInterior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")) )

janela.mainloop()
