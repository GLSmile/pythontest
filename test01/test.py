
__authotr__='bobby'
# .代表任意字符  ,
# ?代表非贪婪匹配 ，默认情况是贪婪匹配模式，即为字符串默认匹配最长的长度,反向匹配的

import re

line1='boooo1oo000by123'
regex_str=".*(b.*b).*"   #(b.*b)  括号代表取子串 ，这种就是贪婪的匹配模式，得到“boooo1oo000b",
                         # 从规则左边开始匹配，不管前面或者后面有什么只取两个b之间的信息
match_obj=re.match(regex_str,line1)
if match_obj:
    print("match_obj1:",match_obj.group(1))

# .......................
line2='boooo1oobb1bbby123'
regex_str2=".*?(b.*?b).*"  # .*? ,*?b 从左往右开始匹配,非贪婪模式，找到了就不要再匹配了
                        #  这样就得到  boooo1oob
#regex_str2=".*?(b.*b).*"   #这样就得到  boooo1oobb1bbb

#regex_str2=".*(b.+b).*"   # + ，这个加号代表出现的字符至少出现一次
                          #  这样就得到  bbb
match_obj2=re.match(regex_str2,line2)
if match_obj2:
    print("match_obj2:",match_obj2.group(1))

'''
# 深度优先过程（递归调用）
def depth_tree(tree_node):
    if tree_node is not None:
        print(tree_node._data)
        if tree_node._left is not None:
            return depth_tree(tree_node._left)
        if tree_node._right is not None:
            return depth_tree(tree_node._right)

#广度优先过程(二叉树的遍历方式实现)
def level_queue(root):
   # 利用队列实现树的广度优先遍历
    if root is None:
        return
    my_queue = [ ]
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.pop(0)
        print(node.elem)
        if node.lchild is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)

'''