import os 
import time 
import datetime

"""
变量说明
#dirs：检索目录
#full_path：完整文件路径
#mtime：文件的修改时间
#file_to_review：字典形式存储的待复习文件路径
#timegap：时间跨度
"""
if __name__ == "__main__":
    #获取日期
    today = datetime.datetime.now()
    dirs = os.getcwd()+r"\\计算机学习笔记"
    temp_dirs = []
    #准备待复习文件记录列表 
    file_to_review = {7:[],14:[],30:[],120:[],360:[]}
    temp_dirs.append(dirs)
    for filename in temp_dirs:
        full_path = os.path.join(dirs,filename)
        for file in os.listdir(full_path):
            full_file_name = full_path+"\\"+file
            if os.path.isdir(full_file_name):
                temp_dirs.append(full_file_name)
            elif os.path.isfile(full_file_name):
                if full_file_name.endswith(".md"):                 
                    #获取修改时间
                    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(full_file_name))
                    timegap = (today - mtime).days
                    for i in [7,14,30,120,360]:
                        if timegap == i:
                            #file_to_review[i].append(full_file_name)
                            print(str(i)+":"+full_file_name)
            
