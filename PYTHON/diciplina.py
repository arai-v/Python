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
root.geometry("1280x720")
root.configure(bg="white")

# Título da janela
title = tk.Label(root, text="Disciplinas Cadastradas", font=("Montserrat", 24), bg="white", fg="#004080")
title.pack(pady=20)

# Botão de adicionar movido para o topo da tela e à direita
add_btn = tk.Button(
    root, 
    text="Adicionar +", 
    font=("Montserrat", 18), 
    bg="white", 
    fg="#004080", 
    borderwidth=2, 
    relief="solid", 
    highlightbackground="white"
)
add_btn.pack(side="top", anchor="ne", padx=400, pady=10)  # Ajustado para o canto superior direito

# Canvas para aplicar o gradiente no menu
canvas = tk.Canvas(root, width=1280, height=720, highlightthickness=0)
canvas.pack(pady=20)

# Criar o gradiente dentro do canvas
create_gradient(canvas, 1280, 720, color1, color2)

# Adicionar a imagem fita.png ao canvas (esquerda)
fita_img = tk.PhotoImage(file="fita.png")
canvas.create_image(50, 40, image=fita_img, anchor="center")

# Desenhar o retângulo do menu com cantos arredondados dentro do novo tamanho
rounded_rectangle(canvas, 10, 10, 1270, 710, radius=50, fill="", outline="", width=0)

# Adicionar linha vertical no meio
canvas.create_line(640, 0, 640, 810, fill="white", width=1)

# Funções de edição e exclusão
def edit_discipline():
    print("Editando disciplina")

def delete_discipline():
    print("Excluindo disciplina")

# Lista de disciplinas
disciplinas = [
    "Língua Portuguesa", "Literatura", "Matemática", "Geografia", 
    "História", "Física", "Química", "Biologia", "Inglês", "Espanhol"
]

# Criar as disciplinas dentro do canvas, ajustando para o novo tamanho
for i, disciplina in enumerate(disciplinas):
    x = 100 if i < 5 else 740  # Ajuste para a nova largura
    y = 100 + (i % 5) * 110    # Ajuste para nova altura
    
    # Caixa de texto com o nome da disciplina (vazado com contorno branco)
    rounded_rectangle(canvas, x, y, x + 500, y + 80, radius=15, fill="", outline="white", width=1)
    
    # Alterando a cor da letra para branco
    canvas.create_text(x + 250, y + 40, text=disciplina, font=("Montserrat", 18), fill="white")

    # Desenhar linha vertical dentro do quadrado da disciplina
    canvas.create_line(x + 460, y + 1, x + 460, y + 80, fill="white", width=1)

    # Adicionar linha horizontal dentro do quadrado
    canvas.create_line(x + 500, y + 40, x + 460, y + 40, fill="white", width=1)

    # Ícones de edição e exclusão como botões
    icon_x = x + 507  # Aumentado para mover os ícones para a direita
    icon_y = y + 40   # Coordenada y centralizada
    
    # Botão de edição (ícone de lápis)
    edit_btn = tk.Button(canvas, text="✏️", font=("Montserrat", 14), fg="black", bg="#ffffff", bd=1, command=edit_discipline, width=2)  # Largura reduzida
    canvas.create_window(icon_x, icon_y - 20, window=edit_btn)
    
    # Botão de exclusão (ícone de lixeira)
    delete_btn = tk.Button(canvas, text="🗑️", font=("Montserrat", 14), fg="black", bg="#ffffff", bd=1, command=delete_discipline, width=2)  # Largura reduzida
    canvas.create_window(icon_x, icon_y + 20, window=delete_btn)

# Carregar a imagem da logo e redimensioná-la
logo_img = tk.PhotoImage(file="logo.png").subsample(2, 2)  # Reduzindo a escala pela metade

# Exibir a logo redimensionada
logo_label = tk.Label(root, image=logo_img, bg="white")
logo_label.pack(pady=(30, 10))  # Aumentando o espaçamento superior para mover a logo mais para baixo

root.mainloop()
