# coding=utf-8
import urllib
import os
import yaml

class StockCode:
    stockcode_file = os.getcwd() + os.sep + "stockcode.yaml"
    stockname_file = os.getcwd() + os.sep + "stockname.yaml"
    stock_codedict = None
    stock_namedict = None
    stock_codelist = []

    def __init__(self):
        self.index = 0
        if self.stock_codedict == None:
            with open(self.stockcode_file) as fd:
                self.stock_codedict = yaml.load(fd)

        if self.stock_namedict == None:
            with open(self.stockname_file) as fd:
                self.stock_namedict = yaml.load(fd)
        if self.stock_codelist == []:
            for code in self.stock_codedict.keys():
                prefix = code[:2]
                if prefix == "30" or prefix == "60" or prefix == "00":
                    self.stock_codelist.append(code)
            self.stock_codelist.sort()
        self.codenum = len(self.stock_codelist)

    def getcode(self, name):
        try:
            return self.stock_namedict[name]
        except:
            return None

    def getname(self, code):
        try:
            return self.stock_codedict[code]
        except:
            return None

    def __iter__(self):
        return self

    def next(self):
        if self.index < self.codenum - 1:
            self.index += 1
            return self.stock_codelist[self.index]
        else:
            self.index = 0
            raise StopIteration()

if __name__ == "__main__":
    stock = StockCode()
    for i in stock:
        print i
    print stock.getname("600000")

