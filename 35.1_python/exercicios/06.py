def triangle_type(side1, side2, side3):
    IS_TRIANGLE = False
    tgl_type = ""
    
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
      
        IS_TRIANGLE = True
      
    if IS_TRIANGLE:
        if side1 == side2 and side2 == side3:
            tgl_type = "Equilátero"
            print("Triângulo {0}: três lados iguais".format(tgl_type))
        elif side1 == side2 or side2 == side3:
            tgl_type = "Isósceles"
            print("Triângulo {0}: quaisquer dois lados iguais".format(tgl_type))
        elif side1 != side2 and side2 != side3:
            tgl_type = "Escaleno"
            print("Triângulo {0}: três lados diferentes".format(tgl_type))
        return IS_TRIANGLE

# triangle_type(21, 6, 10)

triangle_type(8, 6, 3)
      
