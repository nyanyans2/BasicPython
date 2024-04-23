text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text = text.replace(".","")
text = (text.replace(",",""))

split_text = text.split()
text = (split_text)
text2 = list(map(len,(text)))
text2 = list(map(str, text2))
# mapはそれぞれにって読みます
text3 = "".join(text2)
print(text3)