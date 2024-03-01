import pkg_resources
import subprocess

def create_requirements_file(file_path='requirements.txt'):
    # Obtém todos os pacotes instalados
    installed_packages = pkg_resources.working_set

    # Lista de pacotes no formato 'pacote==versão'
    packages_list = [f"{pkg.project_name}=={pkg.version}" for pkg in installed_packages]

    # Escreve a lista de pacotes no arquivo requirements.txt
    with open(file_path, 'w') as file:
        file.write('\n'.join(packages_list))

def install_missing_packages(file_path='requirements.txt'):
    try:
        # Lê os pacotes do arquivo requirements.txt
        with open(file_path, 'r') as file:
            requirements = file.read().splitlines()

        # Filtra os pacotes já instalados
        installed_packages = [pkg.key for pkg in pkg_resources.working_set]
        missing_packages = [req for req in requirements if req.split('==')[0] not in installed_packages]

        # Pergunta ao usuário se deseja instalar os pacotes ausentes
        if missing_packages:
            print("Pacotes ausentes:")
            for pkg in missing_packages:
                print(pkg)

            resposta = input("Deseja instalar os pacotes ausentes? (s/n): ").lower()

            if resposta == 's':
                # Chama a função para instalar os pacotes
                install_packages(missing_packages)
            else:
                print("Instalação cancelada.")

        else:
            print("Todos os pacotes já estão instalados.")

    except Exception as e:
        print(f"Erro ao instalar pacotes: {e}")

def install_packages(packages):
    try:
        # Instala os pacotes ausentes
        subprocess.check_call(['pip', 'install'] + packages)
        print("Pacotes instalados com sucesso.")
    except Exception as e:
        print(f"Erro ao instalar pacotes: {e}")

if __name__ == "__main__":
    create_requirements_file()
    install_missing_packages()
    print("Arquivo requirements.txt criado e pacotes instalados conforme necessário.")
