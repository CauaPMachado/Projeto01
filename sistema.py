import customtkinter
from tkinter import ttk
import sqlite3

item_vet = 0


def abrir_frame_cadastrar():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_cadastrar.grid_propagate(False)
    frame_cadastrar.grid(row=0, column=1, pady=5, padx=5)


def abrir_frame_editar():
    frame_cadastrar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_editar.grid_propagate(False)
    frame_editar.grid(row=0, column=1, pady=5, padx=5)
    ler_dados_editar()


def abrir_frame_saida():
    frame_editar.grid_forget()
    frame_cadastrar.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_saida.grid_propagate(False)
    frame_saida.grid(row=0, column=1, pady=5, padx=5)
    ler_dados_saida()


def abrir_frame_entrada():
    frame_saida.grid_forget()
    frame_editar.grid_forget()
    frame_cadastrar.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_entrada.grid_propagate(False)
    frame_entrada.grid(row=0, column=1, pady=5, padx=5)
    ler_dados_entrada()


def abrir_frame_relatorio_estoque():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_cadastrar.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_estoque.grid_propagate(False)
    frame_relatorio_estoque.grid(row=0, column=1, pady=5, padx=5)
    ler_dados()


def abrir_frame_relatorio_entrada():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_cadastrar.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_propagate(False)
    frame_relatorio_entrada.grid(row=0, column=1, pady=5, padx=5)


def abrir_frame_relatorio_saida():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_cadastrar.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_propagate(False)
    frame_relatorio_saida.grid(row=0, column=1, pady=5, padx=5)


def adicionar_item():
    global item_vet
    item_vet = str(Nome_produto.get())

    if item_vet in items:
        item_texto = Nome_produto.get()

        if item_texto:
            frame_item = customtkinter.CTkFrame(lista_frame)
            frame_item.pack(fill="x", pady=2, padx=5)

            label = customtkinter.CTkLabel(frame_item, text=item_texto, anchor="w")
            label.pack(side="left", fill="x", expand=True, padx=5)

            botao_remover = customtkinter.CTkButton(frame_item, text="🗑", width=30,
                                                    command=lambda: frame_item.destroy())
            botao_remover.pack(side="right", padx=5)

            Nome_produto.delete(0, "end")


def adicionar_item_entrada():
    global item_vet
    item_vet = str(Nome_entrada.get())

    if item_vet in items:
        item_texto = Nome_entrada.get()
        if item_texto:
            frame_item = customtkinter.CTkFrame(lista_frame_entrada)
            frame_item.pack(fill="x", pady=2, padx=5)

            label = customtkinter.CTkLabel(frame_item, text=item_texto, anchor="w")
            label.pack(side="left", fill="x", expand=True, padx=5)

            botao_remover = customtkinter.CTkButton(frame_item, text="🗑", width=30,
                                                    command=lambda: frame_item.destroy())
            botao_remover.pack(side="right", padx=5)

            Nome_entrada.delete(0, "end")


def abrir_janela():
    pop_up = customtkinter.CTk()
    pop_up.title("Pop-Up")
    pop_up.geometry("450x250")
    escolher_relatorio = customtkinter.CTkLabel(pop_up, text="Escolher Relatório(s):", font=("Arial", 15, "bold"))
    escolher_relatorio.grid(pady=10, column=0, sticky="nw", padx=40, row=0)
    escolher_extensao = customtkinter.CTkLabel(pop_up, text="Escolher Extensão:", font=("Arial", 15, "bold"))
    escolher_extensao.grid(pady=10, column=1, sticky="ne", padx=40, row=0)
    exportar_estoque = customtkinter.CTkCheckBox(pop_up, text="Exportar Estoque:", border_color="#0055F5")
    exportar_estoque.grid(pady=10, column=0, padx=40, row=1, stick="w")
    exportar_saida = customtkinter.CTkCheckBox(pop_up, text="Exportar Saida:", border_color="#0055F5")
    exportar_saida.grid(pady=10, column=0, padx=40, row=2, stick="w")
    exportar_entrada = customtkinter.CTkCheckBox(pop_up, text="Exportar Entrada:", border_color="#0055F5")
    exportar_entrada.grid(pady=10, column=0, padx=40, row=3, stick="w")
    word = customtkinter.CTkCheckBox(pop_up, text="Word:", border_color="#0055F5")
    word.grid(pady=10, column=1, padx=40, row=1, stick="w")
    excel = customtkinter.CTkCheckBox(pop_up, text="Excel:", border_color="#0055F5")
    excel.grid(pady=10, column=1, padx=40, row=2, stick="w")
    pdf = customtkinter.CTkCheckBox(pop_up, text="PDF:", border_color="#0055F5")
    pdf.grid(pady=10, column=1, padx=40, row=3, stick="w")
    botao_cancelar_pop = customtkinter.CTkButton(pop_up, text="Cancelar", width=80, height=30)
    botao_cancelar_pop.grid(pady=10, column=1, padx=15, row=4, stick="w")
    botao_salvar_pop = customtkinter.CTkButton(pop_up, text="Salvar", width=80, height=30, fg_color="#013ADF")
    botao_salvar_pop.grid(pady=10, column=1, padx=15, row=4, stick="e")
    pop_up.mainloop()


