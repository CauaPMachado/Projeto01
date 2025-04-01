import customtkinter
import sqlite3

def criar_banco():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text, idade int)")
    conexao.commit()
    conexao.close()


def salvar_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"INSERT INTO pessoas (nome) VALUES ('{entrada.get()}')")
    conexao.commit()
    conexao.close()


def ler_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM pessoas")
    recebe_dados = terminal_sql.fetchall()
    print(recebe_dados)

    nome = ""
    for i in recebe_dados:
        nome += "\n" + str(i[0])
    label_lista.configure(text=nome)

criar_banco()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Sistema Salva Nome")
janela.geometry("300x300")

label_nome = customtkinter.CTkLabel(janela, text="Sistema\n Salva Nome", font=("Arial", 20, "bold"))
label_nome.pack(pady=20)

entrada = customtkinter.CTkEntry(janela, placeholder_text="Nome:")
entrada.pack(pady=5)

botao_salvar = customtkinter.CTkButton(janela, text="Salvar", command=salvar_dados)
botao_salvar.pack(pady=5)

botao_listar = customtkinter.CTkButton(janela, text="Listar", command=ler_dados)
botao_listar.pack(pady=5)

label_lista = customtkinter.CTkLabel(janela, text="")
label_lista.pack(pady=5)


janela.mainloop()