def validation_cpf():
    while True:
        cpf = input("Digite o CPF (somente números): ")

        if len(cpf) != 11 or not cpf.isdigit():
            print(f"CPF {cpf} inválido! Deve ter 11 dígitos numéricos.\n")
            continue

        if cpf == cpf[0] * 11:
            print("CPF inválido (todos os dígitos iguais).\n")
            continue

        digits = [int(d) for d in cpf]

        sum1 = sum(digits[i] * (10 - i) for i in range(9))
        remainder1 = (sum1 * 10) % 11
        if remainder1 == 10:
            remainder1 = 0

        sum2 = sum(digits[i] * (11 - i) for i in range(10))
        remainder2 = (sum2 * 10) % 11
        if remainder2 == 10:
            remainder2 = 0

        if remainder1 == digits[9] and remainder2 == digits[10]:
            print(f"CPF {cpf} válido!\n")
            return cpf
        else:
            print(f"CPF {cpf} inválido!\n")
            continue
