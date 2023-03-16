# 학생들에게 최종 성적을 알려 주는 '학점 계산기'를 만들려고 합니다.

# 이 수업에는 50점 만점의 중간고사와 50점 만점의 기말고사가 있는데요. 두 시험의 점수를 합해서 최종 성적을 내는 방식입니다. 규칙은 다음과 같습니다.

# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만


def print_grade(midterm_score, final_score):
    
    total_score = midterm_score + final_score

    if total_score >= 90:
        print("A")
    elif total_score >= 80:
        print("B")
    elif total_score >= 70:
        print("C")
    elif total_score >= 60:
        print("D")
    else:
        print("F")
        
# 테스트 코드
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)