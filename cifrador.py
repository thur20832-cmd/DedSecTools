alfabeto_real = "abcdefghijklmnopqrstuvwxyz"
minha_chave    = "qwertyuiopasdfghjklzxcvbnm" # Você pode mudar a ordem dessas letras!

def cifrar(texto):
    resultado = ""
    for letra in texto.lower():
        if letra in alfabeto_real:
            indice = alfabeto_real.index(letra)
            resultado += minha_chave[indice]
        else:
            resultado += letra
    return resultado

msg = input("Digite a mensagem secreta: ")
print("Mensagem Cifrada: " + cifrar(msg)) 