def criar_banco():
    conexao = sqlite3.connect("banco_sistema_estoque.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(
        "CREATE TABLE IF NOT EXISTS produtos (nome text, preco decimal, descricao text, quantidade int)")
    conexao.commit()
    conexao.close()


def salvar_dados():
    conexao = sqlite3.connect("banco_sistema_estoque.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(
        f"INSERT INTO produtos (nome,preco,descricao,quantidade) VALUES ('{entrada_nome.get()}',"
        f""f"'{float(entrada_preco.get())}','{entrada_descricao.get('1.0', 'end')}', '{0}')")
    conexao.commit()
    conexao.close()
    ler_dados()


def ler_dados():
    global caixa_editar
    conexao = sqlite3.connect("banco_sistema_estoque.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM produtos")
    recebe_dados = terminal_sql.fetchall()
    print(recebe_dados)

    for item in tree.get_children():
        tree.delete(item)

    for i in recebe_dados:
        produto = str(i[0])
        preco = str(i[1])
        descricao = str(i[2])
        quantidade = str(i[3])
        tree.insert("", "end", values=(produto, quantidade, preco, descricao))


def ler_dados_editar():
    global  caixa_editar
    conexao = sqlite3.connect("banco_sistema_estoque.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM produtos")
    items_editar = terminal_sql.fetchall()

    def selecionar_item(arg_item):
        conexao = sqlite3.connect("banco_sistema_estoque.db")
        terminal_sql = conexao.cursor()
        terminal_sql.execute(f"SELECT * FROM produtos WHERE nome ='{arg_item}'")
        receber_dados_produto = terminal_sql.fetchall()
        print(receber_dados_produto)

        nome_do_produto.insert(0, receber_dados_produto[0][0])
        valor_editar.insert(1, receber_dados_produto[0][1])
        caixa_de_texto.insert(0.0, receber_dados_produto[0][2])

    def desmarcar_item():
        nome_do_produto.delete(0, "end")
        valor_editar.delete(0, "end")
        caixa_de_texto.delete(0.0, "end")

    for item in scrollable_frame_editar.winfo_children():
        item.destroy()

    for item in items_editar:
        caixa_editar = customtkinter.CTkCheckBox(scrollable_frame_editar, text=item, border_color="#0055F5")
        caixa_editar.grid(pady=5, padx=10, stick="s")
        caixa_editar.configure(
            command=lambda nome=item[0], cb=caixa_editar: (selecionar_item(nome) if cb.get() == 1 else desmarcar_item())
        )


