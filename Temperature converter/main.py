
question = input('What are you converting?\nA) Celsius to Fahrenheit\nB) Fahrenheit to Celsius\n')

temp = int(input('What is the temperature\n'))

if question == 'A' or question == 'a':
    contemp = ((temp * 9/5) + 32)
    contemp = int(contemp)
    print(contemp)
elif question == 'B' or question == 'b':
    contemp = (temp - 32) * 5/9
    print(contemp)
else:
    print('Thats not an option')