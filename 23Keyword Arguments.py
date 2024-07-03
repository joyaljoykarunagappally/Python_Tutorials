# keyword arguments = arguments proceed by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments.
#                     Python knows the names of the arguments that our function receives


def fullname(f_name, m_name, l_name):
    print("hello " + f_name + " " + m_name + " " + l_name)


fullname(l_name="Joy", f_name="Joyal", m_name="B")
