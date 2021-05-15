from kivy.utils import platform
import os
def check_recent():
    import glob

    try:
        if platform == 'android':

            list_of_files = glob.glob(
                '/sdcard/DCIM/TypeToWrite/*.png')  # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            return latest_file
        else:
            list_of_files = glob.glob(
                '/Users/willson/NewerUpdates/*.png')  # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            return latest_file
    except:
        pass