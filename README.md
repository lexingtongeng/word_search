# Word Search Tool

这是一个基于 Python 的单词匹配和筛选工具，支持正则表达式模式匹配和高频词过滤。

## 数据来源
本项目使用的 `ecdict.csv` 文件来自以下开源项目：[ecdict](https://github.com/skywind3000/ecdict)。  
该项目遵循 MIT License，感谢原作者的贡献。

## 功能
- 支持正则表达式模式匹配
- 按词频过滤单词
- 使用 Rich 库以表格形式美观地展示结果

## 依赖
- pandas
- rich

## 使用方法
1. 确保 `ecdict.csv` 文件与脚本位于同一目录。
2. 安装依赖：
   ```bash
   pip install pandas rich
