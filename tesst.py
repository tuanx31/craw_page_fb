def convert_to_number(string):
    if 'K' in string:
        a = string.replace('K', '')
        a = a.replace(',', '.')  # Thay dấu phẩy bằng dấu chấm
        number = float(a) * 1000
    else:
        a = string.replace(',', '.')  # Thay dấu phẩy bằng dấu chấm
        number = float(a)
    return int(number)

print(convert_to_number("16,7K"))
