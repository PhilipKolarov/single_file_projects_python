def grade_judge(score):
    grade_info = []

    if score >= 92:
        grade_info.append(6)
        grade_info.append('Excellent')
    elif score >= 81:
        grade_info.append(5)
        grade_info.append('Very Good')
    elif score >= 71:
        grade_info.append(4)
        grade_info.append('Good')
    elif score >= 60:
        grade_info.append(3)
        grade_info.append('Average')
    elif 0 <= score < 60:
        grade_info.append(2)
        grade_info.append('Poor')
    return grade_info


my_score = int(input())
my_grade_as_num, my_grade_as_word = grade_judge(my_score)
print(my_grade_as_num)
print(my_grade_as_word)