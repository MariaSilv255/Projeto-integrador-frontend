## Estrutura do Projeto'

```text
lib/
├── features/                 # Módulos baseados em funcionalidades
│   ├── auth/                 # Tudo sobre Autenticação
│   │   ├── data/             # Chamada de API, persistência de Token
│   │   ├── domain/           # Regras de negócio e entidades
│   │   └── presentation/     # Telas e Widgets de Login/Cadastro
│   ├── home/                 # Funcionalidades da tela principal
│   └── splash/               # Tela de carregamento inicial
├── main.dart                 # Ponto de entrada do aplicativo
├── tela_login.dart           # Tela de Login
├── tela_cadastro.dart        # Tela de Cadastro
├── tela_principal.dart       # Tela Principal
├── tela_recuperar_senha.dart # Tela de Recuperação de Senha
└── dashBoard.dart            # Dashboard de monitoramento
```

