def generate_key(p, g, private_key):
    public_key = (g ** private_key) % p
    return public_key

def generate_shared_secret(public_key_lawan, private_key_sendiri, p):
    shared_secret = (public_key_lawan ** private_key_sendiri) % p
    return shared_secret

# Input parameter prime (p) dan generator (g)
p = int(input("Masukkan nilai prime (p): "))
g = int(input("Masukkan nilai generator (g): "))

# Pihak A
private_key_a = int(input("Masukkan private key Pihak A: "))
public_key_a = generate_key(p, g, private_key_a)

# Pihak B
private_key_b = int(input("Masukkan private key Pihak B: "))
public_key_b = generate_key(p, g, private_key_b)

# Penukaran kunci
shared_secret_a = generate_shared_secret(public_key_b, private_key_a, p)
shared_secret_b = generate_shared_secret(public_key_a, private_key_b, p)

print("\nPublic Key A:", public_key_a)
print("Public Key B:", public_key_b)
print("Shared Secret A:", shared_secret_a)
print("Shared Secret B:", shared_secret_b)

# Pertukaran pesan "terenkripsi"
message = input("\nMasukkan pesan yang akan ditukar: ")

# Pihak A "mengamankan" pesan dengan shared secret
secured_message_a = ''.join([chr(ord(char) + shared_secret_a) for char in message])

# Pihak B mendekripsi pesan dengan shared secret
decrypted_message_b = ''.join([chr(ord(char) - shared_secret_b) for char in secured_message_a])

print("\nPesan Terenkripsi (Pihak A):", secured_message_a)
print("Pesan Terdekripsi (Pihak B):", decrypted_message_b)
