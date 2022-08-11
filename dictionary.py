dictionary = {
  "book" : "kitap",
  "table": "masa",
  "key" : "anahtar"

}

dictionary2 = dict(kitap = "book",masa = "table",kalem = "pencil")

print(dictionary2)
del(dictionary["book"])

print(dictionary)
dictionary["pencil"] = "kalem"

print(dictionary)

print(dictionary["table"])