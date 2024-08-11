import tkinter as tk 
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# Criando janela {
janela = tk.Tk()
janela.title("APP DE TAREFAS") #-->  configurando o titulo da janela
janela.configure(bg="#F0F0F0") #--> defindo uma cor padrão para o fundo da janela
janela.geometry("500x600") #-->Passando as dimensões da janela 

frameEdicao = None # --> toda vez que vamos editar a tarefa, precisamos de um framr
#Função para add tarefa
def adicionarTarefa():
    global frameEdicao
    tarefa = entradaTarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frameEdicao is not None:
            atualizarTarefa(tarefa)
            frameEdicao = None
        else:
            adicionarItemTarefa(tarefa)
            entradaTarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira uma tarefa." )
        
def adicionarItemTarefa(entrada):
    frameTarefa = tk.frame(canvasInterior, bg="White, bd=1, relief= tk.SOLID")        
    labelTarefa = tk.Label(frameTarefa, text=tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")
    labelTarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady= 5)
    botaoEditar = tk.Button(frameTarefa, image=iconEditar)
    
    
cabecalho = font.Font(family="Garamond", size= 24, weight="bold") #--> Estou especificando a font do titulo
cabecalho = tk.Label(janela, text= "APP DE TAREFAS", font=cabecalho, bg="#F0F0F0", fg= "#333").pack(pady=20)#--> passando as especificações do que sera escrito 

frame = tk.Frame(janela, bg="#F0F0F0") #--> passando as especificaçoes do local onde armazena o adionarTarefa e o botaoAdiciona
frame.pack(pady=10) 

adicionaTarefas = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg = "white", fg="grey", width=30)
adicionaTarefas.pack(side=tk.LEFT, padx=10) #--> Local onde o usuario passa a tarefa

botaoAdiciona = tk.Button(frame, text="Adicionar Tarefa", bg="#038C3E", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botaoAdiciona.pack(side=tk.LEFT, padx=10) #--> botão utilizado para gerar uma tarefa

#frama para lista de tarefas, com scroll
frameListaTarefas = tk.Frame(janela, bg="white")
frameListaTarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady = 10) 

canvas = tk.Canvas(frameListaTarefas, bg="White")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)#--> primeiras especificações da tela onde aparecera as tarefas


scroollBar = ttk.Scrollbar(frameListaTarefas, orient="vertical", command=canvas.yview)
scroollBar.pack(side=tk.RIGHT, fill=tk.Y) # --> Gerando um scrool para navegação nas tarefas
canvas.configure(yscrollcommand= scroollBar.set) 
canvasInterior = tk.Frame(canvas, bg="white")
canvas.create_window((0,0), window=canvasInterior, anchor="nw")
canvasInterior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all" )) )

janela.mainloop()