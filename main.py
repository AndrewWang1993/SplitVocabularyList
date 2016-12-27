# -*-coding=utf-8-*-
import re, os, urllib, sys, socket, string, time

reload(sys)
sys.setdefaultencoding('utf-8')


def getHtml(url):  # 获取网页源代码
    page = urllib.urlopen(url)
    htmlText = page.read()
    return htmlText


def getVocabularyList(htmlText):  #
    reg = r'lang="en" word="([^\s]*?)"'
    mre = re.compile(reg)
    picUrl = re.findall(mre, htmlText)
    return picUrl


def getVocabularyDefine(htmlText):  #
    reg = r'<div class="definition">([^\s]*?)</div>"'
    mre = re.compile(reg)
    picUrl = re.findall(mre, htmlText)
    return picUrl


def getVocabularyExample(htmlText):  #
    reg = r'<div class="example">([^\s]*?)</div>"'
    mre = re.compile(reg)
    picUrl = re.findall(mre, htmlText)
    return picUrl


vocabularyURL = "https://www.vocabulary.com/lists/52473"

textInfo = getHtml(vocabularyURL);
print  textInfo

print "----------------------------------------------------------------------------"

vocabularyList = getVocabularyList(textInfo);
print vocabularyList
print len(vocabularyList)

print "----------------------------------------------------------------------------"

vocabularyDefine = getVocabularyDefine(textInfo);
print vocabularyDefine
print len(vocabularyDefine)

print "----------------------------------------------------------------------------"

vocabularyExample = getVocabularyExample(textInfo);
print vocabularyExample
print len(vocabularyExample)

print "----------------------------------------------------------------------------"
