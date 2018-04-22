# Updated on Sep 04, 2018

import jieba
import thulac

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read comments from file
df = pd.read_csv("568230268941.csv", index_col=0, encoding="gbk")
str = ""

# Remove blank comment
comments = df[df["rateContent"] != "此用户没有填写评论!"]["rateContent"]

# Connect all comment in one string
for i in comments:
    str += i + ","

# Split Wording

# Jieba Engine
# word_list_jieba = jieba.cut(str, cut_all=False)
# # word_list = "\n".join(word_list_jieba)
# word_list = " ".join(word_list_jieba)

# thulac Engine
thu1 = thulac.thulac(seg_only=True, filt=True)
word_list = thu1.cut(str, text=True)

# Print Word Cloud
my_wc = WordCloud(font_path="STXIHEI.TTF", width=600, height=600, background_color="white").generate(word_list)
plt.imshow(my_wc)
plt.axis("off")
plt.show()
