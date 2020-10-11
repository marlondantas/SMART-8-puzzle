import time

class View(object):
    #Futaramente usar o tkinter
    count = 0
    __lastTime = 0
    __newTime = 0
    __totalTime = 0

    timepass = 0

    def addCount(self, valor =1, __newTime = 0):
        self.count = self.count +1
        
        self.__totalTime = self.__totalTime + self.timepass

        self.timepass = abs(self.__lastTime - self.__newTime)

        self.__lastTime = self.__newTime

        return self.count

    def progressBar(self, title, total,title2= '',time2 = ''):
        #Atualizacao do tempo
        self.__newTime = time.time()

        if(title2 != ""):
            time2 = str(self.timepass)
        
        print(title,'%s' % (total) ,title2, '%s' % (time2), end='\r')
    # print("")

    def __init__(self):
        self.__lastTime = time.time()

    def setBarra(self):
        pass

    def addBarra(self):
        pass

    def endBarra(self):
        pass

# import sys

# toolbar_width = 40

# # setup toolbar
# sys.stdout.write("[%s]" % (" " * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

# for i in range(150):
#     time.sleep(0.1) # do real work here
#     # update the bar
#     sys.stdout.write("-")
#     sys.stdout.flush()

# sys.stdout.write("]\n") # this ends the progress bar

if __name__ == "__main__":
    
    nova = View()
    for x in range(100000):
        nova.progressBar('Total de tentivas: ',nova.addCount(),'TEMpo:')

    print("")