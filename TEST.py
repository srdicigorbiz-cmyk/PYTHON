import re

# ( \( )?       -> 1-es csoport: opcionális nyitó zárójel
# \d{2}         -> két számjegy (körzetszám)
# (?(1)\))      -> FELTÉTEL: Ha az 1-es csoport létezik (volt nyitó zárójel), AKKOR kell egy csukó zárójel ')' is!
# -\d{3}-\d{4}  -> a telefonszám többi része

pattern = r"(\()? \d{2} (?(1)\)) -\d{3}-\d{4}"

szoveg = """
(06) -123-4567   # Érvényes (van nyitó ÉS csukó)
06-123-4567      # Érvényes (nincs nyitó ÉS nincs csukó)
(06-123-4567     # HIBÁS! (van nyitó, de nincs csukó)
"""

print(re.findall(r"\(?\d{2}\)?-\d{3}-\d{4}", szoveg))