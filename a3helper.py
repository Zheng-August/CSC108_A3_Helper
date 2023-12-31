"""
在做这个assignment之前 请你确保你完成了以下的几件事情：
1.week 1 - 9 的PCRs
2.对dict的运用熟练 或者至少知道dict.item(),.values(),.keys()的概念
3.知道如何遍历dict和list of tuple，如使用循环进行遍历。
4.理解如何处理和操作字符串，包括split、join(这个不一定要用)
5.记得加我微信! 不是代写不卖课 不卖电子烟不是dm 单纯想扩列 wx号:1224917119
6.这个helper未来我有空会进行修改 可以到时候查看一下

*******************************
开始前的介绍
*******************************
现在我要介绍的是我们这次要用到的一个全新的type: 元数据（ArxivType）
虽然它被称作以一个新的type但是实际上和a2的桥数据没有任何区别
它是由一个dict套dict的形式组成的

我们在这个assignment里的example是:
EXAMPLE_ARXIV = {
    '5090': {
        ID: '5090',
        TITLE: "Increasing Students' Engagement to Reminder Emails",
        CREATED: '',
        MODIFIED: '2022-08-02',
        AUTHORS: [('Yanez', 'Fernando'), ('Zavaleta-Bernuy', 'Angela')],
        ABSTRACT: 'Our metric of interest is open email rates.'},

    。。。。。。。

    '42': {
        ID: '42',
        TITLE: '',
        CREATED: '2023-05-04',
        MODIFIED: '2023-05-05',
        AUTHORS: [],
        ABSTRACT: 'This is a strange article with no title\n'
        + 'and no authors.\n\nIt also has a blank line in its abstract!'}
}
可以看出 最外面的这个EXAMPLE_ARXIV是一个dict 然后里面的每一个key都对应着另一个dict

EXAMPLE_ARXIV = {
    '5090': {},

    。。。。。。。

    '42': {}
}
像这样⬆️

这个小的dict里储存的便是最重要的一个部分 比如:
ID: '42',
TITLE: '',
CREATED: '2023-05-04',
MODIFIED: '2023-05-05',
AUTHORS: [],
ABSTRACT: 'This is a strange article with no title\n'
+ 'and no authors.\n\nIt also has a blank line in its abstract!'}

好 那么如果我们想要获取id为42的这个书籍的CREATED 我们应该怎么做？
A: EXAMPLE_ARXIV['42'][CREATED]
以此类推


*******************
Function Helper
*******************
首先 再次声明 这一份hlper中不包含任何实际代码或者直接的语言回答

1. created_in_year
此函数的目的是判断一个指定 ID 的文章是否存在于给定的ArxivType中,并且是否在特定的年份发布。

重点
检查文章ID是否存在:使用 article_id in metadata 来判断文章ID是否在ArxivType字典中。
判断发布年份:如果文章ID存在,提取其创建日期并与给定的年份进行比较。
返回布尔值：如果文章存在且年份匹配，则返回 True;否则,返回 False。


提示
重新看我最上面对ArxivType的分析


2.contains_keyword
此函数的目的是从给定的元数据中找出所有包含特定关键字的文章ID。它会检查文章的标题、作者名字和摘要中是否出现了这个关键词。

重点
关键字匹配：匹配时，关键字必须完全一致，忽略大小写，且忽略标点。
遍历文章：对元数据中的每篇文章进行遍历，检查其标题、作者名字和摘要。
清洗文本：使用之前提到的 clean_word 函数来清洗文本，移除非字母字符，转换为小写。
累计匹配的ID：如果文章的标题、作者名字或摘要包含关键字，将其ID加入结果列表。

可能出错的点
关键字精确匹配：关键字必须是独立的单词，这意味着它不能是更大单词的一部分。这可能会导致漏掉某些匹配情况，
            例如，如果关键字是“bio”，它不会匹配到“biological”。

提示
这个函数的重点依旧是会不会使用遍历 和 对元数据的形式掌握情况
记得使用clean_word


3.average_author_count 
此函数的目的是计算给定元数据中每篇文章的平均作者数量。

重点
计算总作者数：遍历元数据中的每篇文章，累加每篇文章的作者数量。
计算文章总数：通过获取元数据中文章的数量。
计算平均值：用总作者数除以文章总数得到平均作者数量。

可能出错的点
空元数据处理：如果元数据为空（没有文章），函数正确地返回 0.0

提示
🈚️


4.read_arxiv_file
这个函数的制作会比较难
目的：将一系列文本行转换为一个 ArticleType 格式的字典。

重点
逐行读取文件：从文件中读取每一行，除去换行符。
组织文章信息：当遇到 'END' 标记时，将处理后的文章信息存储在字典中。
创建文章字典：使用前几行信息（ID、标题、创建日期、修改日期）初始化文章字典。
处理作者信息：将每行作者信息分割成名字列表，然后添加到文章字典的作者列表中。
处理摘要信息：从特定行开始，读取每行作为摘要的一部分，直到遇到 'END' 标记。

1.可以先学习一下如何初始化文章字典
文章 = {
        名字：小明
        地址：多伦多大学建军路32号
    }
2.作者信息切割要用到split
3。作者信息和摘要信息不止一行 仔细甄别
4.在这个funcions的最下面有工具帮你判断这个函数是否正确


5.make_author_to_articles
目的：创建一个字典，将每个作者的名字映射到他们所写的文章ID列表上。

重点
创建作者到文章的映射：遍历每篇文章，对于每篇文章中的每个作者，如果作者尚未在字典中，添加他们和对应的文章ID；如果已存在，将文章ID添加到他们的列表中。
排序文章ID：对每个作者的文章ID列表按字典序排序（sort）。

可能出错的点
作者名字假设：假设作者名字是唯一的标识符。如果有同名作者，这可能会导致数据混淆。
数据结构假设：假设 id_to_article 中的每篇文章都有一个作者列表。如果缺少作者信息，可能会导致错误。


6.get_coauthors
目的：根据给定的作者名，返回他们的合作作者列表。

重点
识别合作作者：遍历元数据中的每篇文章，如果给定的作者是文章的作者之一，将其他作者添加到合作作者列表中。
排序合作作者：将合作作者列表按字典序排序。

可能出错的点
重复合作作者：如果一个作者与给定的作者在多篇文章中合作，该合作作者可能会在列表中重复出现。

7.get_most_published_authors
目的：找出在元数据中发表文章最多的作者。

重点
统计每个作者的发表数量：使用 make_author_to_articles 函数获取作者与其文章列表的映射，然后统计每个作者的文章数量。
识别最多发表的作者：找出发表文章数量最多的作者。

可能出错的点
多个作者发表数量相同：如果有多个作者的发表数量相同，都是最多的，需要将他们都包含在结果中。

8.suggest_collaborators
目的：为给定的作者推荐潜在的合作伙伴。

重点
确定潜在合作伙伴：查找给定作者的合作作者，然后查找这些合作作者的合作伙伴，排除已经是给定作者合作伙伴的作者。
排序推荐合作伙伴：将潜在的合作伙伴按字典序排序。

可能出错的点
重复推荐：可能会推荐已经是该作者合作伙伴的其他作者。





9.has_prolific_authors 函数
目的：检查给定的文章是否至少有一位发表文章数量达到某个最小值的“多产”作者。

重点
检查多产作者：遍历作者及其文章ID列表，如果找到一个作者的发表数量达到或超过给定的最小发表数量，并且该作者发表了给定的文章，则返回 True。
适用于任意文章：可以用于检查任意文章是否符合多产作者的条件。
需要使用上面的make_author_to_articles function

10.keep_prolific_authors 
目的：更新 id_to_article 字典，使其只包含由多产作者发表的文章。

重点
使用 deepcopy：为了避免修改原始字典，使用 deepcopy 创建一个副本。
在最前面加入from copy import deepcopy
筛选文章：使用 has_prolific_authors 函数来确定是否保留每篇文章。
移除非多产作者的文章：从原始字典中移除那些不符合多产作者条件的文章。


"""