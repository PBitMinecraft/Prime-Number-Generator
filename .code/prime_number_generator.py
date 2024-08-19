import os
import keyboard
from sympy import isprime

def get_last_prime(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as file:
                file.seek(-2, os.SEEK_END)
                while file.tell() > 0:
                    byte = file.read(1)
                    if byte == b'\n':
                        line = file.readline().decode('utf-8').strip()
                        if line:
                            try:
                                return int(line)
                            except ValueError:
                                continue
                    file.seek(-2, os.SEEK_CUR)
                file.seek(0)
                first_line = file.readline().decode('utf-8').strip()
                if first_line:
                    try:
                        return int(first_line)
                    except ValueError:
                        pass
        except IOError as e:
            print(f"Error reading file: {e}")
    return 1

def append_prime_to_file(filename, prime):
    try:
        with open(filename, 'a') as file:
            file.write(f"{prime}\n")
    except IOError as e:
        print(f"Error writing to file: {e}")

def main():
    filename = "prime_numbers.txt"
    last_prime = get_last_prime(filename)

    print(f"Starting from {last_prime}. Press 'q' to stop.")

    while True:
        next_num = last_prime + 1
        while not isprime(next_num):
            next_num += 1
        
        append_prime_to_file(filename, next_num)
        last_prime = next_num
        print(f"Generated prime: {next_num}")

        if keyboard.is_pressed('q'):
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
