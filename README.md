# 单词搜索工具

一个为英语学习者设计的灵活高效的单词搜索和词汇学习工具。使用 Python 构建，支持基于正则表达式的单词匹配、发音模式发现和基于频率的筛选。

---

## ✨ 功能

- ⛏️ **正则表达式模式匹配**：使用模式如 `.ail` 或 `con....` 搜索相关词汇。
- 🔍 **发音支持**：显示国际音标（英式英语），帮助识别发音模式。
- 🔢 **频率筛选**：使用 BNC 和 COCA 语料库数据筛选高频词汇。
- 🔹 **考试标签**：识别单词是否标记为 GRE、IELTS 等考试词汇。
- 🕁️ **并列词组**：轻松比较最小对立对或词族（例如 *slap*, *slip*, *slop*）。
- 🌍 **英英释义**：所有释义均为单语，鼓励沉浸式学习。
- 🌟 **丰富输出**：使用 `rich` 库以整洁、多彩的表格形式呈现搜索结果。

---

## 🔹 演示截图

### 1. 部分拼写匹配
使用占位符（`.` 或空格）发现相关单词。
![partial](https://github.com/user-attachments/assets/b4378e07-8376-474b-b920-04ce8f508294)

### 2. 发音模式分析
按起始模式和元音变化可视化单词组。
![pattern](https://github.com/user-attachments/assets/e4402d0c-457a-4cc7-a4bd-87c77a2f5ea6)

### 3. 元音比较（最小对立对）
将单词如 `slap/slip/slop` 分组以观察元音变化。
![minimal](https://github.com/user-attachments/assets/1d00653f-be1b-4bee-9985-b3b1c2148ee5)

---

## 📊 数据来源

该项目使用 [ecdict](https://github.com/skywind3000/ecdict) 数据集，这是一个免费的开源英汉词典，采用 CSV 格式。它包括：

- 单词拼写和英式国际音标
- 释义和考试标签（GRE、IELTS 等）
- 来自 BNC 和 COCA 的词频数据

> 本项目尊重 ECDICT 原始 MIT 许可证。

---

## 📦 安装

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/word-search-tool.git
cd word-search-tool
```

### 2. 安装依赖
```bash
pip install pandas rich
```

### 3. 下载并放置词典数据  
从以下地址下载 `ecdict.csv`：  
🔗 [ecdict.csv 下载地址](https://github.com/skywind3000/ECDICT/blob/master/ecdict.csv)  

将文件放置在项目根目录。

---

## 🚀 使用

运行脚本并输入模式进行搜索：
```bash
python word_search.py
```
然后输入模式，如：
```
con....
.ail
sl.p
```
你将看到一个包含匹配单词及其音标、释义、标签和频率的彩色表格。

---

## 📍 许可证

本项目使用 MIT 许可证。
感谢 [skywind3000](https://github.com/skywind3000) 提供 ECDICT 数据集。

---

## 🙏 致谢

- [ecdict](https://github.com/skywind3000/ecdict) 提供的词典数据
- [Rich](https://github.com/Textualize/rich) 提供的输出增强

---

祝你单词搜索愉快！🤖
```
