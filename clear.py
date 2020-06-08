# -*- coding: utf-8 -*-

# 清理格式
import os
# https://blog.csdn.net/lixiangyong123/article/details/52515758

# 遍历文件夹
def walkFile(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            if(".md" in f):
                # print(os.path.join(root, f))
                # 读取文件
                fname = os.path.join(root, f)
                # print(fname)
                myfile = open(fname, 'r')
                lines = myfile.readlines()
                # print(lines[0])
                flag = 0

                for i in range(len(lines)):
                    line = lines[i]
                    if("```" in line and flag == 0):
                        flag = 1
                        slist = line.split("```")
                        spaces = slist[0]
                        slen = len(spaces)
                        # print(len(spaces))
                        # 判断开始结束
                        # 判断前置空格数量
                        # print(line)
                    elif("```" in line and flag == 1):
                        lines[i] = line[slen:]
                        flag = 0

                    if(flag == 1 and slen > 0):
                        if(">>>" in line):
                            pass
                        elif(line[0:slen] != (' ' * slen)):
                            pass
                        else:
                            lines[i] = line[slen:]
                        # print(line)
                        # print(line[slen:])
                        # 去掉 slen  个空格

                myfile.close()
                myfile = open(fname, 'w')
                myfile.writelines(lines)
                myfile.close()





                # for line in myfile:
                #     if("```" in line and flag == 0):
                #         flag = 1
                #         slist = line.split("```")
                #         spaces = slist[0]
                #         slen = len(spaces)
                #         # print(len(spaces))
                #         # 判断开始结束
                #         # 判断前置空格数量
                #         # print(line)
                #     elif("```" in line and flag == 1):
                #         flag = 0

                    # if(flag == 1 and slen > 0):
                        # print(line)
                        # print(line[slen:])
                        # 去掉 slen  个空格

                # 关闭

        # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))


def main():
    walkFile("./")


if __name__ == '__main__':
    main()