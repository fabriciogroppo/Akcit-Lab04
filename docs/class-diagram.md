# Diagrama de Classes

```mermaid
classDiagram
    class Settings {
        +int length
        +bool use_digits
        +bool use_lower
        +bool use_upper
        +bool use_symbols
        +__init__(env_path=None)
        +_load_env(env_path)
        +_set_option(name, value)
        +_parse_int(value, default)
        +_parse_bool(value, default)
    }

    class PasswordService {
        +generate_password(length, use_digits, use_lower, use_upper, use_symbols)
    }

    class Main {
        +parse_cli_args(settings)
        +main()
    }

    class PasswordGenerator {
        +generate_password(length, use_digits, use_lower, use_upper, use_symbols)
    }

    Settings <|-- Main : usa
    PasswordService <|-- PasswordGenerator : reexporta
    Main --> PasswordService : chama
