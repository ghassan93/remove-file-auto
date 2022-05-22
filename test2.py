import schedule
import time
import os
import glob
import shutil



    


def job():
    #generate  new file in main folder path
    list1 = ['a', 'b', 'c']

    for i in range(len(list1)):
       open('file%s.sav' % i, 'w').write(list1[i])
    print('added')


    #remove old files in model folder
    files_remove = glob.glob('C:/Users/sa/Desktop/run auto/model/*.sav')
    for f in files_remove:
        os.remove(f)
    print('Removed')


    # move files from main directory to model folder
    source_f = 'C:/Users/sa/Desktop/run auto/' 
    destination_f = 'C:/Users/sa/Desktop/run auto/model/'
    pattern = "\*.sav"

    file_moved = glob.glob(source_f + pattern)
    for file in file_moved:
        file_name = os.path.basename(file)
        shutil.move(file, destination_f + file_name)
    print('Moved')
    print("I'm working...")



######run code every day automatically
######run code every minutes automatically


schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("17:13").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(5)