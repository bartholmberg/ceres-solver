#
# FIX up paths in solution
import glob2 as glob

import os
   
# Using os.walk()
if __name__ == "__main__":
    os.chdir("D:\\build\\ceres-solver\\internal\\")
    for dirpath, dirs, files in os.walk('ceres'): 
        for filename in files:
            fname = os.path.join(dirpath,filename)
          
            if fname.endswith('*.vcxproj'):
               fname.replace('C:\\repo\glog\\Release','d:\\build\\ceres-solver')
               print(fname)
   
