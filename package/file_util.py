

def print_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read())

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    finally:
        print("Done")

def append_file(file_path, content):
    try:
        with open(file_path, 'a') as f:
            f.write(content)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    finally:
        print("Done")

if __name__ == '__main__':
    print_file('../basic/test.txt')
    append_file('../basic/test.txt', 'hello world\n')