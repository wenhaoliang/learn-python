# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
# 使用DOM
from tools import stringer
from xml.dom.minidom import Document

def write_student_to_xml(dic=None, to_path=None):
    if dic is None or to_path is None:
        return None

    doc = Document()
    root_node = doc.createElement("root")
    doc.appendChild(root_node)

    stu_node = doc.createElement("students")
    root_node.appendChild(stu_node)

    note_node = doc.createComment("\n\t学生信息表\n\t\"id\" : [名字, 数学, 语文, 英文]\n\t")
    stu_node.appendChild(note_node)

    # data = json.dumps(dic, ensure_ascii=False, indent=1)
    dic_node = doc.createTextNode(stringer.dict_to_json(dic, "\t\t"))
    stu_node.appendChild(dic_node)

    file = open(to_path, "w")
    file.write(doc.toprettyxml())
    # doc.writexml(file,'    ','    ','\n','utf-8')
    file.close()