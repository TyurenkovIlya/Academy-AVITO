import csv


def read_csv(file_path: str) -> list[dict[str, str]]:
    """
    Takes csv file and transforms it to list of dicts
    """
    employee_data = []
    with open(file_path, 'r', newline='', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        headers = next(csv_reader)
        for row in csv_reader:
            row_data = {key: value for key, value in zip(headers, row)}
            employee_data.append(row_data)
    return employee_data


def dep_hierarchy(raw_data: list[dict[str, str]]):
    """
    Takes list of dicts, find unique combinations
    and print department hierarchy
    """
    depts = {}
    for item in raw_data:
        if item['Департамент'] not in depts:
            depts[item['Департамент']] = []
        if item['Отдел'] not in depts[item['Департамент']]:
            depts[item['Департамент']].append(item['Отдел'])

    for key in depts.keys():
        print(f"{key}: {', '.join(depts[key])}")


def get_report_data(raw_data: list[dict[str, str]]) -> dict[str, dict]:
    """
    Takes list of dicts
    and transforms it to dict of dicts to the further use
    """
    dept_info = {}
    for item in raw_data:
        dept_info[item['Департамент']] = dept_info.get(item['Департамент'], {})
        print(dept_info[item['Департамент']])
        dept_info[item['Департамент']]['people'] = dept_info[item['Департамент']].get('people', 0) + 1
        if 'salary' not in dept_info[item['Департамент']].keys():
            dept_info[item['Департамент']]['salary'] = []
        dept_info[item['Департамент']]['salary'].append(int(item['Оклад']))

    for dept in dept_info:
        dept_info[dept]['salary_min'] = min(dept_info[dept]['salary'])
        dept_info[dept]['salary_max'] = max(dept_info[dept]['salary'])
        dept_info[dept]['salary_mean'] = round(sum(dept_info[dept]['salary']) / len(dept_info[dept]['salary']), 1)
    return dept_info


def show_report(report_data: dict[str, dict]):
    """
    Prints data as a report
    """
    print("{:<15} {:<15} {:<20} {:<10}".format('Департамент', 'Численность', 'Вилка', 'Средняя зарплата'))
    for name, info in report_data.items():
        people, salary, salary_min, salary_max, salary_mean = info.values()
        print("{:<15} {:<15} {:<20} {:<10}".format(name, people, str(salary_min) + ' - ' + str(salary_max), salary_mean))


def save_report(report_data: dict[str, dict]):
    """
    Saves report data as a csv
    """
    header = ['Департамент', 'Численность', 'Вилка', 'Средняя зарплата']
    with open('report.csv', 'w', newline='', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        for name, info in report_data.items():
            people, salary, salary_min, salary_max, salary_mean = info.values()
            salary_fork = str(salary_min) + '-' + str(salary_max)
            writer.writerow([name, people, salary_fork, salary_mean])
    print('Успешно сохранено в report.csv')


if __name__ == '__main__':
    data = read_csv("Corp_Summary.csv")

    print(
        '1. Вывести иерархию команд \n'
        '2. Вывести сводный отчёт по департаментам \n'
        '3. Сохранить сводный отчёт в виде csv-файла \n'
    )
    option = ''
    options = ['1', '2', '3']
    while option not in options:
        print('Введите: {} , {} или {}'.format(*options))
        option = input()

        if option == '1':
            dep_hierarchy(data)
        elif option == '2':
            show_report(get_report_data(data))
        elif option == '3':
            save_report(get_report_data(data))
        else:
            print('Неверный ввод. Попробуй еще раз.')
