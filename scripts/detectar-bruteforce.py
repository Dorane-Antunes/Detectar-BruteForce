# Acesso a argumentos passados pela linha de comando (ex.: nome do arquivo de log).
import sys
from collections import Counter
# Classe Counter, contagem de quantas vezes cada elemento aparece em uma lista.
import re  # Adiciona o módulo de regex.
import os  # Biblioteca Python para interagir com o sistema operacional.
from datetime import datetime

# log_file, caminho do arquivo de log, threshold tentativas falhas para se considerar bruteforce


def detectar_bruteforce(log_file, threshold=3, reports_dir="reports"):
    try:
     # Abre o arquivo de log e lê todas as linhas
        with open(log_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Arquivo {log_file} não encontrado.")
        return

    lista_de_falhas = []
    for line in lines:
        if "Failed password" in line:
            # Captura IPv4 ou IPv6
            match = re.search(r'from ([0-9a-fA-F\.:]+)', line)
            if match:
                ip = match.group(1)
                lista_de_falhas.append(ip)

    counts = Counter(lista_de_falhas)

    if not counts:
        print("Nenhuma tentativa suspeita encontrada.")
    else:
        for ip, num in counts.items():
            if num >= threshold:
                print(f"[ALERTA] IP {ip} teve {num} tentativas falhas.")
            else:
                print(f"IP {ip} teve {num} tentativas falhas.")

# Gera o relatório em texto
    reports_lines = ["\n === Relatório de Tentativas de Login Suspeitas ==="]
    if not counts:
        reports_lines.append("Nenhuma tentativa suspeita encontrada.")
    else:
        for ip, num in counts.items():
            if num >= threshold:
                reports_lines.append(
                    f"[ALERTA] IP {ip} teve {num} tentativas falhas.")
                reports_lines.append(f"IP {ip} teve {num} tentativas falhas.")
                # Adiciona informação de execução ao relatório
                reports_lines.append(
                    f"[INFO] Script executado em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# Salva em arquivo dentro de /reports
    os.makedirs(reports_dir, exist_ok=True)
    reports_file = os.path.join(reports_dir, "relatorio_bruteforce.txt")
    with open(reports_file, "a", encoding="utf-8") as f:
        f.write("\n".join(reports_lines))
    print(f"\nRelatório salvo em: {reports_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python detectar_bruteforce.py em arquivo")
        sys.exit(1)

    log_file = sys.argv[1]
    threshold = int(sys.argv[2]) if len(sys.argv) == 3 else 3
    detectar_bruteforce(log_file, threshold)
