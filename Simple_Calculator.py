print(20*"=")
print("KALKULATOR SEDERHANA")
print(20*"=" + "\n")
while True:
  angka_1 = float(input("masukkan angka pertama = "))
  operator = input("operator ( +, -, x, / ) : ")
  angka_2 = float(input("masukkan angka kedua = "))

# percabangan

  if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil} \n")
  elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil} \n")
  elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil} \n")
  elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil} \n")
  else:
    print("Harap masukkan operator dengan benar!")