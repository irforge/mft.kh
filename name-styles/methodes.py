tst = "  salam MAN ali HASTAM  "

print(tst.upper()) 
print(tst.lower())
print(tst.title())
print(tst.capitalize())
print("------------------")
print("|" + tst.strip() + "|")
print("|" + tst.lstrip() + "|")
print("|" + tst.rstrip() + "|")
print("------------------")
print(tst.replace("ali", "radmehr"))
print(tst.split())
x = tst.lower().split()
print(x)
print(len(x))
print("-".join(tst))
print("------------------")


history = "salam man ali hastam man ashegh cs hastam    "
print(history.strip().count(" ")+ 1)

print(history.startswith("sa"))
print(history.strip().endswith("hastam"))
print("ashegh" in history)
print(tst.strip().find("salam"))

print("1324".isdigit())
print("salam".isalpha())
print("19salar".isalpha())












