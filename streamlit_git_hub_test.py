import streamlit as st
import pandas as pd
import numpy as np
import io



@st.cache_data
def calculate_third_number(numbers):
    return np.array(numbers[:, 0]) + np.array(numbers[:, 1])

st.set_page_config(layout="wide")

st.title("Калькулятор для вычисления суммы двух положительных чисел")


def main():

    results_df = pd.DataFrame(columns=["Число 1", "Число 2", "Результат"])

    how_data = st.number_input("Сколько данных", min_value=1)
    numbers = []
    for i in range(int(how_data) * 2):
        number = st.number_input(label=f"Введите {i+1} число", value=0.00, step=0.01)
        numbers.append(number)

    numbers = np.resize(np.array(numbers), (int(how_data), 2))
    res_num = calculate_third_number(numbers)
    results_df = pd.DataFrame(np.column_stack([numbers, res_num]), index=[f"Наблюдение {i + 1}" for i in range(int(how_data))], columns=["Число 1", "Число 2", "Результат"])


    # Отображение результатов в DataFrame
    st.dataframe(results_df)

if __name__ == "__main__":
    main()


