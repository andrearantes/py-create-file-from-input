def main() -> None:
    name_base = input("Enter name of the file:")
    name_file = f"{name_base}.txt"
    content = []
    print("Enter the content (enter 'stop' for finish)")
    while True:
        linha = input("Enter new line of content:")
        if linha == "stop":
            break
        content.append(linha)
    with open(name_file, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
