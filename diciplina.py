import tkinter as tk

# Função para criar gradiente dentro de um canvas
def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * i / height)
        g = int(color1[1] + (color2[1] - color1[1]) * i / height)
        b = int(color1[2] + (color2[2] - color1[2]) * i / height)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

# Função para desenhar um retângulo com cantos arredondados
def rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        (x1 + radius, y1), (x2 - radius, y1),
        (x2, y1, x2, y1 + radius), (x2, y2 - radius),
        (x2, y2, x2 - radius, y2), (x1 + radius, y2),
        (x1, y2, x1, y2 - radius), (x1, y1 + radius),
        (x1, y1, x1 + radius, y1)
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Cores RGB para o gradiente
color1 = (0, 142, 179)   # Azul
color2 = (60, 33, 121)   # Roxo

# Janela principal
root = tk.Tk()
root.title("Disciplinas Cadastradas")
root.geometry("1400x900")
root.configure(bg="white")

# Título da janela
title = tk.Label(root, text="Disciplinas Cadastradas", font=("Montserrat", 18), bg="white", fg="#004080")
title.pack(pady=20)

# Botão de adicionar movido para o topo da tela e à direita
add_btn = tk.Button(
    root, 
    text="Adicionar +", 
    font=("Montserrat", 16), 
    bg="white", 
    fg="#004080", 
    borderwidth=2, 
    relief="solid", 
    highlightbackground="white"
)
add_btn.pack(side="top", anchor="ne", padx=450, pady=10)  # Ajustado para o canto superior direito

# Canvas para aplicar o gradiente no menu
canvas = tk.Canvas(root, width=1200, height=800, highlightthickness=0)
canvas.pack(pady=20)

# Criar o gradiente dentro do canvas
create_gradient(canvas, 1200, 800, color1, color2)

# Desenhar o retângulo do menu com cantos arredondados sem contorno
rounded_rectangle(canvas, 10, 10, 1190, 790, radius=70, fill="", outline="", width=0)

# Adicionar linha vertical no meio
canvas.create_line(600, 10, 600, 790, fill="white", width=1)

# Lista de disciplinas
disciplinas = [
    "Língua Portuguesa", "Literatura", "Matemática", "Geografia", 
    "História", "Física", "Química", "Biologia", "Inglês", "Espanhol"
]

# Criar as disciplinas dentro do canvas
for i, disciplina in enumerate(disciplinas):
    x = 100 if i < 5 else 700  # Ajuste para a nova largura
    y = 100 + (i % 5) * 120
    
    # Caixa de texto com o nome da disciplina (vazado com contorno branco)
    rounded_rectangle(canvas, x, y, x + 350, y + 60, radius=10, fill="", outline="white", width=1)
    
    # Alterando a cor da letra para branco
    canvas.create_text(x + 150, y + 30, text=disciplina, font=("Montserrat", 20), fill="white")

    # Desenhar linha vertical dentro do quadrado da disciplina
    canvas.create_line(x + 310, y + 1, x + 310, y + 60, fill="white", width=1)

    # Adicionar linha horizontal dentro do quadrado
    canvas.create_line(x + 350, y + 30, x + 310, y + 30, fill="white", width=1)

    # Ícones de edição e exclusão próximos da borda
    icon_x = x + 347  # Coordenada x para os ícones
    icon_y = y + 30   # Coordenada y centralizada
    canvas.create_text(icon_x, icon_y - 15, text="✏️", font=("Montserrat", 21), fill="white", tags="edit")  # Lápis
    canvas.create_text(icon_x, icon_y + 13, text="🗑️", font=("Montserrat", 17), fill="white", tags="delete")  # Lixeira

# Funções de edição e exclusão (placeholder)
def edit_discipline(event):
    print("Editando disciplina")

def delete_discipline(event):
    print("Excluindo disciplina")

# Bind dos eventos de clique para os ícones
canvas.tag_bind("edit", "<Button-1>", edit_discipline)
canvas.tag_bind("delete", "<Button-1>", delete_discipline)

root.mainloop()
