import schedule
import time
import os
import glob
import shutil



    
path_file_remove = 'C:/Users/sa/Desktop/run auto/model/*.sav'
source_file_move='C:/Users/sa/Desktop/run auto/' 
destination_file='C:/Users/sa/Desktop/run auto/model/'


def job():

    #generate  new file in main folder path
    list1 = ['a', 'b', 'c']
    for i in range(len(list1)):
       open('file%s.sav' % i, 'w').write(list1[i])
    print('added')


    #remove old files in model folder
    files_remove = glob.glob(path_file_remove)
    for f in files_remove:
        os.remove(f)
    print('Removed')


    # move files from main directory to model folder
    source_f = source_file_move
    destination_f = destination_file
    pattern = "\*.sav"

    file_moved = glob.glob(source_f + pattern)
    for file in file_moved:
        file_name = os.path.basename(file)
        shutil.move(file, destination_f + file_name)
    print('Moved')
    print("I'm working...")

job()


# schedule.every(1).minutes.do(job)
# # schedule.every().day.at("17:13").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(5)