text = "Hello welcome to Cathay 60th year anniversary"

# 將所有字母轉為小寫
text = text.lower()

# 初始化一個空字典來存放字母和數字的出現次數
char_counts = {}

# 遍歷每個字元
for char in text:
    # 檢查是否為字母或數字
    if char.isalnum():
        # 將字元添加到字典中，如果已存在則增加計數
        char_counts[char] = char_counts.get(char, 0) + 1

# 取得字元及其出現次數的列表，按字元順序排序
sorted_counts = sorted(char_counts.items())

# 打印每個字元及其出現次數
for char, count in sorted_counts:
    print(f"{char} {count}")