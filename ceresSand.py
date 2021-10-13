#
# findReplace OS utility function.  TODO ,  as more added put in assembley
#
#
import glob2 as glob
import os, fnmatch
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
    os.chdir("D:\\build\\ceres-solver")
    a= glob.glob('.\**\*.vcxproj', recursive=True)
    cnt=int(0)
    for filepath in a:
        with open(filepath) as file:
            s = file.read()
        s = s.replace( 'C:\\repo\\glog\\Release','D:\\build\\glog\\Release' )
        with open(filepath, "w") as file:
            file.write(s)
            print('count: ',cnt, 'string: ', s) 
            cnt=cnt+1