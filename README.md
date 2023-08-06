# Návod na spuštění a popis příloh
## Využití pásové struktury pro předzpracování dat při dekompozici binárních matic

Veškeré algoritmy zmíněné v textu práce jsou implementovány v jazyce Python za použítí knihoven NumPy a Matplotlib. Pro jejich spuštění je nutná instalace těchto knihoven pomocí příkazů:

```console
pip install numpy
python -m pip install -U pip
python -m pip install -U matplotlib
```
Nebo případně pomocí oficiálních návodů https://numpy.org/install/ a https://matplotlib.org/stable/users/installing/index.html. 

## Algoritmy
Soubory odpovídají názvu jednotlivých algoritmů zmíněných v textu práce. Kvůli náročnosti výpočtu bylo potřeba párkrát některé implementace optimalizovat. V příloze jsou zachovány i původní verze kvůli přihlednosti a lepšímu pochopení impelementace z pseudokódu. 

## Scripty pro spuštění experimentů
Pro generování výsledků této práce bylo vytvořeno několik skriptů. Jedná se o soubory: filters_picture_export.py, filters_script.py, coverage-graph-asso.py, coverage-graph.py, similarity_graph.py a similarity_table.py. 
Skripty, které generují obrázky jsou nachystány na to, aby obrázky ukládaly, ale pomocí zakomentovaného kódu v nich lze je i rovnou zobrazit. Ovšem pro zobrazení je třeba mít nainstalované některé z možných prostředí.

## Výsledky experimentů
Veškteré výstupní soubory této práce se nachází ve složce data uspořádané podle datasetu, metody pro získání pásové struktury a následně podle použitého filtru. Vždy se v příslušné složce nachází všechny vygenerované soubory a to včetně obrázkových. 

### Obrazová část výsledků
Aby bylo možné přehledně prohlížet obrázky vzniklé v této práci byla vytvořena jednoduchá webová stránka v jazyce php, která se nachází ve složce web. Pro spuštění stránky je za potřebí mít nainstalovaný lokální server například Apache
. Stránka se nachází také na adrese: 