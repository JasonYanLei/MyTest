# MyTest



import json

# Read in json file and write each element to another txt file
输入文档 = 'input.json'
输出文档 = 'output.txt'
转换文档 = 'output.pdf'

# Read in the input json file
with open(输入文档, 'r', encoding="utf-8") as file:
    data = json.load(file)

# Write each element of the json file to another txt file
with open(输出文档, 'w', encoding="utf-8") as file:
    for key, value in data.items():
        file.write(f'{key}: {value}\n\n')

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def txt_to_pdf(input_file, output_file):
    c = canvas.Canvas(output_file, pagesize=letter)
    text = ""
    with open(input_file, 'r', encoding="utf-8") as file:
        for line in file:
            text += line
    c.drawString(100, 750, text)
    c.save()

txt_to_pdf(输出文档, 转换文档)

# NLTK（Natural Language Toolkit）是一个用于自然语言处理的Python库，
# 虽然它主要是针对英文文本的处理，但也可以用于处理中文文本。
# 下面是使用NLTK处理中文文本的例子：

# 1. 分词（Tokenization）：
import jieba

text = "自然语言处理是一门很有趣的学科。"
seg_list = jieba.cut(text, cut_all=False)
print(" ".join(seg_list))

# 2. 词性标注（Part of Speech Tagging）：

import jieba.posseg as pseg

words = pseg.cut("自然语言处理是一门很有趣的学科。")
print(' * '.join('{}/{}'.format(w.word,w.flag)for w in words))

# 3. 停用词移除（Stopword Removal）：

from nltk.corpus import stopwords
import jieba

text = "自然语言处理是一门很有趣的学科。"
stop_words = set(stopwords.words('chinese'))
seg_list = jieba.cut(text, cut_all=False)
filtered_words = [word for word in seg_list if word not in stop_words]
print(" ".join(filtered_words))
