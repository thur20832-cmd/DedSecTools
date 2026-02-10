#!/usr/bin/env python
import requests, os, sys, platform, socket, threading, time, random
# ... resto do código ...
import requests, os, sys, platform, socket, threading, time, random

# Cores e Configurações
G, R, B, W, C = '\033[92m', '\033[91m', '\033[94m', '\033[0m', '\033[96m'
chars = "ABCDEFGHIJKLMNPQRSTUVWXYZ0123456789#@$&*%"

def limpar(): os.system('cls' if os.name == 'nt' else 'clear')

def efeito_hacker(texto, delay=0.04):
    for letra in texto:
        for _ in range(3):
            sys.stdout.write(f"{G}{random.choice(chars)}{W}"); sys.stdout.flush()
            time.sleep(0.01); sys.stdout.write("\b")
        sys.stdout.write(f"{G}{letra}{W}"); sys.stdout.flush(); time.sleep(delay)
    print()

def welcome_ghost():
    limpar()
    # Sequência de Boot Hacker
    efeito_hacker(">>> INICIALIZANDO PROTOCOLO DE ACESSO REMOTO...", 0.02)
    time.sleep(0.5)
    efeito_hacker(">>> QUEBRANDO CRIPTOGRAFIA DE PONTA... [OK]", 0.02)
    efeito_hacker(">>> IGNORANDO FIREWALLS LOCAIS... [OK]", 0.02)
    efeito_hacker(">>> RASTREANDO NODOS DA REDE MUNDIAL...", 0.02)
    time.sleep(0.8)
    
    print(f"\n{G}╔════════════════════════════════════════════╗")
    print(f"║       BEM-VINDO AO SISTEMA DEDSEC          ║")
    print(f"║     'A INFORMAÇÃO QUER SER LIVRE'          ║")
    print(f"╚════════════════════════════════════════════╝{W}")
    
    # Notificação se estiver no Android
    if os.name != 'nt':
        os.system('termux-notification --title "DEDSEC" --content "Acesso Concedido" --led-color 00FF00')
    
    input(f"\n{C}[ Pressione Enter para entrar no Menu ]{W}")

# --- MÓDULO CHAT ---
def receber_msg(sock):
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if msg: print(f"\n{B}[PESSOA]:{W} {msg}\n{C}>>> {W}", end="")
        except: break

def chat():
    limpar()
    print(f"{G}--- DEDSEC PRIVATE COMMS ---{W}")
    modo = input("1. Servidor (Esperar Pessoa) | 2. Cliente (Conectar ao Pessoa)\n> ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        if modo == '1':
            s.bind(('0.0.0.0', 4444)); s.listen(1)
            print(f"{C}[!] Aguardando conexão na porta 4444...{W}"); conn, addr = s.accept(); target = conn
        else:
            ip = input(f"{C}Digite o IP da pessoa: {W}"); s.connect((ip, 4444)); target = s
        
        threading.Thread(target=receber_msg, args=(target,), daemon=True).start()
        print(f"{G}[+] Chat Ativo! Digite sua mensagem abaixo.{W}")
        while True:
            msg = input(f"{C}>>> {W}"); target.send(msg.encode('utf-8'))
    except Exception as e: print(f"{R}Erro de Conexão: {e}{W}"); time.sleep(2)

# --- MÓDULO IP SCAN DETALHADO ---
def ip_tool():
    limpar()
    print(f"{G}--- DEDSEC IP INTELLIGENCE ---{W}")
    alvo = input(f"{C}IP ou URL do Alvo (Vazio para o seu): {W}")
    try:
        res = requests.get(f"http://ip-api.com/json/{alvo}?fields=66846719").json()
        if res['status'] == 'success':
            print(f"\n{G}[+] RELATÓRIO DE INTELIGÊNCIA:{W}")
            print(f"{B}Endereço IP:{W} {res.get('query')}")
            print(f"{B}Localização:{W} {res.get('city')}, {res.get('regionName')}, {res.get('country')}")
            print(f"{B}Provedor (ISP):{W} {res.get('isp')}")
            print(f"{B}Organização:{W} {res.get('org')}")
            print(f"{B}Fuso Horário:{W} {res.get('timezone')}")
            print(f"{B}Coordenadas:{W} {res.get('lat')}, {res.get('lon')}")
        else: print(f"{R}[!] Falha: Alvo inválido.{W}")
    except: print(f"{R}[!] Erro de rede.{W}")
    input(f"\n{G}Pressione Enter para voltar...{W}")

# --- MENU PRINCIPAL ---
def menu():
    welcome_ghost() # Inicia com a animação
    while True:
        limpar()
        print(f"{G}╔══════════════════════════════════════╗")
        print(f"║          DEDSEC TOOLS v2.0           ║")
        print(f"║      'Everything is connected'       ║")
        print(f"╚══════════════════════════════════════╝{W}")
        print(f"{G}[1]{W} IP Intelligence (Detalhado)")
        print(f"{G}[2]{W} Chat Privado (Socket)")
        print(f"{G}[3]{W} Rodar Welcome Ghost novamente")
        print(f"{R}[4]{W} Sair")
        print(f"{B}Feito por Arthur e Gemini{W}")

        op = input(f"\n{C}DedSecTools@Arthur:{W}")
        
        if op == '1': ip_tool()
        elif op == '2': chat()
        elif op == '3': welcome_ghost()
        elif op == '4': sys.exit()

if __name__ == "__main__":
    menu()

