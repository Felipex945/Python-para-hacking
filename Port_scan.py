import socket

IP = '192.168.0.1'  # Exemplo. Mude para o IP real da máquina da vítima.

PORTA = [21, 22, 23, 25, 80, 443, 8080] # Portas de serviços conhecidos. Adapte de acordo com suas necessidades.

print(f"Iniciando varredura em: {IP}\n")

for porta in PORTA:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
        scanner.settimeout(1.0) # Diminua o tempo caso sejam muitas portas.
        
        resultado = scanner.connect_ex((IP, porta))
        
        if resultado == 0:
            print(f"[+] Porta {porta}: ABERTA")
        else:
            print(f"[-] Porta {porta}: Fechada/Filtrada por Firewall")
