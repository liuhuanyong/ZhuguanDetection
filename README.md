# ChineseZhuguanDectection
Chinese Subjective Dectection based on subjective knowlegebase, 基于中文主观性知识库的句子主观性评定方法。

#项目介绍 
主观性是中文舆情和文本挖掘一个必不可少的一项环节。
对于英文而言，我调研过textblob的主观性接口，对于输入一个句子，textblob用的是词语主观性词典+加权的打法，相应的介绍可以查看我的总结材料(documents下的pdf文件)
而针对目前github开源平台上还缺少有对中文句子主观性评定的接口，本项目将尝试弥补这一空缺。
本项目将从中文自身的特点出发，通过总结并挖掘中文句子主观性线索知识库和客观性线索知识库，提供一个面向中文句子的主观性判定方法。

# 主观性字典
1) degree_words.txt:程度副词，221个
2) deny_words.txt:否定副词，29个
3) lianci_words.txt:连词，93个
4) nengyuan_words.txt:能愿副词，719个
5) pingjia_words.txt:评价词，6846个
6) qingtai_words.txt:情态动词，29个
7) rencheng_words.txt:人称代词，32个
8) senti_words:情感词，2090个
9) tanci_words:叹词，139个
10) yiwen_words:疑问代词，26个
11) yuqi_words:语气词，17个
12) zhishi_words.txt:指示代词，64个
13) zhuangtai_words.txt:状态词，49个
14) zhuzhang_words.txt:主张词，235个

# 主观性计算规则
1) 文本分句
2) 计算每个句子的主观性。
3) 每个句子主观性计算方式:主观线索词*主观线索词权重，做加权累加和平均
3) 每个句子主观性求平均
4) 输出文本主观性

# 使用方式：
    from zhuguang import *
    handler = ZhuguanDetect()
    sent = '''你要分析的文本'''
    score = handler.detect(sent)
    print(score)
# 效果
    content = '今天天气晴朗'
    score = 0.0
    **********************
    content = '江龙船艇：台风“山竹”造成直接经济损失400万至500万'
    score = 0.09375
    **********************
    content = '中华人民共和国万岁'
    score = 0.200
    **********************
    content = '这两天经济不景气，恐怕这单子有得毁掉了'
    score = 0.2092
    **********************
    content = '9月底美联储再次加息几乎板上钉钉，央行大概率小幅跟随加息，与此同时的定向降准对冲显得更为重要。预计10月前后可能再次实施定向降准措施。'
    score = 0.237
    **********************
    content = '预计明后两天江西会有大到暴雨'
    score = 0.36
    **********************
    content = '我喜欢你'
    score = 0.767
    *****************************
# 总结
1）本项目以词汇知识库的方式，通过总结归纳出主观性线索词，并加以规则进行计算。  
2) 从上面的效果来看，还像是那么回事，但还有提升空间。  
3) 主观性配合情感得分，相信能够在舆情分析上起到一定作用。   
4）词库欢迎补充。send mail to: lhy_in_blcu@126.com  
