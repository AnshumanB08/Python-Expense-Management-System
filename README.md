# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **Frontend/**: Contains the Streamlit application code.
- **Backend/**: Contains the FastAPI backend server code.
- **Tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Python-Expense-Management-System.git
   
   cd Python-Expense-Management-System
   ```
2. **Install dependencies:**:   
   ```commandline
   pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**:   
   ```commandline
   cd Backend
   
   uvicorn server:app --reload
   ```
4. **Run the Streamlit app:**:   
   ```commandline
   cd Frontend
   
   streamlit run ./app.py
   ```
