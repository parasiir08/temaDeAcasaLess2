"""Utilizatorul va introduce un șir de caractere in consola.
* Calculați și afișați numarul total de litere în șirului de caractere
* Calculați și afișați numarul de vocale în șirul de caractere
* Calculați și afișați numarul de consoane în șirul de caractere

Note: Indiferent daca e majuscula sau minusucula litera

"""
sir = input("Introdu un sir de caractere ")
sir = sir.lower()
numar_total= len(sir)

print(f"Numarul total de litere este {numar_total}")
print("Litera a se repeta de", sir.count("a"))
print("Litera e se repeta de", sir.count("e"))
print("Litera i se repeta de", sir.count("i"))
print("Litera o se repeta de", sir.count("o"))
print("Litera u se repeta de", sir.count("u"))
print("Litera ă se repeta de", sir.count("ă"))
print("Litera î se repeta de", sir.count("î"))
print("Litera â se repeta de", sir.count("â"))

print("Litera b se repeta de", sir.count("b"))
print("Litera c se repeta de", sir.count("c"))
print("Litera d se repeta de", sir.count("d"))
print("Litera f se repeta de", sir.count("f"))
print("Litera h se repeta de", sir.count("h"))
print("Litera j se repeta de", sir.count("j"))
print("Litera k se repeta de", sir.count("k"))
print("Litera l se repeta de", sir.count("l"))
print("Litera m se repeta de", sir.count("m"))
print("Litera n se repeta de", sir.count("n"))
print("Litera p se repeta de", sir.count("p"))
print("Litera q se repeta de", sir.count("q"))
print("Litera r se repeta de", sir.count("r"))
print("Litera s se repeta de", sir.count("s"))
print("Litera ș se repeta de", sir.count("ș"))
print("Litera t se repeta de", sir.count("t"))
print("Litera ț se repeta de", sir.count("ț"))
print("Litera v se repeta de", sir.count("v"))
print("Litera w se repeta de", sir.count("w"))
print("Litera x se repeta de", sir.count("x"))
print("Litera z se repeta de", sir.count("z"))
print("Litera y se repeta de", sir.count("y"))
