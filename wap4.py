#4. Build a BMI calculator. Take height (cm) and weight (kg) as input, compute BMI, and print the category (Underweight / Normal / Overweight / Obese) with a formatted health message.
hgt = input("Enter your height in cm: ")
wgt = input("Enter your weight in kg: ")
BMI = float(wgt) / (float(hgt)/100)**2
if(BMI < 18.5):
    print(f"Your BMI is {BMI:.2f}, you are underweight. Try to eat more nutritious food and exercise regularly.")
elif(BMI >= 18.5 and BMI < 25):
    print(f"Your BMI is {BMI:.2f}, you are normal weight. Keep up the good work and maintain a healthy lifestyle.")
elif(BMI >= 25 and BMI < 30):
    print(f"Your BMI is {BMI:.2f}, you are overweight. Try to eat a balanced diet and exercise regularly to maintain a healthy weight.")
elif(BMI >= 30):
    print(f"Your BMI is {BMI:.2f}, you are obese. It is important to consult with a healthcare professional to develop a plan for weight loss and improving your overall health.")
