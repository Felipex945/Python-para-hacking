from math import isqrt

def decrypt_rsa(n: int, c: int) -> str:
    A = isqrt(n)
    if A * A < n:
        A += 1

    square_diff = A * A - n
    B = isqrt(square_diff)
    
    if B * B != square_diff:
        raise ValueError("A fatoração de Fermat falhou! Os números primos p e q não são próximos o suficiente.")

    p = A - B
    q = A + B

    phi = (p - 1) * (q - 1)
    d = pow(0x10001, -1, phi)

    m = pow(c, d, n)
    return m.to_bytes((m.bit_length() + 7) // 8, "big").decode()

if __name__ == "__main__":
    print("=" * 50)
    print("      RSA DECRYPTOR (Ataque de Fermat)      ")
    print("=" * 50)
    
    try:
        raw_n = input("Digite o valor de n (Módulo): ").strip()
        raw_c = input("Digite o valor de c (Texto Cifrado): ").strip()
        
        n = int(raw_n)
        c = int(raw_c)
        
        print("\nTentando quebrar a criptografia...")
        mensagem = decrypt_rsa(n, c)
        
        print("\n" + "-" * 50)
        print(f"Sucesso! Mensagem encontrada:\n{mensagem}")
        print("-" * 50)
        
    except ValueError as e:
        print(f"\n[!] Erro: {e}. Verifique se digitou apenas números válidos.")
    except Exception as e:
        print(f"\n[!] Ocorreu um erro inesperado: {e}")