def ler_dados_saida():
    conexao = sqlite3.connect("banco_sistema_estoque.db")
    terminal_sql_saida = conexao.cursor()
    terminal_sql_saida.execute("SELECT nome FROM produtos")
    items_saida = terminal_sql_saida.fetchall()

    def selecionar_item(arg_item):
        conexao = sqlite3.connect("banco_sistema_estoque.db")
        terminal_sql = conexao.cursor()
        terminal_sql.execute(f"SELECT * FROM produtos WHERE nome ='{arg_item}'")
        receber_dados_produto = terminal_sql.fetchall()
        print(receber_dados_produto)

        Nome_produto.insert(0, receber_dados_produto[0][0])

    def desmarcar_item():
        Nome_produto.delete(0, "end")

    for widget in Lista_frame_saida.winfo_children():
        widget.destroy()

    for item in items_saida:
        caixa_saida = customtkinter.CTkCheckBox(Lista_frame_saida, text=item, border_color="#0055F5")
        caixa_saida.grid(pady=5, padx=10, stick="s")
        caixa_saida.configure(command=lambda nome=item[0], cb=caixa_saida: (selecionar_item(nome)
                                                                            if cb.get() == 1 else desmarcar_item()))


def ler_dados_entrada():
    conexao = sqlite3.connect("banco_sistema_estoque.db")
    terminal_sql_entrada = conexao.cursor()
    terminal_sql_entrada.execute("SELECT nome FROM produtos")
    items_entrada = terminal_sql_entrada.fetchall()

    def selecionar_item(arg_item):
        conexao = sqlite3.connect("banco_sistema_estoque.db")
        terminal_sql = conexao.cursor()
        terminal_sql.execute(f"SELECT * FROM produtos WHERE nome ='{arg_item}'")
        receber_dados_produto = terminal_sql.fetchall()
        print(receber_dados_produto)

        Nome_entrada.insert(0, receber_dados_produto[0][0])

    def desmarcar_item():
        Nome_entrada.delete(0, "end")

    for widget in scrollable_frame_entrada.winfo_children():
        widget.destroy()

    for item in items_entrada:
        caixa_entrada = customtkinter.CTkCheckBox(scrollable_frame_entrada, text=item[0], border_color="#0055F5")
        caixa_entrada.grid(pady=5, padx=10, stick="s")
        caixa_entrada.configure(
            command=lambda nome=item[0], cb=caixa_entrada: (
                selecionar_item(nome) if cb.get() == 1 else desmarcar_item()))


def deletar_dados(nome_produto):
    conexao = sqlite3.connect("banco_sistema_estoque.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"DELETE FROM produtos WHERE nome = '{nome_produto}'")
    conexao.commit()
    conexao.close()
    nome_do_produto.delete(0, "end")
    valor_editar.delete(0, "end")
    caixa_de_texto.delete(0.0, "end")
    ler_dados_editar()


def editar_produtos(nome_produto, preco_editar, caixa_texto):
    conexao = sqlite3.connect("banco_sistema_estoque.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(
        f"UPDATE produtos SET nome = '{nome_produto}',preco = '{preco_editar}', descricao = '{caixa_texto}' WHERE nome = '{nome_produto}'")
    conexao.commit()
    conexao.close()

    nome_do_produto.delete(0, "end")
    valor_editar.delete(0, "end")
    caixa_de_texto.delete(0.0, "end")
    ler_dados_editar()


criar_banco()

janela = customtkinter.CTk()
janela.title("Sistema de Gerenciamento")
janela.geometry("800x400")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#2a2d2e",
                foreground="white",
                rowheight=25,
                fieldbackground="#343638",
                bordercolor="#343638",
                borderwidth=0)
style.map('Treeview', background=[('selected', '#22559b')])

style.configure("Treeview.Heading",
                background="#2C6196",
                foreground="white",
                relief="flat")
style.map("Treeview.Heading",
          background=[('active', '#3484F0')])

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

frame_menu = customtkinter.CTkFrame(janela, width=196, height=380, corner_radius=2, border_color="#0055F5",
                                    border_width=2)
frame_menu.grid(row=0, column=0, pady=5, padx=5)
frame_menu.pack_propagate(False)

frame_cadastrar = customtkinter.CTkFrame(janela, width=580, height=380, corner_radius=2, border_color="#0055F5",
                                         border_width=2)
frame_cadastrar.grid(row=0, column=1, pady=5, padx=5)
frame_cadastrar.grid_propagate(False)

frame_editar = customtkinter.CTkFrame(janela, width=580, height=380, corner_radius=2, border_color="#0055F5",
                                      border_width=2)
