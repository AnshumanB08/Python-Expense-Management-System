import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger


logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s;", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s;", (expense_date,))


def insert_expenses(expense_date, amount, category, notes):
    logger.info(
        f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s);",
            (expense_date, amount, category, notes)
        )


def fetch_expense_summary_category(start_date, end_date):
    logger.info(f"fetch_expense_summary_category called with start: {start_date} end: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT category, SUM(amount) AS total
            FROM expenses 
            WHERE expense_date 
            BETWEEN %s AND %s
            GROUP BY category;
            ''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data


def fetch_expense_summary_monthly():
    logger.info(f"fetch_expense_summary_monthly called")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                MONTH(expense_date) AS month,
                MONTHNAME(expense_date) AS month_name, 
                SUM(amount) as total
            FROM expenses
            GROUP BY month
            ORDER BY month;
            '''
        )
        data = cursor.fetchall()
        return data



if __name__ == "__main__":
    # expense = fetch_expenses_for_date("2024-08-01")
    # for e in expense:
    #     print(e)

    # insert_expenses("2024-08-25", 40, "Food", "Eat tasty samosa chat")

    # delete_expenses_for_date("2024-08-25")

    # summary = fetch_expense_summary_category("2024-08-01", "2024-08-05")
    # for record in summary:
    #     print(record)

    summary = fetch_expense_summary_monthly()
    for record in summary:
        print(record)