import tkinter as tk
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import time
from bs4 import BeautifulSoup




    
def achar_nome(drivegoogle):
    html = drivegoogle.page_source
    soup = BeautifulSoup(html, 'html.parser')
    elemento_h1 = soup.find('h1', class_='css-1xo9k5n-H1ShareTitle')
    if elemento_h1:
        nome = elemento_h1.get_text(strip=True)
        print(f'O nome amostrado no elemento é: {nome}')
    else:
        print('Elemento não encontrado.')

def criar_duas_contas():
    menu_de_criação.destroy()
    pass

def finalizar_conta(drivegoogle):
    buscar_cookies_e_salvar()
    drivegoogle.quit()
    pass
    
def ler_email_invertexto(drivegoogle):
    wait = WebDriverWait(drivegoogle, 30)
    elemento_email = wait.until(EC.presence_of_element_located((By.ID, 'email-input')))
    email = elemento_email.get_attribute('value')
    print(f'O e-mail mostrado no elemento é: {email}')
    return email

def buscar_cookies_e_salvar(drivegoogle):
    cookies = drivegoogle.get_cookies()
    cookies_dir = os.path.join(os.path.dirname(__file__), "cookies")
    os.makedirs(cookies_dir, exist_ok=True)
    cookies_path = os.path.join(cookies_dir, "cookies.json")
    with open(cookies_path, "w") as file:
        json.dump(cookies, file, indent=4)

def abrir_invertexto(drivegoogle):
    drivegoogle.get("https://www.invertexto.com/gerador-email-temporario")
    time.sleep(2)
    return ler_email_invertexto(drivegoogle)
def abrir_twtktk_abas(drivegoogle):
    drivegoogle.execute_script("window.open('https://twitter.com/i/flow/signup');")
    time.sleep(0.5)
    drivegoogle.execute_script("window.open('https://www.tiktok.com/login');")
    
def receber_nome_twitter(drivegoogle):
    wait = WebDriverWait(drivegoogle, 10)
    botao_perfil = wait.until(EC.presence_of_element_located((By.ID, 'id_do_seu_botao_perfil')))
    botao_perfil.click()
    wait.until(EC.url_contains('site.com/'))
    link_perfil = drivegoogle.current_url
    print(link_perfil)
    return link_perfil
    
def abrir_nova_janela():
    menu_de_criação.destroy()
    window = tk.Tk()
    window.geometry("300x400")
    button2 = tk.Button(window, text="Achar Nome", command=achar_nome)
    button3 = tk.Button(window, text="Criei Twitter", command=receber_nome_twitter)
    button = tk.Button(window, text="Finalizar Conta", command=finalizar_conta)
    button.pack(pady=10)
    button2.pack(pady=10)
    button3.pack(pady=10)
    return window
    
    
def abrir_uma_aba():
    driver = webdriver.Chrome()
    abrir_invertexto(driver)
    abrir_twtktk_abas(driver)
    
    
def criar_uma_conta():
    abrir_nova_janela().mainloop()
    abrir_uma_aba()
    pass

    
menu_de_criação = tk.Tk()
menu_de_criação.geometry("300x400")
menu_de_criação.title("Menu de Criação")
buttoncriacao1 = tk.Button(menu_de_criação, text="Criar uma conta", command=criar_uma_conta)
buttoncriacao2 = tk.Button(menu_de_criação, text="Criar duas contas", command=criar_duas_contas)
buttoncriacao1.pack(pady=10)
buttoncriacao2.pack(pady=10)



menu_de_criação.mainloop()