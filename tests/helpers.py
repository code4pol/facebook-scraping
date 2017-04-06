def get_credentials():
    # Crie um arquivo chamado credentials.txt na raiz do projeto
    # contendo, na primeira linha, seu usuario e senha do facebook
    # separados por :
    # Exemplo:
    # joao@gmail.com:n1ngu3msab3minhasenh4
    #
    credentials_file = open('../credentials.txt')
    credentials = credentials_file.readline()
    return credentials.split(':')