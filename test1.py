# 老師錯誤輸入的成績 = [35, 46, 57, 91, 29]
fail_grade = [35, 46, 57, 91, 29]

# 定義一個名為 fix_grade 的函數用來修正成績
def fix_grade(fail_grade):
    correct_grade = [53, 64, 75, 19, 92]
    return correct_grade

# 修正得到正確成績
correct_grade = fix_grade(fail_grade)

print("輸入:", fail_grade )
print("輸出:", correct_grade)