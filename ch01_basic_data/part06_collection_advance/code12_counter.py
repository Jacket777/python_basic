"""
1.12 序列中出现次数多的元素
问题
怎样找出一个序列中出现次数多的元素呢？
解决方案
collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法直接给了你答案。
"""
from collections import Counter

def sample_01():
    words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes',
             'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes',
             "you're", 'under']
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)
    print(word_counts['not'])
    print(word_counts['eyes'])
    more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    for word in more_words:
        word_counts[word] += 1
    print(word_counts['eyes'])



def sample_02():
    words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes',
             'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes',
             "you're", 'under']
    more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_counts = Counter(words)
    word_counts.update(more_words)
    print(word_counts['eyes'])



def sample_03():
    words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes',
             'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes',
             "you're", 'under']
    more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    a = Counter(words)
    b = Counter(more_words)
    print(a)
    print(b)
    c = a + b
    print(c)
    d = a - b
    print(d)






if __name__ == '__main__':
    sample_03()