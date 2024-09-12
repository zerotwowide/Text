
from Student_info.score import Score
from Student_info.Student import Student

# 储存学生信息
students = []

# 录入学生信息
def main():
    while True:
        # 录入信息
        stu_id = input("Enter Student ID: ")
        stu_name = input("Enter Student Name: ")
        stu_sex = input("Enter Student Sex: ")
        stu_project = input("Enter Student Project: ")
        stu_score = input("Enter Student Score: ")
        score = Score(stu_project, stu_score)

        # 记录信息
        student = Student(stu_id, stu_name, stu_sex, score)
        students.append(student)

        # 打印信息
        count = 0
        for i in students:
            count += 1
            print(f"student {count} , id: {i.id}, name: {i.name}, "
                  f"sex: {i.sex}, project and score: {i.score.project, i.score.score}")

        # 判断是否退出录入
        judgment = input("Do you want to continue?(True/False): ")
        if judgment == "True":
            continue
        elif judgment == "False":
            break
        else:
            print("输入错误，结束录入")
            break

# 打印所有学生信息
def print_stu():
    count = 0
    for i in students:
        count += 1
        print(f"student {count} , id: {i.id}, name: {i.name}, "
              f"sex: {i.sex}, project and score: {i.score.project, i.score.score}")

if __name__ == '__main__':
    main()
    print_stu()