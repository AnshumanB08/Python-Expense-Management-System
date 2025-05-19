from backend import db_helper


def test_fetch_expenses_for_date_aug_15():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    if expenses:
        assert len(expenses) == 1
        assert expenses[0]["amount"] == 10.0
        assert expenses[0]["category"] == "Shopping"
        assert expenses[0]["notes"] == "Bought potatoes"
    else:
        print("No expenses found for the given data")


def test_fetch_expenses_for_date_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")

    if expenses:
        assert len(expenses) == 0
    else:
        print("Expenses has valid date")


def test_fetch_expense_summary_category_invalid_range():
    summary = db_helper.fetch_expense_summary_category("2099-01-01", "2099-12-31")

    if summary:
        assert len(summary) == 0
    else:
        print("Expenses has valid range")


def test_fetch_expense_summary_monthly_invalid_year():
    summary = db_helper.fetch_expense_summary_monthly("9999")

    if summary:
        assert len(summary) == 0
    else:
        print("Expenses has valid year")