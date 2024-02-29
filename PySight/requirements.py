import pkg_resources

def create_requirements_file(file_path='requirements.txt'):
    # Obtém todos os pacotes instalados
    installed_packages = pkg_resources.working_set

    # Lista de pacotes no formato 'pacote==versão'
    packages_list = [f"{pkg.project_name}=={pkg.version}" for pkg in installed_packages]

    # Escreve a lista de pacotes no arquivo requirements.txt
    with open(file_path, 'w') as file:
        file.write('\n'.join(packages_list))

if __name__ == "__main__":
    create_requirements_file()
    print("Arquivo requirements.txt criado com sucesso.")
