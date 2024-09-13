class Score:
    project = None
    score = None
    # 构造函数
    def __init__(self, project, score):
        self.project = project
        self.score = score

if __name__ == "__main__":
    score = Score("math",89)

