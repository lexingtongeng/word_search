# Word Search Tool

这是一个基于 Python 的单词匹配和筛选工具，支持正则表达式模式匹配和高频词过滤，帮助用户更高效地记忆和学习单词。

---

## 演示

### 示例 1：形近单词记忆
用户输入时用` `或者 `.`（空格或者英文句点） 表示不确定的字母（如 `.ail`），回车即可检索出高频单词的音标、英英释义、标签（如 GRE、IELTS 等）、英国国家语料库（BNC）和当代语料库（FRQ）。

![形近单词演示](https://github.com/user-attachments/assets/b4378e07-8376-474b-b920-04ce8f508294)

### 示例 2：比较发音规律
此脚本支持多个位置挖空。例如，输入 `con....`，返回 54 个匹配单词，并展示其发音规律（如 `/kɒn/` 和 `/kәn/`）。

![发音规律演示](https://github.com/user-attachments/assets/e4402d0c-457a-4cc7-a4bd-87c77a2f5ea6)

---

## 数据来源

本项目使用的 `ecdict.csv` 文件来自以下开源项目：[ecdict](https://github.com/skywind3000/ecdict)。  
该项目遵循 MIT License，感谢原作者的贡献。

---

## 数据文件

本项目需要使用 `ecdict.csv` 文件，该文件可以从以下链接下载：  
[ecdict.csv 下载链接](https://github.com/skywind3000/ECDICT/blob/master/ecdict.csv)

下载后，请将文件放置在项目根目录下。

---

## 功能

- 支持正则表达式模式匹配，灵活检索单词。
- 按词频过滤单词，聚焦高频词汇。
- 使用 Rich 库以表格形式美观地展示结果。

---

## 依赖

运行此项目需要以下 Python 库：
- `pandas`
- `rich`

---

## 使用方法

1. 确保 `ecdict.csv` 文件与脚本位于同一目录。
2. 安装依赖：
   ```bash
   pip install pandas rich
