# -*- coding: utf-8 -*-
#by liangwenhao
# 第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中
# 使用lxml
import codecs
from lxml import etree

def write_city_to_xml(dic=None, to_path=None):
    if dic is None or to_path is None:
        return None

    root_node = etree.Element('root')
    root_node.text = "\n\t"

    city_node = etree.SubElement(root_node, 'citys')

    comment_node = etree.Comment("\n城市信息\n")
    comment_node.tail = "\n\t"
    city_node.append(comment_node)

    city_node.text = "\n\t" + stringer.dict_to_json(dic, "\t") + u'\n'
    city_node.tail = "\n"

    city_tree = etree.ElementTree(root_node)
    city_tree.write(to_path, pretty_print=True, xml_declaration=True, encoding='utf-8')
    # output = codecs.open(to_path, 'w', 'utf-8')
    # output.write(etree.tounicode(city_tree.getroot()))
    # output.close()