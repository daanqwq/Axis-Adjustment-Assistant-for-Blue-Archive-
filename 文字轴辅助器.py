import pyperclip
import os

def print_preview(inputs):
    preview = []
    i = 0
    while i < len(inputs):
        if inputs[i] == '—'*10:
            preview.append('—'*10)
            i += 1
        else:
            if i+1 < len(inputs) and inputs[i+1] != '—'*10:
                preview.append(f"{inputs[i]}C -> {inputs[i+1]}")
                i += 2
            else:
                preview.append(f"{inputs[i]}C -> ")
                i += 1
    return preview

inputs = []

try:
    while True:
        os.system('cls')  # 清空屏幕
        
        # 显示当前预览
        preview = print_preview(inputs)
        print("当前预览：")
        for line in preview:
            print(line)
        print("\n" + "="*30)
        
        # 计算有效输入数量（排除分隔线）
        effective_length = len([x for x in inputs if x != '—'*10])
        next_num = effective_length + 1
        prompt = "请输入费用" if next_num % 2 == 1 else "请输入操作"
        
        # 获取输入
        user_input = input(f"{prompt}（直接回车结束输入，输入--以生成分割线）: ").strip()
        
        # 结束输入条件
        if not user_input:
            break
            
        # 处理特殊输入
        if user_input == "--":
            inputs.append('—'*10)
        else:
            inputs.append(user_input)

except KeyboardInterrupt:
    pass

# 生成最终输出
os.system('cls')
print("最终结果(已复制)：\n")
output_lines = []
i = 0
while i < len(inputs):
    current = inputs[i]
    if current == '—'*10:
        output_lines.append(current)
        i += 1
    else:
        if i + 1 < len(inputs) and inputs[i+1] != '—'*10:
            output_lines.append(f"{current}C -> {inputs[i+1]}")
            i += 2
        else:
            output_lines.append(f"{current}C -> ")
            i += 1

output = '\n'.join(output_lines)
print(output)
pyperclip.copy(output)
