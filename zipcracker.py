import multiprocessing
import zipfile

# Attempting to extract the contents
def extractZip(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print("[-] Wrong Password")
        return

# Looping over the extractZip() function with a wordlist file
def main():
    zfile = zipfile.ZipFile('passwords.zip')    # Change filename
    passFile = open('passwords.txt')            # Change wordlist
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractZip(zfile, password)
        if guess:
            print("[+] The password is: " + password)
            zfile.printdir()
            break

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.apply_async(main())
    pool.close()
    pool.join()
