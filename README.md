# Word Search Tool

A flexible and efficient word search and vocabulary-learning tool for English learners. Built with Python, it supports regex-based word matching, pronunciation pattern discovery, and frequency-based filtering.

---

## ✨ Features

- ⛏️ **Regex Pattern Matching**: Search words with patterns like `.ail` or `con....` to explore related vocabulary.
- 🔍 **Pronunciation Support**: Displays IPA phonetics (British English), helps identify pronunciation patterns.
- 🔢 **Frequency Filtering**: Filter by high-frequency vocabulary using BNC and COCA corpus data.
- 🔹 **Exam Tags**: Identify if words are tagged for GRE, IELTS, etc.
- 🕁️ **Side-by-side Word Grouping**: Easily compare minimal pairs or word families (e.g. *slap*, *slip*, *slop*).
- 🌍 **English-English Definitions**: All definitions are monolingual to encourage immersive learning.
- 🌟 **Rich Output**: Uses the `rich` library to present search results in a clean, colorful table format.

---

## 🔹 Demo Screenshots

### 1. Partial Spelling Match
Search with placeholders (`.` or space) to discover related words.
![partial](https://github.com/user-attachments/assets/b4378e07-8376-474b-b920-04ce8f508294)

### 2. Pronunciation Pattern Analysis
Visualize groups of words by onset pattern and vowel variation.
![pattern](https://github.com/user-attachments/assets/e4402d0c-457a-4cc7-a4bd-87c77a2f5ea6)

### 3. Vowel Comparison (Minimal Pairs)
Group words like `slap/slip/slop` to observe vowel changes.
![minimal](https://github.com/user-attachments/assets/1d00653f-be1b-4bee-9985-b3b1c2148ee5)

---

## 📊 Data Source

The project uses the [ecdict](https://github.com/skywind3000/ecdict) dataset, a free and open-source English-Chinese dictionary in CSV format. It includes:

- Word spellings and British IPA phonetics
- Definitions, and exam tags (GRE, IELTS, etc.)
- Word frequency data from BNC and COCA

> This project respects the original MIT license of ECDICT.

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/word-search-tool.git
cd word-search-tool
```

### 2. Install dependencies
```bash
pip install pandas rich
```

### 3. Download and place the dictionary data
Download `ecdict.csv` from:
https://github.com/skywind3000/ECDICT/blob/master/ecdict.csv

Place the file into the project root directory.

---

## 🚀 Usage

Run the script and input patterns to search:
```bash
python word_search.py
```
Then enter a pattern like:
```
con....
.ail
sl.p
```
You will see a colored table of matching words with phonetics, meanings, tags, and frequencies.

---

## 📍 License

This project is licensed under the MIT License.
Thanks to [skywind3000](https://github.com/skywind3000) for the ECDICT dataset.

---

## 🙏 Acknowledgments

- [ecdict](https://github.com/skywind3000/ecdict) for the dictionary data
- [Rich](https://github.com/Textualize/rich) for output enhancement

---

Happy word hunting! 🤖

