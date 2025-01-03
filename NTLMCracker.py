import hashlib


def ntlm_hash(password):

    #Generate NTLM Hash For a Given Pass
    return hashlib.new('md4', password.encode('utf-16le')).hexdigest()


def crack_ntlm_hash(target_hash, wordlist_file):

    try:
        with open (wordlist_file, "r") as file:
            for line in file:
                password = line.strip()
                hashed_password = ntlm_hash(password)
                print(f"Trying : {password} ---> {hashed_password}")

                if hashed_password.lower() == target_hash.lower():
                    print(f"[+] Password Found : {password}")
        
        print(f"[-] Password Not Found ")

    except FileNotFoundError:
        print("[-] WordList File Not Found")
        


if __name__ == "__main__":
    target_hash = input("Enter The NTLM Hash To Crack: ").strip()
    wordlist_file = input("Enter The Path To The WordList File :").strip()

crack_ntlm_hash(target_hash, wordlist_file)