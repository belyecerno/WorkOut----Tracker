import json # Import JSON module to work with files

data=[] # Global list to store all workouts

class WorkOut:
    Day = None
    Type = None

    def __init__(self,Day,Type):
        # Constructor: set day and workout type
        self.Day = Day
        self.Type = Type

    def getdata(self):
        # Print day and type to console
        print(self.Day,':',self.Type)          

class Training(WorkOut):
    Ers = None
    Rpt = None
    Wgt = None
    def __init__(self, Day, Type, Ers, Rpt, Wgt):
        # Call parent constructor to set day and type
        super().__init__(Day, Type)
        # Add own fields: exercise, reps, weight
        self.Ers = Ers
        self.Rpt = Rpt
        self.Wgt = Wgt

    def getdata(self):
                # Print exercise info first
                print('Упражнение:',self.Ers ,'\n','Кол-во повторений:',self.Rpt ,'\n', 'Вес:', self.Wgt)
                # Then call parent method to print day and type
                return super().getdata()
    
    def to_dict(self):
         # Convert object to dictionary for JSON saving
         return {
              'Day': self.Day ,
              'Type': self.Type ,
              'Ers': self.Ers ,
              'Rpt': self.Rpt ,
              'Wgt': self.Wgt
         }
    
    def add_to_file(self, date):
         # Add current object to the list
         data.append(self)
         # Convert all objects to dictionaries
         data_to_save=[tr.to_dict() for tr in data]
         # Open file and save data
         with open('Plan.json', 'w', encoding= 'utf-8') as f:
              json.dump(data_to_save, f, ensure_ascii=False, indent=4)  

# Create a workout
Training1=Training('Среда', 'Силовая', 'Жим лежа', 8, 90)
# Save it to file
Training1.add_to_file(data)





    

