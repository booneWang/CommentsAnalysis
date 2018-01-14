import jieba
import pandas as pd
import os

df = pd.read_csv("551549909497.csv", index_col=0)
str = ""

for i in df["rateContent"]:
    str += i + ","

word_list_jieba = jieba.cut(str, cut_all=True)
word_list = "\n".join(word_list_jieba)

with open("temp.txt", mode="w",encoding="utf16") as file:
    file.write(word_list)
