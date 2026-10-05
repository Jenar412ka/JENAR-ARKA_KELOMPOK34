def cek_nilai (nilai):
  if nilai>=80:
    return "A"
  elif 40<nilai<80:
    return "B"
  else:
    return "C"


hasil_nilai = cek_nilai(80)
print(hasil_nilai)
