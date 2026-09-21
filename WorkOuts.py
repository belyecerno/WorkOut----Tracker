import json
data=[]
class WorkOut:
    Day = None
    Type = None

    def __init__(self,Day,Type):
        self.Day = Day
        self.Type = Type

    def getdata(self):
        print(self.Day,':',self.Type)          

class Training(WorkOut):
    Ers = None
    Rpt = None
    Wgt = None
    def __init__(self, Day, Type, Ers, Rpt, Wgt):
        super().__init__(Day, Type)
        self.Ers = Ers
        self.Rpt = Rpt
        self.Wgt = Wgt

    def getdata(self):
                print('Упражнение:',self.Ers ,'\n','Кол-во повторений:',self.Rpt ,'\n', 'Вес:', self.Wgt)
                return super().getdata()
    
    def to_dict(self):
         return {
              'Day': self.Day ,
              'Type': self.Type ,
              'Ers': self.Ers ,
              'Rpt': self.Rpt ,
              'Wgt': self.Wgt
         }
    
    def add_to_file(self, date):
         data.append(self)
         data_to_save=[tr.to_dict() for tr in data]
         with open('WorkOut-Tracker/WorkOut -- Tracker/Plan.json', 'w', encoding= 'utf-8') as f:
              json.dump(data_to_save, f, ensure_ascii=False, indent=4)  
    
Training1=Training('Среда', 'Силовая', 'Жим лежа', 8, 90)
Training1.add_to_file(data)





    

