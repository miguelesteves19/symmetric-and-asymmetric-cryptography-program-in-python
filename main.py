from symmetric_cipher import generate_symmetric_key, symmetric_encrypt, symmetric_decrypt
from asymmetric_cipher import generate_asymmetric_keys, save_private_key, save_public_key, load_private_key, load_public_key, asymmetric_encrypt, asymmetric_decrypt

def main():

    # Input do utilizador:
    data = input("Insira os dados que deseja criptografar: ")

    # Criptografia Simétrica:
    symmetric_key = generate_symmetric_key()
    encrypted_data_symmetric = symmetric_encrypt(data, symmetric_key)
    decrypted_data_symmetric = symmetric_decrypt(encrypted_data_symmetric, symmetric_key)

    # Criptografia Assimétrica:
    private_key, public_key = generate_asymmetric_keys()
    save_private_key(private_key)
    save_public_key(public_key)

    loaded_private_key = load_private_key()
    loaded_public_key = load_public_key()

    encrypted_data_asymmetric = asymmetric_encrypt(data, loaded_public_key)
    decrypted_data_asymmetric = asymmetric_decrypt(encrypted_data_asymmetric, loaded_private_key)

    # Resultados do input:
    print("\nResultados:")
    print("Os seus dados originais:", data)
    print("\nPara a criptografia Simétrica:")
    print("Chave Simétrica:", symmetric_key)
    print("Dados criptografados (Simétrica):", encrypted_data_symmetric)
    print("Dados descriptografados (Simétrica):", decrypted_data_symmetric)

    print("\nPara a criptografia Assimétrica:")
    print("Sua Chave Privada:", private_key)
    print("Sua Chave Pública:", public_key)
    print("Dados criptografados (Assimétrica):", encrypted_data_asymmetric)
    print("Dados descriptografados (Assimétrica):", decrypted_data_asymmetric)

if __name__ == "__main__":
    main()
