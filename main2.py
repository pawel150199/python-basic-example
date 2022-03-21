import lab2

if __name__ == "__main__":
    # generowanie hasła
    pas = lab2.Password()
    print(f"Wygenerowane hasło: {pas.generate()}")

    # tworzenie miniaturki
    mi = lab2.Min("image.jpeg", 300, 300, "watermarked")
    mi.miniaturizing()

    # tworzenie kopii zapasowej
    lab2.zipping("name1", "name2")

    # dzielenie PDF
    lab2.divided("xd.pdf", 100)

    # tworzenie znaku wodnego
    lab2.watermark("image.jpeg", "image.jpeg", (128,128), (200, 200), 256)

    #jakies dodawanko
    lab2.matematica('8767+346')
    lab2.matematica('435346-3432')
    lab2.matematica('45*35')
