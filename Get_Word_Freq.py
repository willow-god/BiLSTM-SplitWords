# 读取sighan.txt文件
with open('data/sighan.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 将文章分词，假设词汇是用空格分开的
words = text.split()

# 统计词汇频率
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# 读取dictionary.txt文件，提取常用词汇
with open('data/dictionary.txt', 'r', encoding='utf-8') as dict_file:
    common_words = set(dict_file.read().split())

# 筛选常用词汇的频率统计结果
common_word_freq = {word: freq for word, freq in word_freq.items() if word in common_words}

# 按频率降序排序
sorted_common_word_freq = dict(sorted(common_word_freq.items(), key=lambda item: item[1], reverse=True))

# 将频率统计结果保存到文件
with open('data/word_freq.txt', 'w', encoding='utf-8') as output_file:
    for word, freq in sorted_common_word_freq.items():
        output_file.write(f'{word}: {freq}\n')
