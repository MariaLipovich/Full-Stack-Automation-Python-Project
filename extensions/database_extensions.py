import allure

import test_cases.conftest as conf


class DatabaseExtensions:

    @staticmethod
    @allure.step('Build a query')
    def get_query(col_names, table_name, where_col, where_value):
        col = ','.join(col_names)
        query = "SELECT " + col + " FROM " + table_name + " WHERE " + where_col + " = '" + where_value + "'"
        return query

    @staticmethod
    @allure.step('Get data from a database')
    def get_data(col_names, table_name, where_col, where_value):
        get_query = DatabaseExtensions.get_query(col_names, table_name, where_col, where_value)
        cursor = conf.connectorDB.cursor()
        cursor.execute(get_query)
        result = cursor.fetchall()
        return result
