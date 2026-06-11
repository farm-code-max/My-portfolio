weight = float(input("กรอกน้ำหนักของคุณ (กิโลกรัม): "))
height_cm = float(input("กรอกส่วนสูงของคุณ (เซนติเมตร): "))

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print(f"\nค่า BMI ของคุณคือ: {bmi:.2f}")


if bmi < 18.5:
    print("เกณฑ์รูปร่าง: น้ำหนักน้อย/ผอม")
elif bmi < 23:
    print("เกณฑ์รูปร่าง: ปกติ/สมส่วน")
elif bmi < 25:
    print("เกณฑ์รูปร่าง: น้ำหนักเกิน")
elif bmi < 30:
    print("เกณฑ์รูปร่าง: โรคอ้วนระดับ 1")
else:
    print("เกณฑ์รูปร่าง: โรคอ้วนระดับ 2/ขั้นรุนแรง")