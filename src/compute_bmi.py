def compute_bmi(weight, height):
    """
    Calcule l'IMC
    weight en kg
    height en mètres
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Values must be positive")

    bmi = weight / (height * height)

    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "healthy"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"
