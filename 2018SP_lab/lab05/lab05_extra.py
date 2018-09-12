""" Optional questions for Lab 05 """

from lab05 import *

# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:
            table[prev] = [tokens[index] for index in [i+1 for i,v in enumerate(tokens) if v==prev]]
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        result += word
        word = random.choice(table[word])
        result += ' '
    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
# tokens = shakespeare_tokens()
# table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)

# Q8
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    def delete_leaf(t, delete):
        if is_tree(t):
            head = label(t)
            if is_tree(head) and is_leaf(head):
                # 调用branch函数时，返回结果可能会出现嵌套叶子结点，如[['thor']]
                if head == [delete] or head == [[delete]]:
                    return delete_leaf(branches(t), delete)
                else:
                    return tree(head, delete_leaf(branches(t), delete))
            elif is_tree(head):
                left = tree(delete_leaf(label(head), delete), 
                            delete_leaf(branches(head), delete))
                right = delete_leaf(branches(t), delete) 
                return tree(left, right)
            else: 
                return tree(head, delete_leaf(branches(t), delete))
        else:
            return t
    for elem in vals:
        if t == [elem]:
            return
        elif is_tree(t):
            t = delete_leaf(t, elem)
    if not is_tree(t):
        return
    return t

# Q9
def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    >>> t3 = tree(0, [tree(1, [tree(2, [tree(3)])])])
    >>> print_tree(t3)
    0
      1
        2
          3
    >>> new3 = sprout_leaves(t3, [6, 1, 2])
    >>> print_tree(new3)
    0
      1
        2
          3
            6
            1
            2
    """
    if is_tree(t):
        if len(t) == 2:
        # 调用branch函数(切片)时，当t的长度为2时，返回结果为[tail](tail为最后一个元素)
        # 是一个嵌套列表,tail才是要求的，重新组成树时不要忘了给right外面嵌套列表
            left = sprout_leaves(label(t), vals)
            right = sprout_leaves(t[1], vals)
            return tree(left, tree(right))
        elif is_leaf(t):
            v = [tree(x) for x in vals]
            return tree(label(t), v)
        else:
            left = sprout_leaves(label(t), vals)
            right = sprout_leaves(branches(t), vals)
            return tree(left, right)
    else:
        return t


# Q10
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if is_tree(t2):
        if len(t1) == 2:
        # 调用branch函数(切片)时，当t的长度为2时，返回结果为[tail](tail为最后一个元素)
        # 是一个嵌套列表,里面的列表才是要求的，重新组成树时不要忘了给right外面嵌套列表
            left = add_trees(label(t1), label(t2))
            right = add_trees(t1[1], t2[1])
            return tree(left, tree(right))
        elif is_leaf(t1):
            result = tree(t1[0]+t2[0])
            return result
        else:
            left_left = label(t1)
            left_right = label(t2)
            left = add_trees(left_left, left_right)
            right_left = branches(t1)
            right_right = branches(t2)
            right = add_trees(right_left, right_right)
            result = tree(left, right)
            return result
    elif int(t1):
        result = t1 + t2
        return result
    else:
        return t2
