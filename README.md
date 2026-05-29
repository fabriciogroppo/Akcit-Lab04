# Gerador de Senhas

Projeto simples em Python 2.7 para gerar senhas aleatórias e seguras com base em critérios configuráveis.

## Estrutura do Projeto

- `main.py` - ponto de entrada do aplicativo CLI.
- `config/settings.py` - classe `Settings` que lê as definições de senha do arquivo `.env`.
- `services/password_service.py` - implementação da lógica de geração de senha.
- `password_generator.py` - wrapper que reexporta `generate_password` para compatibilidade.
- `test_password_generator.py` - testes unitários para validação da geração de senha.
- `.env` - configurações padrão de geração de senha.
- `.gitignore` - arquivos e pastas ignorados pelo Git.

## Configuração

O projeto usa o arquivo `.env` na raiz para definir os critérios padrão:

```text
PASSWORD_LENGTH=16
USE_DIGITS=True
USE_LOWER=True
USE_UPPER=True
USE_SYMBOLS=False
```

### Exemplo de valores

- `PASSWORD_LENGTH` - tamanho padrão da senha.
- `USE_DIGITS` - inclui dígitos quando `True`.
- `USE_LOWER` - inclui letras minúsculas quando `True`.
- `USE_UPPER` - inclui letras maiúsculas quando `True`.
- `USE_SYMBOLS` - inclui símbolos de pontuação quando `True`.

## Uso

Execute o gerador de senha pelo terminal:

```bash
python main.py
```

Opções de linha de comando:

- `-l`, `--length` - tamanho da senha.
- `-n`, `--no-digits` - exclui dígitos.
- `-L`, `--no-lower` - exclui letras minúsculas.
- `-U`, `--no-upper` - exclui letras maiúsculas.
- `-s`, `--symbols` - inclui símbolos.

### Exemplos

Gerar senha padrão:

```bash
python main.py
```

Gerar senha de 24 caracteres com símbolos:

```bash
python main.py -l 24 -s
```

Gerar senha sem dígitos e sem letras minúsculas:

```bash
python main.py -n -L
```

## Testes

Para executar os testes unitários:

```bash
python -m unittest test_password_generator
```

## Observações

Este projeto foi desenvolvido para Python 2.7 e usa apenas bibliotecas padrão da linguagem.
