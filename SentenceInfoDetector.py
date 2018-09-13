#!/usr/bin/env python3
# coding: utf-8
# File: SentenceInfoDetector.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-9-6

import os
import jieba
import jieba.posseg as pseg
from collections import Counter
class SentInfo:
    def __init__(self, sent):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        degree_file = os.path.join(cur_dir, 'dict/degree_words.txt')
        deny_file = os.path.join(cur_dir, 'dict/deny_words.txt')
        mark_file = os.path.join(cur_dir, 'dict/mark_words.txt')
        opinion_file = os.path.join(cur_dir, 'dict/opinion_words.txt')
        prob_file = os.path.join(cur_dir, 'dict/prob_words.txt')
        question_file = os.path.join(cur_dir, 'dict/question_words.txt')
        status_file = os.path.join(cur_dir, 'dict/status_words.txt')
        self.sent = sent
        self.degree_dict = self.build_dict(degree_file)
        self.deny_dict = self.build_dict(deny_file)
        self.mark_dict = self.build_dict(mark_file)
        self.opinion_dict = self.build_dict(opinion_file)
        self.prob_dict = self.build_dict(prob_file)
        self.question_dict = self.build_dict(question_file)
        self.status_dict = self.build_dict(status_file)
        self.words, self.postags = self.seg_sents(sent)

    '''构建字典'''
    def build_dict(self, filepath):
        return {i.strip().split('\t')[0]: i.strip().split('\t')[1] for i in open(filepath) if i.strip() and len(i.strip().split('\t')) == 2}

    '''语气类型'''
    def tone(self):
        tone_dict = {
            '?':'question',
            '？':'question',
            '!': 'emphasize',
            '！': 'emphasize',
        }
        pos = [i for index, i in enumerate(self.words) if self.postags[index] == 'x' and i in tone_dict]
        start = pos[0]
        if not pos:
            return 'normal'
        pos_dict = {i[0]:i[1] for i in Counter(pos).most_common()}
        rank_start = [i[0] for i in Counter(pos).most_common()][0]
        if pos_dict[start] == pos_dict[rank_start]:
            return tone_dict[start]
        else:
            return tone_dict[rank_start]

    '''判断句子是否属于观点句'''
    def opinion(self):
        opinion_words = list(self.opinion_dict.keys()) + list(self.prob_dict.keys())
        opinion_tag = [wd for wd in self.words if wd in opinion_words]
        if opinion_tag:
            return 1
        else:
            return 0

    '''判断句子激烈程度'''
    def degree(self):
        degrees = [float(self.degree_dict.get(wd, 0)) for wd in self.words]
        if not degrees:
            return 0.0
        else:
            return sum(degrees)

    '''判断句子状态'''
    def status(self):
        status_words = [wd for wd in self.words if wd in list(self.status_dict.keys())]
        if not status_words:
            return 'now'
        else:
            return self.status_dict.get(status_words[0])

    '''判断句子极性'''
    def ploarity(self):
        neg_words = [wd for wd in self.words if wd in list(self.deny_dict.keys())]
        if not neg_words:
            return 'normal'
        else:
            return 'deny'


    '''对句子进行分词处理'''
    def seg_sents(self, sent):
        tmp = [[w.word, w.flag] for w in pseg.cut(sent)]
        words = [i[0] for i in tmp]
        postags = [i[1] for i in tmp]
        return words, postags

sent = '2018年这些新车将要上市了你想要买吗？？？!!!!!'
handler = SentInfo(sent)
tone = handler.tone()
print(tone)
opinion = handler.opinion()
print(opinion)
degree = handler.degree()
print(degree)
status = handler.status()
print(status)
ploarity = handler.ploarity()
print(ploarity)