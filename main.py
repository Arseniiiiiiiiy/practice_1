import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--vfs")
parser.add_argument("--script")
parser.add_argument("--config")
args = parser.parse_args()

vfs = args.vfs
script = args.script

if args.config:
    try:
        file = open(args.config, encoding="utf-8")
        config = json.load(file)
        file.close()

        if "vfs" in config:
            vfs = config["vfs"]
        if "script" in config:
            script = config["script"]

    except:
        print("Ошибка чтения конфигурационного файла")

print("VFS:", vfs)
print("Стартовый скрипт:", script)
print("Конфигурационный файл:", args.config)
VFS = "VFS"


def parse(s):
    parts = s.split()

    if not parts:
        return None, []

    return parts[0], parts[1:]


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

    if script:
        try:
            file = open(script, encoding="utf-8")

            for s in file:
                s = s.strip()

                if s:
                    print(f"{VFS}:~$ {s}")
                    command, arguments = parse(s)
                    execute_command(command, arguments)

            file.close()
        except:
            print("Ошибка выполнения стартового скрипта")

    running = True

    while running:
        s = input(f"{VFS}:~$ ")

        command, arguments = parse(s)

        if command is None:
            continue

        running = execute_command(command, arguments)


if __name__ == "__main__":
    main()