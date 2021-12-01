import csv

with open('Book1.csv', 'r') as f:
  reader = csv.reader(f)
  my_list = list(reader)
    
curiosity = my_list[0]
while '' in curiosity:
    curiosity.remove('')
urgency =  my_list[1]
while '' in urgency:
    urgency.remove('')
helplessness =  my_list[2]
while '' in helplessness:
    helplessness.remove('')
anger =  my_list[3]
satisfied =  my_list[4]
while '' in satisfied:
    satisfied.remove('')
happy =  my_list[5]
while '' in happy:
    happy.remove('')
inspired =  my_list[6]
while '' in inspired:
    inspired.remove('')
peaceful =  my_list[7]
while '' in peaceful:
    peaceful.remove('')


