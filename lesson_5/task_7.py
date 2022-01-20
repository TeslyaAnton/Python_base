import json

with open('answer_firm.json', 'w', encoding='utf-8') as write_ans:
    with open('firm.txt', encoding='utf-8') as my_file:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_file}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                           len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, write_ans, ensure_ascii=False, indent=4)