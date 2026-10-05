VFS="name"

def parse(s):
    parts = s.split()
    if not parts:
        return None, []

    a = parts[0]
    b = parts[1:]

    return a,b

def execute_command(command, arguments):

    if command == "ls":
        print("ls", arguments)

    elif command == "cd":
        print("cd", arguments)

    elif command == "exit":
        if arguments:
            print("Ошибка: exit не принимает аргументы")
        else:
            return False

    else:
        print(f"Ошибка: неизвестная команда '{command}'")

    return True

def main():
    print("Эмулятор UNIX shell")
    print("Для выхода используйте команду exit")

    running = True

    while running:
        s = input(f"{VFS}> ")

        command, arguments = parse(s)

        if command is None:
            continue

        running = execute_command(command, arguments)

if __name__ == "__main__":
    main()