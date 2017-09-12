
##wordcloud

import matplotlib.pylab as plt
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
import PIL.Image as Image
import jieba
from scipy.misc import imread

coloring = imread(r'引用图片名称')

text_from_file_with_apath = open(r'文本文件名称').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
#结巴分词，并用空格连接，赋给新变量

my_wordcloud = WordCloud(background_color="black",     
                         max_words=2000,
                         mask = coloring,
                         max_font_size=60,
                         random_state=42,
                         scale=2,
                         font_path = '字体文件.ttf').\
                         generate(wl_space_split)
#ttf文件为字体，如果没有该文件，汉字无法正常显示(在自己电脑上直接搜索*.ttf就能找到系统的字体文件)

#使用图片的颜色
#image_colors = ImageColorGenerator(coloring)
#plt.imshow(my_wordcloud.recolor(color_func=image_colors))

plt.title(u"图片标题")   #如要使用中文, 也要设字体
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
my_wordcloud.to_file("命名图片")
