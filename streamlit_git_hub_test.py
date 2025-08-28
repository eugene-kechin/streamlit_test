
%%writefile app.py

import streamlit as st
import pandas as pd
import numpy as np

# Функция для вычисления третьего числа на основе двух введенных чисел
@st.cache_data
def calculate_third_number(numbers):
    # Здесь должна быть логика вычисления третьего числа
    return np.array(numbers[:, 0]) + np.array(numbers[:, 1])

# Создание веб-приложения
st.set_page_config(layout="wide")

# Заголовок приложения
st.title("Вычисление третьего числа")

# Инициализация DataFrame для хранения результатов
results_df = pd.DataFrame(columns=["Число 1", "Число 2", "Результат"])

how_data = st.number_input("Сколько данных", min_value=1)
numbers = []
for i in range(int(how_data) * 2):
# Ввод первого числа
    number = st.number_input(label=f"Введите {i+1} число")

# Ввод второго числа
    #second_number = st.number_input(label=f"Введите {i+2} число")
    numbers.append(number)

#button_calculate = st.button('Вычислить третье число')
#if button_calculate:
numbers = np.resize(np.array(numbers), (int(how_data), 2))

res_num = calculate_third_number(numbers)

results_df = pd.DataFrame(np.column_stack([numbers, res_num]), index=[f"Наблюдение {i + 1}" for i in range(int(how_data))], columns=["Число 1", "Число 2", "Результат"])
#results_df = pd.concat([results_df, pd.DataFrame({'First Number': [first_number], 'Second Number': [second_number], 'Third Number': [third_number]})], ignore_index=True)

# Кнопка для вычисления третьего числа
#button_calculate = st.button('Вычислить третье число')

# Проверка нажатия кнопки
#if button_calculate:
    # Вычисление третьего числа
    #third_number = calculate_third_number(first_number, second_number)

    # Добавление нового ряда в DataFrame

#    results_df = pd.concat([results_df, pd.DataFrame({'First Number': [first_number], 'Second Number': [second_number], 'Third Number': [third_number]})], ignore_index=True)

    #results_df = results_df.append({'First Number': first_number, 'Second Number': second_number, 'Third Number': third_number}, ignore_index=True)



# Кнопка для скачивания DataFrame в формате Excel
button_download = st.button('Скачать результаты в формате Excel')

# Проверка нажатия кнопки скачивания
if button_download:
    #results_df = results_df.reset_index(names='Номер наблюдения')
    # Скачивание DataFrame в формате Excel
    results_df.to_excel('results.xlsx')


# Отображение результатов в DataFrame
st.dataframe(results_df)