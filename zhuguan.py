#!/usr/bin/env python3
# coding: utf-8
# File: ZhuguanDetect.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-9-6

import jieba.posseg as pseg
import os
import re

class ZhuguanDetect:
    def __init__(self):
        curdir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        degree_file = os.path.join(curdir, 'dict/degree_words.txt')
        deny_file = os.path.join(curdir, 'dict/deny_words.txt')
        qingtai_file = os.path.join(curdir, 'dict/qingtai_words.txt')
        zhuzhang_file = os.path.join(curdir, 'dict/zhuzhang_words.txt')
        senti_file = os.path.join(curdir, 'dict/senti_words.txt')
        pingjia_file = os.path.join(curdir, 'dict/pingjia_words.txt')
        rencheng_file = os.path.join(curdir, 'dict/rencheng_words.txt')
        zhishi_file = os.path.join(curdir, 'dict/rencheng_words.txt')
        yiwen_file = os.path.join(curdir, 'dict/yiwen_words.txt')
        lianci_file = os.path.join(curdir, 'dict/lianci_words.txt')
        tanci_file = os.path.join(curdir, 'dict/tanci_words.txt')
        yuqi_file = os.path.join(curdir, 'dict/yuqi_words.txt')
        zhuangtai_file = os.path.join(curdir, 'dict/zhuangtai_words.txt')
        nengyuan_file = os.path.join(curdir, 'dict/nengyuan_words.txt')

        self.degree_words = self.load_words(degree_file)
        self.deny_words = self.load_words(deny_file)
        self.qingtai_words = self.load_words(qingtai_file)
        self.zhuzhang_words = self.load_words(zhuzhang_file)
        self.senti_words = self.load_words(senti_file)
        self.pingjia_words = self.load_words(pingjia_file)
        self.rencheng_words = self.load_words(rencheng_file)
        self.zhishi_words = self.load_words(zhishi_file)
        self.yiwen_words = self.load_words(yiwen_file)
        self.lianci_words = self.load_words(lianci_file)
        self.tanci_words = self.load_words(tanci_file)
        self.yuqi_words = self.load_words(yuqi_file)
        self.nengyuan_words = self.load_words(nengyuan_file)
        self.zhuangtai_words = self.load_words(zhuangtai_file)

    '''构造词典'''
    def load_words(self, file):
        return set([i.strip() for i in open(file) if i.strip()])

    '''基于主观线索进行主观性分析'''
    def zhuguan(self, sent):
        scores = []
        segs = [[w.word, w.flag] for w in pseg.cut(sent)]
        for index, seg in enumerate(segs):
            wd = seg[0]
            postags = seg[1]
            score = self.score_words(wd)
            scores.append(score)
        return sum(scores)/len(segs)

    '''通过对主观性词语进行加权，用来计算'''
    def score_words(self, word):
        score = 0.0
        if word in self.degree_words:
            score = 0.75
        elif word in self.deny_words:
            score = 0.51
        elif word in self.qingtai_words:
            score = 0.81
        elif word in self.rencheng_words:
            score = 0.95
        elif word in self.zhuzhang_words:
            score = 0.98
        elif word in self.senti_words:
            score = 0.4
        elif word in self.pingjia_words:
            score = 0.95
        elif word in self.zhishi_words:
            score = 0.75
        elif word in self.yiwen_words:
            score = 0.9
        elif word in self.lianci_words:
            score = 0.88
        elif word in self.tanci_words:
            score = 0.75
        elif word in self.yuqi_words:
            score = 0.75
        elif word in self.nengyuan_words:
            score = 0.75
        elif word in self.zhuangtai_words:
            score = 0.6
        return score

    '''文章分句处理, 切分长句，冒号，分号，感叹号等做维护标识'''
    def split_sents(self, content):
        return [sentence for sentence in re.split(r'[？?！!。；;：:\n\r]', content) if sentence]

    '''程序主函数'''
    def detect(self, content):
        sents = self.split_sents(content)
        scores = []
        for sent in sents:
            sent_score = self.zhuguan(sent)
            scores.append(sent_score)
        return sum(scores)/len(scores)

if __name__ == '__main__':
    handler = ZhuguanDetect()
    sent = '''中华人民共和国万岁'''
    score = handler.detect(sent)
    print(score)