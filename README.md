# Detectar-BruteForce
Script em Python para análise de logs de autenticação, detectando tentativas de brute force por IP. Gera relatórios com alertas e histórico, ajudando na identificação de acessos suspeitos em ambientes de segurança.

## 🚀 Como usar

1. Clone o repositório:
```bash
git clone https://github.com/Dorane-Antunes/Detectar-BruteForce.git
cd projeto-bruteforce
```
2. Execute o script passando o arquivo de log como argumento:
 ```bash
 python scripts/detectar-bruteforce.py logs/auth.log [limite]
 ```
 - Limite de falhas para identificar BruteForce, por padrão 3.
   
## Estrutura do Projeto
```bash
Projeto-BruteForce/
├── logs/                # Arquivos de log (ex.: auth.log)
├── reports/             # Relatórios gerados (relatorio_bruteforce.txt)
├── scripts/             # Código-fonte (detectar-bruteforce.py)
└── .gitignore           # Arquivos ignorados pelo Git
```

## Exemplo de saída
```bash
=== Relatório de Tentativas de Login Suspeitas ===
[ALERTA] IP 192.168.0.10 teve 5 tentativas falhas.
IP 192.168.0.20 teve 2 tentativas falhas.
[INFO] Script executado em 2026-08-17 17:50:00
```

## Requisitos
- Python 3
- Permissão de leitura nos arquivos de log
