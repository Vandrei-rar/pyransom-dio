import os
import pyaes
import argparse

# Pegando o nome do arquivo
parser = argparse.ArgumentParser()
parser.add_argument("arquivo", help="é o nome do arquivo")

args = parser.parse_args()
ext = os.path.splitext(args.arquivo)[1]

if ext == ".crybaby":
    file = open(args.arquivo, "rb")
    data = file.read()
    file.close()

    # Definindo chave de descriptografia
    key = b"chavederansombye"
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(data)
    os.remove(args.arquivo)

    new_file = args.arquivo.replace(".crybaby", "")
    dencrypt_file = open(f'{new_file}','wb')
    dencrypt_file.write(decrypt_data)
    dencrypt_file.close()

    print(args.arquivo, "descriptografrado com sucesso!")
else:
    print("Não foi possível descriptografar ", args.arquivo)
