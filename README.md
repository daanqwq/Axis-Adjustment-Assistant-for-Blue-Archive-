# 蔚蓝档案文字轴辅助器

一个用于处理交替费用/操作输入的命令行工具，支持实时预览和格式化输出。

### 功能特性
- 智能交替提示（费用↔操作）
- 输入'--'生成分隔线`——————————`
- 清屏实时预览当前进度
- 结果自动复制到剪贴板
- 支持未完成项处理（如单独费用输入）

### 使用方式
1. 按提示交替输入费用/操作
2. 输入'--'插入分隔线
3. 直接回车结束输入
4. 自动生成格式：
   ```
   aaC -> bb
   ——————————
   ccC -> dd
   ```

### 运行要求
```bash
pip install pyperclip
```
*Windows用户建议以管理员身份运行CMD/PowerShell*

### 输入示例
```
[费用] 2
[操作] 锅
[费用] --
[操作] 5
[回车结束]

输出：
最终结果(已复制)：
2C -> 锅
——————————
5C -> 
```
