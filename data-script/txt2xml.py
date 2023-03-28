# D:\Anaconda3\python.exe
# -*- coding = utf-8 -*-
# @Time : 2022/11/28 10:53
# @Author : L_PenguinQAQ
# @File : txt2xml.py
# @Software: PyCharm
# @function: txt文件转换为xml文件

import os
from xml.dom.minidom import Document

import cv2


def makexml(txtPath, xmlPath, picPath):  # 读取txt路径，xml保存路径，数据集图片所在路径
    dict = {'0': "crack"}
    files = os.listdir(txtPath)
    for i, name in enumerate(files):
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)
        txtFile = open(txtPath + name)
        txtList = txtFile.readlines()
        if name[0:-4] != 'scrip':
            print(picPath + name[0:-4] + ".jpg")
            img = cv2.imread(picPath + name[0:-4] + ".jpg")
        Pheight, Pwidth, Pdepth = img.shape
        flag = 0
        for i in txtList:
            flag += 1
            oneline = i.strip().split(" ")
            folder = xmlBuilder.createElement("folder")  # folder标签
            folderContent = xmlBuilder.createTextNode("images")
            folder.appendChild(folderContent)
            annotation.appendChild(folder)
            if flag == 1:
                filename = xmlBuilder.createElement("filename")  # filename标签
                filenameContent = xmlBuilder.createTextNode(name[0:-4] + ".jpg")
                filename.appendChild(filenameContent)
                annotation.appendChild(filename)

                size = xmlBuilder.createElement("size")  # size标签
                width = xmlBuilder.createElement("width")  # size子标签width
                widthContent = xmlBuilder.createTextNode(str(Pwidth))
                width.appendChild(widthContent)
                size.appendChild(width)
                height = xmlBuilder.createElement("height")  # size子标签height
                heightContent = xmlBuilder.createTextNode(str(Pheight))
                height.appendChild(heightContent)
                size.appendChild(height)
                depth = xmlBuilder.createElement("depth")  # size子标签depth
                depthContent = xmlBuilder.createTextNode(str(Pdepth))
                depth.appendChild(depthContent)
                size.appendChild(depth)
                annotation.appendChild(size)

            object = xmlBuilder.createElement("object")
            picname = xmlBuilder.createElement("name")
            print(dict[oneline[0]], oneline[0])
            nameContent = xmlBuilder.createTextNode(dict[oneline[0]])
            picname.appendChild(nameContent)
            object.appendChild(picname)
            pose = xmlBuilder.createElement("pose")
            poseContent = xmlBuilder.createTextNode("Unspecified")
            pose.appendChild(poseContent)
            object.appendChild(pose)
            truncated = xmlBuilder.createElement("truncated")
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)
            difficult = xmlBuilder.createElement("difficult")
            difficultContent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultContent)
            object.appendChild(difficult)
            bndbox = xmlBuilder.createElement("bndbox")
            xmin = xmlBuilder.createElement("xmin")
            mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            xminContent = xmlBuilder.createTextNode(str(mathData))
            xmin.appendChild(xminContent)
            bndbox.appendChild(xmin)
            ymin = xmlBuilder.createElement("ymin")
            mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            yminContent = xmlBuilder.createTextNode(str(mathData))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)
            xmax = xmlBuilder.createElement("xmax")
            mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            xmaxContent = xmlBuilder.createTextNode(str(mathData))
            xmax.appendChild(xmaxContent)
            bndbox.appendChild(xmax)
            ymax = xmlBuilder.createElement("ymax")
            mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            ymaxContent = xmlBuilder.createTextNode(str(mathData))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)
            object.appendChild(bndbox)

            annotation.appendChild(object)

        f = open(xmlPath + name[0:-4] + ".xml", 'w')
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()


makexml("./concreteCrackSet/labels/", "./concreteCrackSet/temp_xmls/", "./concreteCrackSet/images/")
