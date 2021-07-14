from cases.anki.cleam_html import trim_br, remove_span, decode_html_specials, remove_multiple_br, remove_multiple_space


def assert_func(func, source, expected):
    a = func(source)
    print(a)
    assert a == expected


def test_trim_br():
    assert_func(trim_br, '<br><br>line1<br>line2', 'line1<br>line2')
    assert_func(trim_br, 'line1<br>line2<br><br>', 'line1<br>line2')
    assert_func(trim_br, '<br><br>line1<br>line2<br><br>', 'line1<br>line2')

    assert_func(trim_br, '<br><aaa>line1<br>line2<br><br>', '<aaa>line1<br>line2')

    assert_func(trim_br, '<BR><br>line1<br>line2<BR><br>', 'line1<br>line2')

    assert_func(trim_br, '<br/><br/>line1<br/>line2', 'line1<br/>line2')
    assert_func(trim_br, 'line1<br/>line2<br/><br/>', 'line1<br/>line2')
    assert_func(trim_br, '<br/><br/>line1<br/>line2<br/><br/>', 'line1<br/>line2')

    assert_func(trim_br, '<br><br/>line1<br/>line2<br><br/>', 'line1<br/>line2')
    assert_func(trim_br, '<br/><br>line1<br/>line2<br/><br>', 'line1<br/>line2')
    assert_func(trim_br, '<br><br />line1<br/>line2<br><br />', 'line1<br/>line2')
    assert_func(trim_br, '<br /><br>line1<br/>line2<br /><br>', 'line1<br/>line2')


def test_remove_multiple_br():
    func = remove_multiple_br
    assert_func(func, '<br>', '<br>')
    assert_func(func, '<br><br>', '<br><br>')
    assert_func(func, '<br><br><br>', '<br><br>')
    assert_func(func, '<br><br><br/><br>', '<br><br>')
    assert_func(func, 'text<br><br><br/><br>text', 'text<br><br>text')


def test_remove_multiple_spaces():
    func = remove_multiple_space
    assert_func(func, ' ', ' ')
    assert_func(func, '  ', ' ')
    assert_func(func, '   ', ' ')
    assert_func(func, 'text   text', 'text text')


def test_remove_span():
    assert_func(remove_span, '<span>a', 'a')
    assert_func(remove_span, '</span>a', 'a')
    assert_func(remove_span, '<span>a</span>', 'a')
    assert_func(remove_span, '<span>line</span>', 'line')
    assert_func(remove_span, 'line<span>line</span>line', 'linelineline')

    assert_func(remove_span, '<span style="background-color: rgba(255, 255, 255, 0.9);">', '')
    assert_func(remove_span, '</span><span style="background-color: rgba(255, 255, 255, 0.9);">', '')


def test_decode_html_special():
    assert_func(decode_html_specials, '&nbsp;a', ' a')


if __name__ == "__main__":
    test_trim_br()
    test_remove_multiple_br()
    test_remove_multiple_spaces()
    test_remove_span()
    test_decode_html_special()
    print("Everything passed")
