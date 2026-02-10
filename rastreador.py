import os

print("---------------------------------")
print("   RASTREADOR GEOGRÁFICO DEDSEC  ")
print("        Agente: Arthur           ")
print("---------------------------------")

ip = input("Digite o IP do alvo: ")
print(f"\n[!] Rastreando rastro digital de {ip}...\n")

# Usa o curl para buscar os dados de forma organizada
os.system(f"curl ip-api.com/line/{ip}")

print("\n---------------------------------")
print("[+] Busca concluída. Limpe os rastros após ler.")

