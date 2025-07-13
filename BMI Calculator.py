height = float(input("enter your height in meters: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/height**2
bmi_round_off= round(bmi,1)

if bmi_round_off < 18.5:
 print(f"Your BMI is {bmi_round_off}, you are underweight.")
elif bmi_round_off < 25:
 print(f"Your BMI is {bmi_round_off}, you have a normal weight.")
elif bmi_round_off < 30:
 print(f"Your BMI is {bmi_round_off}, you are slightly overweight.")
elif bmi_round_off < 35:
  print(f"Your BMI is {bmi_round_off}, you are obese.")
else:
 print(f"Your BMI is {bmi_round_off}, you are clinically obese.")
