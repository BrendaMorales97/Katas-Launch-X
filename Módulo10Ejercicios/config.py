def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se encontro el archivo config.txt!")
    except PermissionError:
        print("Se encontro el archivo config.txt pero este directorio no contiene los permisos para leerse")


if __name__ == '__main__':
    main()