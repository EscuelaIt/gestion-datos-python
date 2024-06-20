graphic = open("graphic.csv", "w")

for i in range(-10, 10):
    for j in range(-10, 10):
        graphic.write(str((i ** 2 - j ** 2)) + ",")
    graphic.write("\n")

graphic.close()
