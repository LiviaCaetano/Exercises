import sqlite3

def create_database():
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            imc REAL NOT NULL,
            classificacao TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 35:
        classificacao = "Obesidade grau I"
    elif 35 <= imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return round(imc, 2), classificacao

def salvar_paciente(nome, peso, altura, imc, classificacao):
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pacientes(nome, peso, altura, imc, classificacao)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, peso, altura, imc, classificacao))

    conn.commit()
    conn.close()

def listar_pacientes():
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes")
    registros = cursor.fetchall()

    conn.close()
    return registros

def menu():
    create_database()

    while True:
        print("\n===== SISTEMA DE IMC =====")
        print("1 - Calcular IMC e salvar")
        print("2 - Listar cálculos realizados")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))

            imc, classificacao = calcular_imc(peso, altura)
            salvar_paciente(nome, peso, altura, imc, classificacao)

            print(f"\nIMC: {imc}")
            print(f"Classificação: {classificacao}")
            print("Registro salvo com sucesso!")

        elif opcao == "2":
            pacientes = listar_pacientes()
            print("\n===== HISTÓRICO DE PACIENTES =====")
            for p in pacientes:
                print(f"ID: {p[0]} | Nome: {p[1]} | Peso: {p[2]} | Altura: {p[3]} | IMC: {p[4]} | Classificação: {p[5]}")
        
        elif opcao == "3":
            print("Encerrando...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
