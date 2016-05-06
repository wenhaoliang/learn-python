# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中
def write_numbers_to_xml(list=None, to_path=None):
     if list is None or to_path is None:
        return None

     root_node = etree.Element('root')
     root_node.text = "\n\t"

     number_node = etree.SubElement(root_node, 'numbers')

     comment_node = etree.Comment("\n数字信息\n")
     comment_node.tail = "\n\t"
     number_node.append(comment_node)

     number_node.text = "\n\t" + stringer.list_to_json(list, "\t") + u'\n'
     number_node.tail = "\n"

     number_tree = etree.ElementTree(root_node)
     number_tree.write(to_path, pretty_print=True, xml_declaration=True, encoding='utf-8')
