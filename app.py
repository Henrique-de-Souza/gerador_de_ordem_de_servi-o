import customtkinter as ctk
from fpdf import FPDF
from tkinter import messagebox
from PIL import Image



ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

class PlaceholderEntry(ctk.CTkEntry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self.on_entry_click)
        self.bind("<FocusOut>", self.on_focus_out)
        self.last_focused = None

    def on_entry_click(self, event):
        if self.get() == self.placeholder:
            self.delete(0, ctk.END)  # Remove o texto padrão
            self.place_configure(y=0)  # Define a posição inicial no canto superior esquerdo

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)  # Restaura o placeholder
            self.place_configure(y=0)  # Mantém a posição no canto superior esquerdo
        else:
            self.last_focused = self  # Atualiza o último campo focado

# minha janela principal
janela = ctk.CTk()
janela.geometry("820x600")
janela.title("Gerador de Ordem de Serviço")
janela.resizable(False, False)

def on_entry_click(event, entry):
    if entry.get() == entry.placeholder:
        entry.delete(0, ctk.END)  # Remove o texto padrão

def gerar_ordem_de_servico():
    messagebox.showinfo('Carregando...', 'Sua ordem de serviço está sendo gerada')
    pdf = FPDF()
    pdf.add_page()  # Adiciona uma página padrão
    pdf.set_font('Arial', 'B', size=12)

    # Adicionando a imagem do template
    pdf_width = 210
    pdf_height = 297
    imagem_width = 210
    imagem_height = 297
    x = (pdf_width - imagem_width) / 2
    y = (pdf_height - imagem_height) / 2
    pdf.image("template5.png", x=x, y=y, w=imagem_width, h=imagem_height)

    # Posicionar cada elemento no template
    nome_texto = campo_nome.get()
    rua_texto = campo_rua.get()
    num_texto = campo_num.get()
    bairro_texto = campo_bairro.get()
    complemento_texto = campo_complemento.get()
    veiculo_texto = campo_veiculo.get()
    placa_texto = campo_placa.get()
    relato_texto = campo_relato.get()
    servico_texto = campo_servico.get()
    garantia_observacoes_texto = campo_garantia_observacoes.get()
    preco1_texto = campo_preco1.get()
    preco2_texto = campo_preco2.get()
    total_texto = campo_total.get()
    data_texto = campo_data.get()

    # posicionar cada elemento no template
    pdf.text(32, 64, nome_texto)
    pdf.text(39, 75, rua_texto)
    pdf.text(25, 87, num_texto)
    pdf.text(34, 99, bairro_texto)
    pdf.text(51,110, complemento_texto)
    pdf.text(76, 132, veiculo_texto)
    pdf.text(76, 141, placa_texto)
    pdf.text(10, 167, relato_texto)
    pdf.text(10, 203, servico_texto)
    pdf.text(10, 233, garantia_observacoes_texto)
    pdf.text(149, 267, preco1_texto)
    pdf.text(149, 274, preco2_texto)
    pdf.text(149, 281, total_texto)
    pdf.text(157, 27, data_texto)

    pdf.output("ordemdeservico.pdf")
    print("Ordem de Serviço gerada com sucesso!")



# Layout da janela
dados_cliente = ctk.CTkLabel(
    janela,
    text='DADOS DO CLIENTE:',
    text_color='black',
    font=('Verdana', 15),
    width=367, height=45,
    bg_color='#CFCFCF'
)
dados_cliente.place(x=20, y=40)

# Adicionando a capacidade de usar placeholders nos campos de entrada
campo_nome = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o nome do cliente:",
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_nome.place(x=20, y=100)

campo_rua = ctk.CTkEntry(
    janela,
    placeholder_text="Rua",
    border_color='#CFCFCF',
    border_width=1,
    width=270
)
campo_rua.place(x=20, y=150)

campo_num = ctk.CTkEntry(
    janela,
    placeholder_text="nº",
    border_color='#CFCFCF',
    border_width=1,
    width=85
)
campo_num.place(x=300, y=150)

campo_bairro = ctk.CTkEntry(
    janela,
    placeholder_text="Bairro",
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_bairro.place(x=20, y=200)

campo_complemento = ctk.CTkEntry(
    janela,
    placeholder_text='Complemento',
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_complemento.place(x=20, y=250)

dados_veiculo = ctk.CTkLabel(
    janela,
    text='DADOS DO VEÍCULO:',
    text_color='black',
    font=('Verdana', 15),
    width=367, height=45,
    bg_color='#CFCFCF')
dados_veiculo.place(x=20, y=300)

campo_veiculo = ctk.CTkEntry(
    janela,
    placeholder_text="Veículo",
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_veiculo.place(x=20, y=360)

campo_placa = ctk.CTkEntry(
    janela,
    placeholder_text="placa",
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_placa.place(x=20, y=405)

relato_cliente = ctk.CTkLabel(
    janela,
    text='RELATO DO CLIENTE:',
    text_color='black',
    font=('Verdana', 15),
    width=367, height=45,
    bg_color='#CFCFCF'
)
relato_cliente.place(x=20, y=450)

campo_relato = ctk.CTkEntry(
    janela,
    placeholder_text="Digite aqui o relato de seu cliente...",
    border_color='#CFCFCF',
    border_width=1,
    width=367, height=50
)
campo_relato.place(x=20, y=510)

servico_prestado = ctk.CTkLabel(
    janela,
    text='SERVIÇO A SER PRESTADO:',
    text_color='black',
    font=('Verdana', 15),
    width=367, height=45,
    bg_color='#CFCFCF'
)
servico_prestado.place(x=430, y=40)

campo_servico = ctk.CTkEntry(
    janela,
    placeholder_text="Digite aqui o serviços que serão prestados...",
    border_color='#CFCFCF',
    border_width=1,
    width=367, height=50
)
campo_servico.place(x=430, y=105)

garantia = ctk.CTkLabel(
    janela,
    text='GARANTIA E OBSERVAÇÕES:',
    text_color='black',
    font=('Verdana', 15),
    width=367, height=45,
    bg_color='#CFCFCF'
)
garantia.place(x=430, y=180)

campo_garantia_observacoes = ctk.CTkEntry(
    janela,
    placeholder_text="Garantia e observações...",
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_garantia_observacoes.place(x=430, y=245)

orcamento = ctk.CTkLabel(
    janela,
    text='ORÇAMENTO:',
    text_color='black',
    font=('Verdana', 15),
    width=367, height=45,
    bg_color='#CFCFCF'
)
orcamento.place(x=430, y=300)

campo_preco1 = ctk.CTkEntry(
    janela,
    placeholder_text="Preço do serviço prestado R$",
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_preco1.place(x=430, y=360)

campo_preco2 = ctk.CTkEntry(
    janela,
    placeholder_text="Preço das peças usadas R$",
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_preco2.place(x=430, y=409)

campo_total = ctk.CTkEntry(
    janela,
    placeholder_text="Preço Total R$",
    border_color='#CFCFCF',
    border_width=1,
    width=367
)
campo_total.place(x=430, y=455)


campo_data = ctk.CTkEntry(
    janela,
    placeholder_text= 'Data dd/mm/aaaa',
    border_color='#CFCFCF',
    border_width=1,
    width=150
)
campo_data.place(x=430,y=512)

botao = ctk.CTkButton(
    janela, 
    text="Gerar Ordem de Serviço", 
    width=150, height=30,
    command=gerar_ordem_de_servico
)
botao.place(x=645, y=512)

janela.mainloop()