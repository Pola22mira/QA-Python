import pytest
from string_utils import StringUtils 

stringUtils = StringUtils()


#   ПРОВЕРКА метода capitilize

@pytest.mark.parametrize('string, result', [
('text', 'Text'),
("текст", "Текст"),
("текст с пробелами", "Текст с пробелами"),
('123', '123')
])
def test_positive_capitilize(string, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [
([], []),
(['asd', 'dfg', 'dfg'], ['Asd', 'dfg', 'dfg']),
(123, 123)
])
def test_xxx777_capitilize(string, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == result
 

@pytest.mark.parametrize('string, result', [
('', ''),
(' ', ' ')
])
def test_empty_capitilize(string, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == result


@pytest.mark.parametrize('string, result', [
("текст. Длинный Текст", "Текст. Длинный Текст")  
])
def test_error_capitilize(string, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(string)
    assert res == result



#   ПРОВЕРКА метода trim

@pytest.mark.parametrize('string, result', [
(' asd', 'asd'),
(' Маша', 'Маша'),
('asd', 'asd'), #нет пробела вначале
(' "Маша"', '"Маша"'),
(' Маша и Миша', 'Маша и Миша'),
(' 123', '123'),
('', ''),
(' ', '')
])
def test_positive_trim(string, result):
    stringUtils = StringUtils()
    res = stringUtils.trim(string)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [
(123, 123),
(None, None)
])
def test_negative_trim(string, result):
    stringUtils = StringUtils()
    res = stringUtils.trim(string)
    assert res == result



#   ПРОВЕРКА метода to_list

@pytest.mark.parametrize('string, result', # разделитель - по умолчанию
[("a,b,c,d", ["a", "b", "c", "d"]),
("1,2,3", ["1", "2", "3"])])
def test_positive_to_list(string, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string)
    assert res == result
    

@pytest.mark.parametrize('string, delimeter, result', # с указанием разделителя
[("a.b.c.d", ".", ["a", "b", "c", "d"]),
("А, п, А, п", ", ", ["А", "п", "А", "п"]),
("А/п/А/#", "/", ["А", "п", "А", "#"])])
def test_positive2_to_list(string, delimeter, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string, delimeter)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, delimeter, result', [
("abcd", "", ["a", "b", "c", "d"]),
("А, п, А, п", ",", ["А", "п", "А", "п"]),
('', '',''),
(123, '',  ["1", "2", "3"]),
(["a", "b", "c", "d"], ',', ["a", "b", "c", "d"]),
([], ',', [])
])
def test_negative_to_list(string, delimeter, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string, delimeter)
    assert res == result



#   ПРОВЕРКА метода contains

@pytest.mark.parametrize('string, symbol, result', [
('Maria', 'a', True),
('Мария', 'ф', False),
("С пробелом@", '@', True),
("С пробелом@", ' ', True),
("Безпробела", ' ', False),
(" Пробел_вначале", ' ', True),
([], ' ', False), 
('123456', '3', True),
('', '', True)
])
def test_positive_contains(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    print(res)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
(123456, 3, True) 
])
def test_negative_contains(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)
    print(res)
    assert res == result



#   ПРОВЕРКА метода delete_symbol

@pytest.mark.parametrize('string, symbol, result', [
('Maria', 'a', 'Mri'),
('Maria', 'b', 'Maria'),
('Maria', 'aria', 'M'),
('Maria', 'Mari', 'a'),
('С пробелом ', ' ', 'Спробелом'), 
('С пробелом с пробелом', 'м с п', 'С пробелоробелом'),
('123', '1', '23'),
('Maria@', '@', 'Maria'),
('Maria@', 'М@', 'Maria@'), #символы подстроки не по порядку
('', '', '')
])
def test_positive_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
(None, None, None),  
(123, 2, 13)
])
def test_negative_delete_symbol(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result



#   ПРОВЕРКА метода starts_with

@pytest.mark.parametrize('string, symbol, result', [
('Maria', 'M', True),
('Maria', 'b', False),
('123456', '1', True),
(' Maria', ' ', True), 
('#Maria', '#', True),
(' ', ' ', True)
])
def test_positive_starts_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
(123456, 1, True),
('123456', 1, True)
])
def test_negative_starts_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == result



#   ПРОВЕРКА метода end_with

@pytest.mark.parametrize('string, symbol, result', [
('Maria', 'a', True),
('Maria', 'f', False),
('Maria ', ' ', True),
('123450', '0', True),
('12345@', '@', True),
('', '', True),
(' ', ' ', True)
])
def test_positive_end_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, symbol, result', [
(12345, 5, True)
])
def test_negative_end_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == result



#   ПРОВЕРКА метода is_empty

@pytest.mark.parametrize('string, result', [
('',  True),
(' ',  True),
('Maria', False) 
])
def test_positive_is_empty(string, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == result


@pytest.mark.xfail
@pytest.mark.parametrize('string, result', [([],  True), (None, None)])
def test_negative_is_empty(string, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(string)
    assert res == result



#   ПРОВЕРКА метода list_to_string

@pytest.mark.parametrize('list, result', [
(["a", "b", "c", "d"], "a, b, c, d"),
(["1", "2"], "1, 2"),
([1, 2], "1, 2"),
([], ""),
([ ], "")
])
def test_positive_list_to_string(list, result): #joiner по умолчанию
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(list)
    assert res == result


@pytest.mark.parametrize('list, joiner, result', [
(["a", "b", "c"], ".", "a.b.c"),
(["a", "b", "c"], "/", "a/b/c"),
(["a", "b", "c"], "", "abc"),
(["a", "b", "c"], " ", "a b c"),
([1,2,3,4], " asd-asd ", "1 asd-asd 2 asd-asd 3 asd-asd 4"),
([1, "b", "c"], "#", "1#b#c"),
([3, "b", [1,2,3]], ".", "3.b.[1, 2, 3]")
])
def test_positive_joiner_ist_to_string(list, joiner, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(list, joiner)
    assert res == result