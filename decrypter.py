import os
import pyaes

def ler_chave():
    with open("salvo.txt", "rb") as f:
        chave = f.read()
    return chave

def descriptografar_arquivo(file_path, chave):
    with open(file_path, "rb") as file:
        crypto_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(chave)
    decrypted_data = aes.decrypt(crypto_data)

    new_file_path = file_path.replace(".ransomwaretroll", "")

    with open(new_file_path, 'wb') as new_file:
        new_file.write(decrypted_data)

    os.remove(file_path)

def descriptografar_diretorio(diretorio, chave):
    for root, dirs, files in os.walk(diretorio):
        for file_name in files:
            if file_name.endswith(".ransomwaretroll"):
                file_path = os.path.join(root, file_name)
                descriptografar_arquivo(file_path, chave)

chave = ler_chave()

diretorio_alvo = "/"

descriptografar_diretorio(diretorio_alvo, chave)

print("Todos os arquivos foram descriptografados com sucesso.")
