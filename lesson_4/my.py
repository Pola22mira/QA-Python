'''def capitilize(string: str) -> str:
    print(string.capitalize())
    
capitilize('текст Длинный Текст. Длинный')'''

    
#@pytest.mark.skip(reason = "пропустить пока")  #пропустить тест

def list_to_string(lst: list, joiner=", ") -> str:
        string = ""
        length = len(lst)
        
        if length == 0: 
            return string 
        
        for i in range(0, length-1):
            string += str(lst[i]) + joiner
        
        print(string + str(lst[-1]))
        return string + str(lst[-1])

list_to_string(["Sky", "Pro"], '')


'''
#python_functions = *sum*
#python_functions = test_div_by_zero

markers =
    positive_test: только позитивные тесты
    auth test: тесты нв авторизацию

#python_functions = test_sum_positive_nums

#@pytest.mark.skip(reason = "пропустить пока")  #пропустить тест
'''