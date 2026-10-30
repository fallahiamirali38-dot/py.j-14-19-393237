




ghad=float(input("ghad khod ra be m vared koned:"))

vazen=float(input("vazen khod ra be kg vared koned:"))

bmi=vazen/(ghad**2)

if 18.5>=bmi:
    print("kambod vazen")

elif 18.5<bmi<25:
    print("vazen monaseb")

elif 25<=bmi<=30:
    print("shma ezafe vazn dared")

elif bmi>30:
    print("shma khagh hasted")