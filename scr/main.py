def get_less_avg(list_numbers):
    avg = sum(list_numbers) / len(list_numbers)
    new_list = []
    for number in list_numbers:
       if number < avg:
           new_list.append(number)
    return new_list