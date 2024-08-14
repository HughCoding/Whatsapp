from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import tkinter as tk
from tkinter import messagebox

# Função para obter a mensagem do usuário
def obter_mensagem():
    global mensagem  #! Global var

    # Configurar a janela principal
    root = tk.Tk()
    root.title("")  
    root.geometry("600x400") 
    root.configure(bg='#f8f9fa') 

    # Função para enviar mensagem e fechar a janela
    def enviar_mensagem():
        global mensagem  # Declarar que estamos usando a variável global
        msg = entrada.get("1.0", "end-1c")  # Captura o texto da caixa de texto
        if not msg.strip(): 
            messagebox.showwarning("Aviso", "A mensagem não pode estar vazia.")
            return
        mensagem = msg  # Atualiza a variável global
        root.quit()  # Fecha a janela

    # Função para chamar ao pressionar Enter
    def tecla_enter(event):
        enviar_mensagem()

    # Widgets
    label = tk.Label(root, text="Digite a mensagem:", wraplength=560,
                     font=("Helvetica", 14), bg='#f8f9fa', fg='#000000')
    label.pack(pady=20)  # Espaço ao redor
    
    entrada = tk.Text(root, wrap=tk.WORD, height=10, width=70,
                      font=("Helvetica", 12), bg='#ffffff', fg='#000000', borderwidth=2, relief="groove")
    entrada.pack(pady=15) 
    
    # Associa a função de pressionar Enter ao widget Text
    entrada.bind("<Return>", tecla_enter)
    
    botao_enviar = tk.Button(root, text="Enviar", command=enviar_mensagem,
                             font=("Helvetica", 12, "bold"), bg='#28a745', fg='#ffffff', relief="raised", borderwidth=2)
    botao_enviar.pack(pady=20) 
    
    root.mainloop()  # Exibe a janela e aguarda a interação

# Obter a mensagem 
obter_mensagem()

# Configuração do número de telefone e link do WhatsApp
telefone = '27996872006'
link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

# Abrir o WhatsApp Web
webbrowser.open('https://web.whatsapp.com/')
sleep(5)

# Abrir o link no navegador
webbrowser.open(link_mensagem_whatsapp)
sleep(10)  

pyautogui.press('enter')
sleep(2) 

print("Mensagem enviada!")
