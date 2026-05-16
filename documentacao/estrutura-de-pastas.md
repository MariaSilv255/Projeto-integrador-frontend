## Estrutura do Projeto

```text
lib/
├── features/                 # Módulos baseados em funcionalidades
│   ├── auth/                 # Tudo sobre Autenticação
│   │   ├── data/             # Chamada de API, persistência de Token
│   │   ├── domain/           # Regras de negócio e entidades
│   │   └── presentation/     # Telas e Widgets de Login/Cadastro
│   │       ├── tela_cadastro.dart
│   │       ├── tela_login.dart
│   │       └── tela_recuperar_senha.dart
│   ├── home/                 # Funcionalidades da tela principal
│   │   ├── data/             # Acesso a dados (APIs, Local) da tela principal
│   │   ├── domain/           # Entidades e casos de uso
│   │   └── presentation/     # Telas e Widgets
│   │       └── tela_principal.dart
│   └── splash/               # Tela de carregamento inicial
│       ├── data/             # Acesso a dados da splash
│       ├── domain/           # Entidades e casos de uso
│       └── presentation/     # Telas e Widgets
├── main.dart                 # Ponto de entrada do aplicativo
```
