# -*- coding: utf-8 -*-

"""
3.9 中缀前缀和后缀表达式
"""

from __future__ import print_function

from py_3_5_stack import Stack


def infix_to_postfix(infix_expr):
    """
    中缀表达式 -> 后缀表达式
    :param infix_expr: 这里的中缀表达式是一个由空格分隔的标记字符串
    """

    # 用一个字典来保存操作符的优先级
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    tokens = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    op_stack = Stack()      # 创建一个空栈以保存运算符
    postfix_list = []
    infix_list = infix_expr.split()

    for token in infix_list:
        if token in tokens:
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            # 如果标记是右括号，则弹出 op_stack，直到删除相应的左括号。
            # 将每个运算符附加到输出列表的末尾。
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            # 如果标记是运算符：
            # 首先删除已经在 op_stack 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中
            # 再将此运算符压入 op_stack
            while (not op_stack.is_empty()) and \
                    (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    # 最后，检查 op_stack，仍然在栈上的任何运算符都可以删除并加到输出列表的末尾
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return ''.join(postfix_list)


def test_infix_to_postfix():
    print(infix_to_postfix("A * ( B + C ) * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


def do_math(op, op1, op2):
    """
    执行数学运算
    :param op:  操作符
    :param op1: 操作数1
    :param op2: 操作数2
    """
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2


def postfix_eval(postfix_expr):
    """
    后缀表达式求值

    如果 token 是操作数，将其从字符串转换为整数，并将值压到operandStack。

    如果 token 是运算符*，/，+或-，它将需要两个操作数。弹出operandStack 两次。
    第一个弹出的是第二个操作数，第二个弹出的是第一个操作数。执行算术运算后，
    将结果压到操作数栈中。

    :param postfix_expr: 这里的后缀表达式是一个由空格分隔的标记(token)字符串
    """

    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in '0123456789':
            operand_stack.push(int(token))
        else:
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            result = do_math(token, op1, op2)
            operand_stack.push(result)

    return operand_stack.pop()


def test_postfix_eval():
    print(postfix_eval('7 8 + 3 2 + /'))


if __name__ == '__main__':
    test_infix_to_postfix()
    test_postfix_eval()


