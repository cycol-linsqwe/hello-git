def greet(name: str) -> str:
    return f"你好，{name}！这是我第一个 Git 仓库。"


def farewell(name: str) -> str:
    return f"再见，{name}！记得提交代码。"


if __name__ == "__main__":
    print(greet("世界"))
    print(farewell("世界"))
