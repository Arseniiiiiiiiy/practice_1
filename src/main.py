import json
import argparse
import os

def load_vfs(path):
    """Загрузить VFS в память."""
    if not os.path.isdir(path):
        print("Ошибка загрузки VFS")
        return {}

    data = {}

    for root, dirs, files in os.walk(path):
        data[root] = {"dirs": dirs, "files": {}}

        for name in files:
            file_path = os.path.join(root, name)

            try:
                file = open(file_path, encoding="utf-8")
                data[root]["files"][name] = file.read()
                file.close()
            except:
                print("Ошибка загрузки файла:", name)

    return data

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
VFS_NAME = "VFS"


def parse(s):
    """Разделить строку на команду и аргументы."""
    parts = s.split()

    if not parts:
        return None, []

    return parts[0], parts[1:]


def execute_command(command, arguments):
    """Выполнить команду эмулятора."""
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
    """Запустить эмулятор."""
    print("Эмулятор UNIX shell")
    print("Для выхода используйте команду exit")

    vfs_data = {}

    if vfs:
        vfs_data = load_vfs(vfs)
    if vfs_data:
        print("VFS загружена")

    if script:
        try:
            file = open(script, encoding="utf-8")

            for s in file:
                s = s.strip()

                if s:
                    print(f"{VFS_NAME}:~$ {s}")
                    command, arguments = parse(s)
                    execute_command(command, arguments)

            file.close()
        except:
            print("Ошибка выполнения стартового скрипта")

    running = True

    while running:
        s = input(f"{VFS_NAME}:~$ ")

        command, arguments = parse(s)

        if command is None:
            continue

        running = execute_command(command, arguments)


if __name__ == "__main__":
    main()