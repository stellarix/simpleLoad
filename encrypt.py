import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt_file(input_file, output_file, key, iv):
    
    with open(input_file, 'rb') as f:
        file_data = f.read()

    
    cipher = AES.new(key, AES.MODE_CBC, iv)

    padded_data = pad(file_data, AES.block_size)

    encrypted_data = cipher.encrypt(padded_data)

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

    print(f"File encrypted and saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Encrypt a file using AES-CBC-128.")
    parser.add_argument('-i', '--input', required=True, help="Input file to encrypt")
    parser.add_argument('-o', '--output', required=True, help="Output file for encrypted data")
    parser.add_argument('-k', '--key', required=False, help="AES key as a 16-character string")
    parser.add_argument('-v', '--iv', required=False, help="AES IV as a 16-character string")

    args = parser.parse_args()

    
    if args.key:
        if len(args.key) != 16:
            raise ValueError("Key must be a 16-character string.")
        key = args.key.encode()
    else:
        key = get_random_bytes(16)
        print(f"Generated AES Key: {key.hex()}")

    
    if args.iv:
        if len(args.iv) != 16:
            raise ValueError("IV must be a 16-character string.")
        iv = args.iv.encode()
    else:
        iv = get_random_bytes(16)
        print(f"Generated AES IV: {iv.hex()}")

    
    encrypt_file(args.input, args.output, key, iv)

if __name__ == "__main__":
    main()
