from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import tkinter as tk
from tkinter import messagebox

def obter_mensagem():
    global mensagem 

    root = tk.Tk()
    root.title("")  
    root.geometry("500x400") 
    root.configure(bg='#f8f9fa') 
    
    def enviar_mensagem():
        global mensagem  
        msg = entrada.get("1.0", "end-1c")  
        if not msg.strip(): 
            messagebox.showwarning("Aviso", "A mensagem não pode estar vazia.")
            return
        mensagem = msg  
        root.quit()  

    def tecla_enter(event):
        enviar_mensagem()

    label = tk.Label(root, text="Digite a mensagem:", wraplength=560,
                     font=("Helvetica", 14), bg='#f8f9fa', fg='#000000')
    label.pack(pady=20) 
    
    entrada = tk.Text(root, wrap=tk.WORD, height=10, width=70,
                      font=("Helvetica", 12), bg='#ffffff', fg='#000000', borderwidth=2, relief="groove")
    entrada.pack(pady=15) 
    
    entrada.bind("<Return>", tecla_enter)
    
    botao_enviar = tk.Button(root, text="Enviar", command=enviar_mensagem,
                             font=("Helvetica", 12, "bold"), bg='#28a745', fg='#ffffff', relief="raised", borderwidth=2)
    botao_enviar.pack(pady=20) 
    
    root.mainloop()

 
obter_mensagem()


telefone = '27996872006'
link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

webbrowser.open('https://web.whatsapp.com/')
sleep(5)
webbrowser.open(link_mensagem_whatsapp)
sleep(10)  
pyautogui.press('enter')
sleep(2) 

print("Mensagem enviada!")





from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import schedule
import time

mensagem = "OI ISSO É UMA MENSAGEM AUTOMATICA"

telefone = '27997611547'
link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'

def enviar_mensagem():
    webbrowser.open('https://web.whatsapp.com/')
    sleep(10)  
    webbrowser.open(link_mensagem_whatsapp)
    sleep(15)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.hotkey('ctrl', 'w')

schedule.every().day.at("____").do(enviar_mensagem)

while True:
    schedule.run_pending()
    time.sleep(1)


