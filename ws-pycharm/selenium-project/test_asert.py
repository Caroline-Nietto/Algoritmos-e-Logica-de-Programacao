

# assert numbers
# num_esperado = 3
# num_obtido = 2

# assert num_esperado > num_obtido, f"Esperado {num_esperado}. Atual {num_obtido}."

# assert text
# text_esperado = "Selenium"
# text_obtido = "selenium"
#
# assert text_esperado.lower() == text_obtido.lower(), f"Esperado: {text_esperado} Atual: {text_obtido} "

# assert text in string
text_esperado = "Seleniumz"
text_obtido = "Selenium WebDriver"

assert text_esperado not in text_obtido, f"Esperado: '{text_esperado}'  não está dentro da string Atual: '{text_obtido}' "


# assert is_displayed/is-enabled/is_selected
