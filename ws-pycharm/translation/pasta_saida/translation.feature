Feature Validação do Login do Usuário

Scenario Outline Verificação de login com credencial válida e credencial inválida

    Given que o usuário está na página de login

    When o usuário insere as credenciais "<username>" e "<password>"

    Then o usuário deve ver a mensagem "<message>"

nan

    Examples:

      | username | password                             | Teste

      | tomsmith | SuperSecretPassword!   | Teste

      | tomsmith | pass456                                 | Teste

      | tomsmith |                                                  | Teste

