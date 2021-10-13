#
# FIX up paths in solution
import glob2 as glob
import os, fnmatch
# Using os.walk()
#    os.chdir("D:\\build\\ceres-solver\\internal\\")
#    for dirpath, dirs, files in os.walk('ceres'): 
#        for filename in files:
#            fname = os.path.join(dirpath,filename) 
#            if fname.endswith('*.vcxproj'):
#               fname.replace('C:\\repo\glog\\Release','d:\\build\\ceres-solver')
#               print(fname)







def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)
   
if __name__ == "__main__":
    os.chdir("D:\\build\\ceres-solver\\internal\\")
    a= glob.glob('.\**\*.vcxproj', recursive=True)
    for filepath in a:
        with open(filepath) as file:
            s = file.read()
        s = s.replace( 'd:\\build\\ceres-solver','D:\\build\\glog\\Release' )
        with open(filepath, "w") as file:
            file.write(s)