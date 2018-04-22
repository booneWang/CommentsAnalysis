import jieba
import thulac

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("558517626411.csv", index_col=0)
str = ""

comments = df[df["rateContent"] != "此用户没有填写评论!"]["rateContent"]

for i in comments:
    str += i + ","

# Jieba Engine
# word_list_jieba = jieba.cut(str, cut_all=False)
# # word_list = "\n".join(word_list_jieba)
# word_list = " ".join(word_list_jieba)

# thulac Engine
thu1 = thulac.thulac(seg_only=True, filt=True)
word_list = thu1.cut(str, text=True)

my_wc = WordCloud(font_path="STHeiti Medium.ttc", width=600, height=600, background_color="white").generate(word_list)
plt.imshow(my_wc)
plt.axis("off")
plt.show()

# with open("temp.csv", mode="w", encoding="utf16") as file:
#     file.write(word_list)
