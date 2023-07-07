def find_longest_line(file_path):
    try:
        with open(file_path, 'r') as file:
            longest_line = ''
            for line in file:
                line = line.rstrip('\n')
                if len(line) > len(longest_line):
                    longest_line = line
            if longest_line:
                print(f"Liniile din fișierul {file_path}:\n{longest_line}")
            else:
                print("Fișierul este gol.")
    except FileNotFoundError:
        print(f"Fisierul {file_path} nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare la citirea fișierului: {str(e)}")

# Exemplu de utilizare
file_path = input("Introduceți calea către fișierul textual(/Users/parasiir08/Downloads/large_text_file.txt): ")
find_longest_line(file_path)