frame_editar.grid_propagate(False)

frame_saida = customtkinter.CTkFrame(janela, width=580, height=380, corner_radius=2, border_color="#0055F5",
                                     border_width=2)
frame_saida.grid_propagate(False)

frame_entrada = customtkinter.CTkFrame(janela, width=580, height=380, corner_radius=2, border_color="#0055F5",
                                       border_width=2)
frame_entrada.grid_propagate(False)

frame_relatorio_estoque = customtkinter.CTkFrame(janela, width=580, height=380, corner_radius=2, border_color="#0055F5",
                                                 border_width=2)
frame_relatorio_estoque.grid_propagate(False)

frame_relatorio_entrada = customtkinter.CTkFrame(janela, width=580, height=380, corner_radius=2, border_color="#0055F5",
                                                 border_width=2)
frame_relatorio_entrada.grid_propagate(False)

frame_relatorio_saida = customtkinter.CTkFrame(janela, width=580, height=380, corner_radius=2, border_color="#0055F5",
                                               border_width=2)
frame_relatorio_saida.grid_propagate(False)

nome_do_sistema = customtkinter.CTkLabel(frame_menu, text="Nome do Sistema", font=("Arial", 20, "bold"))
nome_do_sistema.pack(pady=10)

botao_cadastrar = customtkinter.CTkButton(frame_menu, text="Cadastrar", command=abrir_frame_cadastrar,
                                          fg_color="#045FB4")
botao_cadastrar.pack(pady=10)

botao_editar = customtkinter.CTkButton(frame_menu, text="Editar", command=abrir_frame_editar, fg_color="#045FB4")
botao_editar.pack(pady=10)

botao_saida = customtkinter.CTkButton(frame_menu, text="Saida", command=abrir_frame_saida, fg_color="#045FB4")
botao_saida.pack(pady=10)

botao_entrada = customtkinter.CTkButton(frame_menu, text="Entrada", command=abrir_frame_entrada, fg_color="#045FB4")
botao_entrada.pack(pady=10)

botao_relatorio = customtkinter.CTkButton(frame_menu, text="Relatório", command=abrir_frame_relatorio_estoque,
                                          fg_color="#045FB4")
botao_relatorio.pack(pady=10)

# Frame Cadastrar

cadastro_do_produto = customtkinter.CTkLabel(frame_cadastrar, text="Cadastro do Produto", font=("Arial", 20, "bold"))
cadastro_do_produto.grid(pady=10, column=2)

label_nome_do_produto = customtkinter.CTkLabel(frame_cadastrar, text="Nome do produto:")
label_nome_do_produto.grid(pady=5, column=1, padx=7)

label_preco = customtkinter.CTkLabel(frame_cadastrar, text="Preço(R$):")
label_preco.grid(pady=5, column=1, sticky="e", padx=7)

label_descricao = customtkinter.CTkLabel(frame_cadastrar, text="Descrição:")
label_descricao.grid(pady=5, column=1, sticky="ne", padx=7)

entrada_nome = customtkinter.CTkEntry(frame_cadastrar, placeholder_text="Digite o nome do produto:", width=300,
                                      height=30, border_color="#00B8F5")
entrada_nome.grid(pady=5, row=1, column=2, padx=5, sticky="w")

entrada_preco = customtkinter.CTkEntry(frame_cadastrar, placeholder_text="0,00:", width=80, height=28,
                                       border_color="#00B8F5")
entrada_preco.grid(pady=5, row=2, column=2, padx=5, sticky="w")

entrada_descricao = customtkinter.CTkTextbox(frame_cadastrar, width=350, height=150)
entrada_descricao.grid(pady=5, row=3, column=2, padx=5, sticky="w")

botao_salvar = customtkinter.CTkButton(frame_cadastrar, text="Salvar", width=80, height=30, fg_color="#013ADF",
                                       command=salvar_dados)
botao_salvar.grid(pady=5, row=4, column=2, sticky="e", padx=5)

# Frame Editar

tela_editar = customtkinter.CTkLabel(frame_editar, text="Editar", font=("Arial", 20, "bold"))
tela_editar.grid(pady=10, row=0, column=1, sticky="n")

