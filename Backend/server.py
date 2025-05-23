from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel


app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)

    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database!")

    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses: List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for e in expenses:
        db_helper.insert_expenses(expense_date, e.amount, e.category, e.notes)

    return {"message": "Expenses updated successfully"}


@app.post("/analytics_by_category/")
def get_analytics_by_category(date_range: DateRange):
    data = db_helper.fetch_expense_summary_category(date_range.start_date, date_range.end_date)

    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary by categories from the database!")

    grand_total = sum([row["total"] for row in data])
    breakdown = {}
    for row in data:
        percentage = (row["total"]/grand_total)*100 if grand_total != 0 else 0
        breakdown[row["category"]] = {
            "total": row["total"],
            "percentage": percentage
        }

    return breakdown


@app.get("/analytics_by_months")
def get_analytics_by_months():
    data = db_helper.fetch_expense_summary_monthly()

    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary by months from the database!")

    return data