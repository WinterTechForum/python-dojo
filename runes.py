#!/usr/bin/env python3

"""
Simple example::


"""

def getlines():
    with open('UnicodeData.txt') as fp:
        lines = fp.readlines()
    return lines

def splitline(line:str):
    '''Breaks the line on the semicolons

        >>> splitline('a;b;c')
        ['a', 'c']

    '''
    return line.split(';')[:2]

def matchline(query, line):
    query_set = set(query.upper().split())
    line_set = set(line.split())

    return query_set <= line_set

def matchlines(query, lines):
    # results = []
    for line in lines:
        code, codepoint_name = splitline(line)
        if matchline(query, codepoint_name):
            # results.append((code, codepoint_name))
            yield (code, codepoint_name)
    # return results

def main(args):
    query = ' '.join(args)
    for code, codepoint_name in matchlines(query, getlines()):
        print(chr(int(code, 16)), codepoint_name)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])