def mark_brackets(lines):
    max_length = max(len(line) for line in lines)  # 确定最大行长度
    output_lines = []  # 存储输出结果的列表

    for line in lines:
        # 初始化标记行，全部填充为空格
        mark_line = ' ' * max_length
        stack = []  # 用于存储左括号位置的栈

        # 处理当前行的每个字符
        for i, char in enumerate(line):
            if char == '(':
                stack.append(i)  # 左括号入栈，存储其位置
            elif char == ')':
                if stack:
                    stack.pop()  # 弹出栈顶元素，表示匹配了一个左括号
                else:
                    # 没有匹配的左括号，将标记行的对应位置设置为'?'
                    mark_line = mark_line[:i] + '?' + mark_line[i + 1:]

                    # 检查栈中剩余的左括号，将其标记为'x'
        for pos in stack:
            mark_line = mark_line[:pos] + 'x' + mark_line[pos + 1:]

            # 对齐当前行和标记行，使其长度与最大行长度一致
        line = line.ljust(max_length)

        # 将输入行和标记行添加到输出列表中
        output_lines.append(line)
        output_lines.append(mark_line)

        # 打印输出结果
    for line in output_lines:
        print(line)

    # 从键盘读取输入，直到用户输入一个空行


user_input = []
while True:
    line = input("请输入一行文本（输入空行结束）: ")
    if line == '':
        break
    user_input.append(line)

# 调用函数并打印结果
mark_brackets(user_input)