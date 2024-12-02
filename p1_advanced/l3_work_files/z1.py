def write_file(filename: str, data: str):
    with open(filename, mode="w") as f:
        f.write(data)


def read_file(filename: str):
    with open(filename, mode="r") as f:
        print(f.read())


if __name__ == '__main__':
    filename = 'files/output.txt'
    user_data = input("Введите строку для хранения: ")
    write_file(filename, user_data)
    read_file(filename)
