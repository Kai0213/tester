def find_last_person(n):
    # Check if n is within the valid range (0-100)
    if not (0 <= n <= 100):
        print("請輸入有效的 n 值 (0-100)。")
        return

    # 創建一個包含 n 人的列表，表示團康活動的人員
    people = list(range(1, n + 1))

    # 當列表中還有超過一個人時，繼續進行報數並移除報到 3 的人
    while len(people) > 1:
        # 進行報數，每次報到 3 的人退出圈子
        for _ in range(2):
            people.append(people.pop(0))

        # 移除報到 3 的人
        people.pop(0)

    # 返回最後留下的那位同事的順位
    return people[0]

# 接收使用者輸入 n 的值
n = int(input("n值(0-100): "))
result = find_last_person(n)

if result is not None:
    print(f"第 {result} 順位。")