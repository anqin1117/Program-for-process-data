import os
import shutil
import cv2
 
def getFileList(dir,Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    #print("newDir = ",newDir)
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)
    
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir=os.path.join(dir,s)
            getFileList(newDir, Filelist, ext)
 
    return Filelist

def getTxt(dir,Txtlist,ext=None):#查找TXT文件路径

    txtDir = dir
    if os.path.isfile(dir): #判断dir是否为文件
        if ext is None:
            Txtlist.append(dir)
        else:
            if ext in dir[-3:]:
                Txtlist.append(dir)

    elif os.path.isdir(dir): #判断某dir是否为目录(文件夹)
        for s in os.listdir(dir):
                txtDir = os.path.join(dir,s)
                getTxt(txtDir, Txtlist, ext)
    
    return Txtlist
'''
def wirteTxt(txtdir,imgdir):
#这段代码是将字符串转为list去处重再逐个元素放入txt文件

   txtpath_list = getTxt(txtdir, [], 'txt')
   imglist = getFileList(imgdir,[],'jpg')
   txt = open(txtpath_list,'r+')
   for i in range(len(imglist)):
        imgname = os.path.splitext(os.path.basename(imglist[i]))[0] #图片名称
        #print("imaname = ",imgname)
        alp_label = alp_label+imgname
        #print('alp_label', alp_label)
    #print("for循环完成")
    #alp_list = list(set(alp_label))
    #print("str->list 完成")
    #print('alp_list', alp_list)
    print("len(alp_label) = ", len(alp_label))
    1/0
    for j in range(len(alp_label)):
        txt.write(alp_list[j]+'\n')
    txt.close()
'''


if __name__ == '__main__':

    org_img_folder='./traindata'
    org_txt_folder='./'
    save_dir = './traindata'
    txtfile = './string.txt'
    # 检索文件
    imglist = getFileList(org_img_folder, [], 'jpg')
    #print('imglist = ', imglist)
    print('本次执行检索到 '+str(len(imglist))+' 张图像\n')#图片数量

    alp_label = ''
    alp_list = []
    txt = open(txtfile,'r+')
    for i in range(len(imglist)):
        imgname = os.path.splitext(os.path.basename(imglist[i]))[0] #图片名称
        #print("imaname = ",imgname)
        alp_label = alp_label+imgname
        #print('alp_label', alp_label)
    print("for循环完成")
    alp_list = list(set(alp_label))
    print("str->list 完成")
    #print('alp_list', alp_list)
    for j in range(len(alp_list)):
        txt.write(alp_list[j]+'\n')
    print("finish")
    txt.close()
    
    '''
    txtlist = getTxt(org_txt_folder,[],'txt') #txt文件路径 list类型
    txt = open(txtlist[0]) #打开txt文件
    lines = txt.readlines() ##读取全部内容 ，并以列表方式返回，每个元素是一行内容
    print("lines length = ",len(lines))
    for i in range(len(imglist)):
        imgname = os.path.splitext(os.path.basename(imglist[i]))[0] #图片名称
        print('imgname = ',imgname)
        j = int(imgname[4:11])#包括了imgname[4] 不包括imgname[11]
        print('j = ',j)
        old_dir = os.path.join(org_img_folder,imgname+'.jpg')
        #print("old_dir = ",old_dir)
        labname = lines[j-1][:11] #图片就名称与label名称的对应
        #print("imaname = ",imgname)
        print('labname = ',labname)
        newname = lines[j-1][16:-1] #图片的新名称，用图中文字命名
        print('newname = ',newname)
        if imgname == labname:
            new_dir = os.path.join(save_dir,'{}{}'.format(newname,'.jpg'))
            print('new_dir = ',new_dir)
            shutil.copyfile(old_dir,new_dir)
            #os.rename(old_dir, new_dir) #相当于把原图剪切然后重命名并放入其他文件夹
            print("save_dir = ",new_dir)
  
    txt.close()
    '''#这段代码是将字符串转为list去处重再逐个元素放入txt文件
