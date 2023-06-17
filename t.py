def convert_views_to_number(views_str):
    views_str = views_str.replace(" lượt xem", "")  # Loại bỏ " lượt xem" từ chuỗi
    if "K" in views_str:
        if ',' in views_str:
            views_str = views_str.replace(",", "")
            views_str = views_str.replace("K", "")
            views = float(views_str) * 100
        else:
            views_str = views_str.replace("K", "")
            views = float(views_str) * 1000
    else:
        views = int(views_str)
    return int(views)

string = "49K lượt xem"
converted_number = convert_views_to_number(string)
print(converted_number)  # Kết quả: 4900
