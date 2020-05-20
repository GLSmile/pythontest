from xml.sax.handler import ContentHandler
from xml.sax import parse
import os

class Dispatcher:
    '''
     dispatch的处理思路是:
    首先根据传递的参数（就是操作名称以及节点名称）判断是否存在对应的函数如startPage，
    如果不存在则执行default+操作名称：如defaultStart。
    '''
    def dispatch(self,prefix,name,attrs=None):
        mname = prefix + name.capitalize()
        dname = 'defauilt' + prefix.capitalize
        method = getattr(self,mname,None)
        if callable(method):
            args = ()
        else:
            method = getattr(self,dname,None)
            args = name, #可以加逗号？
        if prefix == 'start':
            args +=attrs, #可以加逗号？
        if callable(method):
            method(*args)

    def startElement(self,name,attrs):
        self.dispatch('start',name,attrs)

    def endElement(self,name,attrs):
        self.dispatch('end',name)

class WebsiteConstructor(Dispatcher,ContentHandler):
    #定义的类WebsiteConstructor 继承了两个父类Dispatcher和ContentHandler
    passthrough = False

    def __init__(self,directory):
        self.directory = [directory]
        self.ensureDirectory()

    def ensureDirectory(self):
        path = os.path.join(*self.directory) #这句是什么意思？
        print(path)
        print('---------')
        if not os.path.isdir(path):
            os.makedirs(path)

    def characters(self, chars):
        if self.passthrough:
            self.out.write(chars)

    def defaultStart(self,name,attrs):
        if self.passthrough:
            self.out.write('<'+name)
            for key,val in attrs.items():
                self.out.write('%s="%s'%(key,val))
                self.out.write('>')

    def defaultEnd(self,name):
        if self.passthrough:
            self.out.write('</%s>' %name)

    def startDirectory(self,attrs):
        self.directory.append(attrs['name'])
        self.ensureDirectory()

    def endDirectory(self):
        print('endDirectory')
        self.directory.pop()

    def startPage(self,attrs):
        print('startPage')
        filename = os.path.join(*self.directory + [attrs['name']+ '.html'] )
        self.out =open(filename,'w')
        self.writeHeader(attrs['title'])
        self.passthrough = True

    def endPage(self):
        print('endPage')
        self.passthrough = False
        self.writeFooter()
        self.out.close()

    def writeHeader(self,title):
        self.out.write('<html>\n <head>\n  <title>')
        self.out.write(title)
        self.out.write('<title>\n </head>\n  <body>\n')

    def writeFooter(self):
        self.out.write('\n </body>\n<html>\n')


if __name__ =="__main__":
    parse('website.xml', WebsiteConstructor('public_html'))

