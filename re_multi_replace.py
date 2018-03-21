# coding=utf-8

import re


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


if __name__ == '__main__':
    text = "Larry Wall is the creator of  Perl"
    adict = {
        "Larry Wall": "Guido van Rossum",
        "creator": "Benevolent  Dicator for Life",
        "Perl": "Python",
    }
    print(multiple_replace(text, adict))
    print(r'\b%s\b' % r'\b|\b'.join(map(re.escape, adict)))

    inputStr = "hello 12 world 456"

    def _add111(matched):
        intStr = matched.group("number")  # 123
        intValue = int(intStr)
        addedValue = intValue + 111  # 234
        addedValueStr = str(addedValue)
        return addedValueStr

    replacedStr = re.sub("(?P<number>\d{3})", _add111, inputStr)
    print("replacedStr=", replacedStr)  # hello 234 world 567