root = customtkinter.CTk()
root.geometry("580x380")

scrollable_frame_editar = customtkinter.CTkScrollableFrame(frame_editar, border_width=2, border_color="#00B8F5")
scrollable_frame_editar.grid(row=2, column=0, pady=5, padx=5, stick="ws", rowspan=4)

Buscar_produto = customtkinter.CTkEntry(frame_editar, placeholder_text="Buscar Produto:", width=220,
                                        border_color="#00B8F5")
Buscar_produto.grid(row=1, column=0)

nome_do_produto = customtkinter.CTkEntry(frame_editar, placeholder_text="Nome do produto:", border_color="#00B8F5")
nome_do_produto.grid(row=2, column=1, columnspan=3, stick="w")

valor_editar = customtkinter.CTkEntry(frame_editar, placeholder_text="R$ 0,00", border_color="#00B8F5")
valor_editar.grid(row=3, column=1, columnspan=3, stick="w")

caixa_de_texto = customtkinter.CTkTextbox(frame_editar, width=300, height=100)
caixa_de_texto.grid(pady=5, row=4, column=1, columnspan=3, padx=5)

botao_excluir = customtkinter.CTkButton(frame_editar, text="Excluir", width=80,
                                        command=lambda: deletar_dados(nome_do_produto.get()))
botao_excluir.grid(row=5, column=1, pady=5)

botao_cancelar_editar = customtkinter.CTkButton(frame_editar, text="Cancelar", width=80)
botao_cancelar_editar.grid(row=5, column=2, pady=5)

botao_salvar_editar = customtkinter.CTkButton(frame_editar, text="Salvar", width=80, fg_color="#013ADF",
                                              command=lambda: editar_produtos(nome_do_produto.get(),
                                                                              valor_editar.get(),
                                                                              caixa_de_texto.get(0.0, "end")))
botao_salvar_editar.grid(row=5, column=3, pady=5)

# Frame Saída

tela_saida = customtkinter.CTkLabel(frame_saida, text="Saida de Produto", font=("Arial", 20, "bold"))
tela_saida.grid(pady=10, column=1, sticky="n")

root = customtkinter.CTk()
root.geometry("580x380")

Campo_busca = customtkinter.CTkEntry(frame_saida, placeholder_text="Campo de Busca:", width=220, border_color="#00B8F5")
Campo_busca.grid(row=1, column=0)

Nome_produto = customtkinter.CTkEntry(frame_saida, placeholder_text="Nome do produto:", width=220,
                                      border_color="#00B8F5")
Nome_produto.grid(row=1, column=1)

quantidade_saida = customtkinter.CTkEntry(frame_saida, placeholder_text="Qtd a sair:",
                                          border_color="#00B8F5", width=105, height=30)
quantidade_saida.grid(padx=5, row=2, column=1, columnspan=3, stick="w")

botao_adicionar = customtkinter.CTkButton(frame_saida, text="Adicionar Item", width=105, height=30,
                                          command=adicionar_item)

botao_adicionar.grid(pady=5, row=2, column=1, sticky="e", padx=5)

botao_cancelar_saida = customtkinter.CTkButton(frame_saida, text="Cancelar", width=80, height=30)
botao_cancelar_saida.grid(row=4, column=1, sticky="w")

botao_salvar_saida = customtkinter.CTkButton(frame_saida, text="Salvar", width=80, height=30, fg_color="#013ADF")
botao_salvar_saida.grid(row=4, column=1, sticky="e")

Lista_frame_saida = customtkinter.CTkScrollableFrame(frame_saida, border_width=2, border_color="#00B8F5")
Lista_frame_saida.grid(row=2, column=0, pady=5, padx=5, stick="w", rowspan=6)

lista_frame = customtkinter.CTkFrame(frame_saida, width=220, height=180)
lista_frame.grid(padx=5, pady=5, row=3, column=1, stick="snwe")

# Frame Entrada

tela_entrada = customtkinter.CTkLabel(frame_entrada, text="Entrada", font=("Arial", 20, "bold"))
tela_entrada.grid(pady=10, column=1, sticky="n")

