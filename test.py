import pandas as pd
from rich.console import Console
from rich.table import Table

def just_az_words(df):
    filtered_df = df[df["word"].str.match(r'^[a-z]', na=False)]
    return filtered_df

def match_word(df, pattern):
    regex_pattern = "^"+pattern.replace(" ", ".")+"$"
    filtered_df = df[df["word"].str.match(regex_pattern)]
    return filtered_df

def frq_filtered_words(df, min_frq):
    df = df.copy()
    df["frq"] = df["frq"].astype(int)
    df["bnc"] = df["bnc"].astype(int)
    filtered_df = df[df["frq"] >= min_frq]
    return filtered_df

def print_table_rich(df, columns):
    console = Console() 
    table = Table(title="Filtered Words", show_lines=True)
    for col in columns:
        table.add_column(col, overflow="wrap", style="cyan")
    for _, row in df.iterrows():
        row_data = [
            str(row.get(col, "")).replace("\\n", "\n")
            if pd.notna(row.get(col, ""))
            else ""          
            for col in columns
        ]
        table.add_row(*row_data)
    console.print(table)
    
def main():
    df = pd.read_csv("ecdict.csv", encoding="utf-8",comment ="#")
    az_words = just_az_words(df)
    while True:
        inquery = input("Enter a pattern : ")
        if inquery == 'q':
            print("程序已退出。")
            break    
        matching_words_df = match_word(az_words, inquery)
        frq_words_df = frq_filtered_words(matching_words_df, 100)
        showed_columns = ["word", "phonetic", "definition", "oxford", "tag", "bnc", "frq"]
        aviailable_columns = [col for col in showed_columns if col in frq_words_df.columns]
        print_table_rich(frq_words_df, aviailable_columns)
        word_count = len(frq_words_df["word"].unique())
        if word_count >= 10:
            print(f"匹配到的单词数目: {word_count}")

if __name__ == "__main__":
    main()

