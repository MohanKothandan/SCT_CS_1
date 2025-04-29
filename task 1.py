def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return ''.join(result)

def print_welcome():
    print("\n📢 Welcome to the Caesar Cipher Program")
    print("-" * 40)
    print("Type 'encrypt' to encode a message")
    print("Type 'decrypt' to decode a message")
    print("Type 'history' to view previous results")
    print("Type 'exit' to quit the program")
    print("-" * 40 + "\n")

def main():
    history = []

    print_welcome()

    while True:
        command = input("Enter command (encrypt/decrypt/history/exit): ").strip().lower()

        if command == 'exit':
            print("\n👋 Exiting... Goodbye!")
            break

        elif command == 'history':
            if not history:
                print("No history yet.")
            else:
                print("\n🔁 Session History:")
                for entry in history:
                    print(f"  - [{entry['mode']}] '{entry['input']}' → '{entry['output']}' (shift: {entry['shift']})")
            print()

        elif command in ['encrypt', 'decrypt']:
            text = input("Enter your message: ")

            try:
                shift = int(input("Enter shift value (positive integer): "))
                if shift < 0:
                    raise ValueError
            except ValueError:
                print("❌ Invalid shift! Please enter a positive integer.\n")
                continue

            result = caesar_cipher(text, shift, mode=command)
            print(f"\n✅ Your {command}ed message: {result}\n")

            # Save to history
            history.append({
                'mode': command,
                'input': text,
                'output': result,
                'shift': shift
            })

        else:
            print("❌ Unknown command. Please try again.\n")

if __name__ == "__main__":
    main()
