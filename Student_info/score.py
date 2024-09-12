class Score:
    project = None
    score = None
    # 构造函数
    def __init__(self, project, score):
        self.project = project
        self.score = score

    def print_score(self):
        print(f"student project : {self.project},score is {self.score}")

if __name__ == "__main__":
    score = Score("math",89)
    score.print_score()
