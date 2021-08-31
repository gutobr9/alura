class Data:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    
    def formatting(self):
        print("{:02d}/{:02d}/{:02d}".format(self.day,self.month,self.year))

data = Data(10,1,21)
data.formatting()

# 17952
# 4200