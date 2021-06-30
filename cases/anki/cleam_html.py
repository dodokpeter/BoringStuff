import regex as re


def clean_html(source_html):
    target = source_html.strip()
    target = trim_br(target)
    target = remove_span(target)
    target = decode_html_special(target)
    return target


def lregstrip(string, pattern):
    return re.sub(r'(?:^(' + pattern + ')+)', '', string, flags=re.IGNORECASE)


def rregstrip(string, pattern):
    return re.sub(r'(?:(' + pattern + ')+$)', '', string, flags=re.IGNORECASE)


def reg_strip(string, pattern=' \n\r\t\f\v'):
    return rregstrip(lregstrip(string, pattern), pattern)


def reg_remove(string, pattern=' \n\r\t\f\v'):
    return re.sub(r'(?:(' + pattern + ')+)', '', string, flags=re.IGNORECASE)


def reg_change(string, _from, _to ):
    return re.sub(r'(?:(' + _from + ')+)', _to, string, flags=re.IGNORECASE)


# remove occurrence of BR tag from start and end
def trim_br(source):
    return reg_strip(source, '(<br)[ a-zA-Z/]*(>)')


# remove span tag
def remove_span(source):
    # this \- is causing that the regex is underline in ide
    return reg_remove(source, '(<)[ /]*(span)[ a-zA-Z0-9/=\-.,:;()&\"\']*(>)')


# &nbsp; to space
def decode_html_special(source):
    return reg_change(source, '&nbsp;', ' ')
