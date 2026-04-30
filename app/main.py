def main() -> None:
    name_base = input("policy")
    name_file = f"{name_base}.txt"
    content = []
    print("Digite o conteúdo (digite 'stop' para finalizar)")
    while True:
        linha = input("Digite a próxima linha do conteúdo:")
        if linha == "stop":
            break
        content.append(linha)
    with open(name_file, "w") as file:
        file.write("\n".join(content))

if __name__ == "__main__":
    main()