root = customtkinter.CTk()
root.geometry("580x380")
scrollable_frame_entrada = customtkinter.CTkScrollableFrame(frame_entrada, border_width=2, border_color="#00B8F5")
scrollable_frame_entrada.grid(row=2, column=0, pady=5, padx=5, stick="w", rowspan=6)

Campo_busca = customtkinter.CTkEntry(frame_entrada, placeholder_text="Campo de Busca:", width=220,
                                     border_color="#00B8F5")
Campo_busca.grid(row=1, column=0)

Nome_entrada = customtkinter.CTkEntry(frame_entrada, placeholder_text="Nome do produto:", width=220,
                                      border_color="#00B8F5")
Nome_entrada.grid(row=1, column=1)

quantidade_entrada = customtkinter.CTkEntry(frame_entrada, placeholder_text="Qtd a entrar:", border_color="#00B8F5",
                                            width=105,
                                            height=30)
quantidade_entrada.grid(padx=5, row=2, column=1, columnspan=3, stick="w")

botao_adicionar_item = customtkinter.CTkButton(frame_entrada, text="Adicionar Item", width=105, height=30,
                                               command=adicionar_item_entrada)
botao_adicionar_item.grid(pady=5, row=2, column=1, sticky="e", padx=5)

botao_cancelar_entrada = customtkinter.CTkButton(frame_entrada, text="Cancelar", width=80, height=30)
botao_cancelar_entrada.grid(row=4, column=1, sticky="w")

botao_salvar_entrada = customtkinter.CTkButton(frame_entrada, text="Salvar", width=80, height=30, fg_color="#013ADF")
botao_salvar_entrada.grid(row=4, column=1, sticky="e")

lista_frame_entrada = customtkinter.CTkFrame(frame_entrada, width=220, height=180)
lista_frame_entrada.grid(padx=5, pady=5, row=3, column=1, stick="snwe")

# Frame Relatório do Estoque

tela_relatorio_estoque = customtkinter.CTkLabel(frame_relatorio_estoque, text="Relatório de Estoque",
                                                font=("Arial", 20, "bold"))
tela_relatorio_estoque.grid(pady=10, column=0, sticky="n", columnspan=4)

Buscar_produto_relatorio_estoque = customtkinter.CTkEntry(frame_relatorio_estoque, placeholder_text="Buscar produto:",
                                                          width=220, border_color="#00B8F5")
Buscar_produto_relatorio_estoque.grid(row=1, column=0, sticky="w", padx=5)

botao_exportar = customtkinter.CTkButton(frame_relatorio_estoque, text="Exportar", width=80, height=30,
                                         command=abrir_janela)
botao_exportar.grid(row=1, column=3, sticky="e", padx=5)

tree = ttk.Treeview(frame_relatorio_estoque, columns=("Nome", "Quantidade", "Preço", "Descrição"), show="headings",
                    height=9)
tree.heading("Nome", text="Nome")
tree.heading("Quantidade", text="Quantidade")
tree.heading("Preço", text="Preço")
tree.heading("Descrição", text="Descrição")
tree.grid(padx=10, pady=10, columnspan=4)
tree.column("Nome", width=130, anchor="center")
tree.column("Quantidade", width=130, anchor="center")
tree.column("Preço", width=130, anchor="center")
tree.column("Descrição", width=135, anchor="center")

botao_saida_relatorio_estoque = customtkinter.CTkButton(frame_relatorio_estoque, text="Saida", width=80, height=30,
                                                        command=abrir_frame_relatorio_saida)
botao_saida_relatorio_estoque.grid(row=3, column=3)

botao_entrada_relatorio_estoque = customtkinter.CTkButton(frame_relatorio_estoque, text="Entrada", width=80, height=30,
                                                          command=abrir_frame_relatorio_entrada)
botao_entrada_relatorio_estoque.grid(row=3, column=2)

botao_estoque_relatorio_estoque = customtkinter.CTkButton(frame_relatorio_estoque, text="Estoque", width=80, height=30,
                                                          command=abrir_frame_relatorio_estoque)
botao_estoque_relatorio_estoque.grid(row=3, column=1)

# Frame Relatório da Entrada

