Feature Valida��o do Login do Usu�rio

Scenario Outline Verifica��o de login com credencial v�lida e credencial inv�lida

    Given que o usu�rio est� na p�gina de login

    When o usu�rio insere as credenciais "<username>" e "<password>"

    Then o usu�rio deve ver a mensagem "<message>"

nan

    Examples:

      | username | password                             | Teste

      | tomsmith | SuperSecretPassword!   | Teste

      | tomsmith | pass456                                 | Teste

      | tomsmith |                                                  | Teste

