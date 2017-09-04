### Conditionals, braces are optional:

gpa = 5.0
if 4 < gpa < 4.5:
    skill = 'good'
elif gpa >= 4.5:
    skill = 'excellent'
else:
    skill = 'bad'

print(skill)

if 1 == 1 and 2 + 2 == 4:
    print('Math works!')


## ternary
max_score = 1
score = 0.51
result = 'pass' if score > (0.5 * max_score) else 'fail'

print(result)
