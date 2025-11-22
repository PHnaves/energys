from style.colors import CYAN, GREEN, RED, RESET, YELLOW

def validation_cpf():
    while True:
        cpf = input(CYAN + "Digite o CPF (somente números): " + RESET)

        if len(cpf) != 11 or not cpf.isdigit():
            print(f"{YELLOW}CPF {cpf} inválido! Deve ter 11 dígitos numéricos.{RESET}")
            continue

        if cpf == cpf[0] * 11:
            print(f"{YELLOW}CPF inválido (todos os dígitos iguais).{RESET}")
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
            print(f"{GREEN}CPF válido!{RESET}")
            return cpf
        else:
            print(f"{RED}CPF inválido!{RESET}")
            continue