tela_relatorio_entrada = customtkinter.CTkLabel(frame_relatorio_entrada, text="Relatório de Entrada",
                                                font=("Arial", 20, "bold"))
tela_relatorio_entrada.grid(pady=10, column=0, sticky="n", columnspan=4)

Buscar_produto_relatorio_entrada = customtkinter.CTkEntry(frame_relatorio_entrada, placeholder_text="Buscar produto:",
                                                          width=220, border_color="#00B8F5")
Buscar_produto_relatorio_entrada.grid(row=1, column=0, sticky="w", padx=5)

botao_exportar_relatorio_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text="Exportar", width=80,
                                                           height=30, command=abrir_janela)
botao_exportar_relatorio_entrada.grid(row=1, column=3, sticky="e", padx=5)

tree_entrada = ttk.Treeview(frame_relatorio_entrada, columns=("Nome", "Quantidade", "Data/Hora"), show="headings",
                            height=9)
tree_entrada.heading("Nome", text="Nome")
tree_entrada.heading("Quantidade", text="Quantidade")
tree_entrada.heading("Data/Hora", text="Data/Hora")
tree_entrada.grid(padx=10, pady=10, columnspan=4)
tree_entrada.column("Nome", width=175)
tree_entrada.column("Quantidade", width=175)
tree_entrada.column("Data/Hora", width=175)

botao_saida_relatorio_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text="Saida", width=80, height=30,
                                                        command=abrir_frame_relatorio_saida)
botao_saida_relatorio_entrada.grid(row=3, column=3)

botao_entrada_relatorio_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text="Entrada", width=80, height=30,
                                                          command=abrir_frame_relatorio_entrada)
botao_entrada_relatorio_entrada.grid(row=3, column=2)

botao_estoque_relatorio_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text="Estoque", width=80, height=30,
                                                          command=abrir_frame_relatorio_estoque)
botao_estoque_relatorio_entrada.grid(row=3, column=1)

# Frame Relatório da Saida

tela_relatorio_saida = customtkinter.CTkLabel(frame_relatorio_saida, text="Relatório de Saida",
                                              font=("Arial", 20, "bold"))
tela_relatorio_saida.grid(pady=10, column=0, sticky="n", columnspan=4)

Buscar_produto_relatorio_saida = customtkinter.CTkEntry(frame_relatorio_saida, placeholder_text="Buscar produto:",
                                                        width=220, border_color="#00B8F5")
Buscar_produto_relatorio_saida.grid(row=1, column=0, sticky="w", padx=5)

botao_exportar_relatorio_saida = customtkinter.CTkButton(frame_relatorio_saida, text="Exportar", width=80, height=30,
                                                         command=abrir_janela)
botao_exportar_relatorio_saida.grid(row=1, column=3, sticky="e", padx=5)

tree_saida = ttk.Treeview(frame_relatorio_saida, columns=("Nome", "Quantidade", "Data/Hora"), show="headings", height=9)
tree_saida.heading("Nome", text="Nome")
tree_saida.heading("Quantidade", text="Quantidade")
tree_saida.heading("Data/Hora", text="Data/Hora")
tree_saida.grid(padx=10, pady=10, columnspan=4)
tree_saida.column("Nome", width=175)
tree_saida.column("Quantidade", width=175)
tree_saida.column("Data/Hora", width=175)

botao_saida_relatorio_saida = customtkinter.CTkButton(frame_relatorio_saida, text="Saida", width=80, height=30,
                                                      command=abrir_frame_relatorio_saida)
botao_saida_relatorio_saida.grid(row=3, column=3)

botao_entrada_relatorio_saida = customtkinter.CTkButton(frame_relatorio_saida, text="Entrada", width=80, height=30,
                                                        command=abrir_frame_relatorio_entrada)
botao_entrada_relatorio_saida.grid(row=3, column=2)

botao_estoque_relatorio_saida = customtkinter.CTkButton(frame_relatorio_saida, text="Estoque", width=80, height=30,
                                                        command=abrir_frame_relatorio_estoque)
botao_estoque_relatorio_saida.grid(row=3, column=1)

janela.mainloop()
