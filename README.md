# user-info-manager

# User Info Form Project

A simple full-stack web application where users can enter personal information through a form and view the submitted data.

## Project Structure

```
user_info_project/
│
├── backend/
│   ├── main.py                # FastAPI app
│   └── requirements.txt       # Backend dependencies
│
├── frontend/
│   ├── app.py                 # Streamlit app
│   └── requirements.txt       # Frontend dependencies
│
└── README.md                  # This file
```

## How to Run the Project

### Backend Setup

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

The backend will be available at `http://127.0.0.1:8000`.

### Frontend Setup

1. Navigate to the frontend folder:
   ```bash
   cd ../frontend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

The frontend will open in your browser at `http://localhost:8501`.

## Step 5: Test the Application

1. Open the Streamlit app in your browser (`http://localhost:8501`)
2. Fill out the form with your information
3. Click "Submit"
4. Verify that:
   - You see a success message
   - Your submitted information appears below the form
   - The data matches what you entered

## Accessing the Application

- Backend API: http://localhost:8000
- Frontend UI: http://localhost:8501

## Database

- SQLite database file will be created automatically in the backend directory
- Database file: user_info.db

## How It All Works at Level-1

Let me explain the key components and their interactions:

1. **Frontend (Streamlit)**:
   - Creates a form with all required fields
   - Handles form submission and validation
   - Sends data to the backend via HTTP POST request
   - Displays the response from the backend

2. **Backend (FastAPI)**:
   - Provides two endpoints:
     - POST `/submit_user_info/` - receives and stores user data
     - GET `/get_user_info/` - returns the stored user data
   - Uses Pydantic models for data validation
   - Implements CORS to allow cross-origin requests from the frontend

3. **Communication Flow**:
   - When you submit the form, Streamlit sends a POST request to FastAPI
   - FastAPI receives the data, stores it in memory, and returns it
   - Streamlit then makes a GET request to display the stored data

4. **Validation**:
   - Both client-side (in Streamlit) and server-side (in FastAPI via Pydantic) validation
   - Checks for required fields, valid age, proper pincode format, etc.

## Bonus Features Implemented

I've included all the optional bonus features you mentioned:
1. **Form validation** - checks for required fields and valid inputs
2. **Loading indicator** - shows a spinner during submission
3. **Nice formatting** - displays the data in a clean JSON format (with commented alternative for more styled display)

## Next Steps for Learning

To deepen your understanding, you could:
1. Add more fields to the form
2. Implement proper error handling for the API calls
3. Add unit tests for both frontend and backend
4. Replace the in-memory storage with a real database
5. Deploy the application (e.g., Streamlit Cloud for frontend, Render for backend)

This project gives you a solid foundation in building full-stack applications with Python. The concepts you've learned here (API communication, form handling, validation) are fundamental to web development.

## Level-2 : 


## Key Improvements in Level 2

1. **Database Integration**:
   - SQLite database with SQLAlchemy ORM
   - Automatic table creation
   - Persistent data storage

2. **Full CRUD Operations**:
   - **Create**: Add new users via form
   - **Read**: Display all users in a table with search/filter
   - **Update**: Edit existing users
   - **Delete**: Remove users with confirmation

3. **Enhanced UI**:
   - Two-column layout (form + user list)
   - Edit mode detection
   - Confirmation dialogs
   - Search and filter functionality
   - Expandable user details

4. **State Management**:
   - Streamlit session state for form data
   - Edit mode tracking
   - Current user selection

5. **Validation**:
   - Form field validation
   - Error handling
   - User feedback

## Bonus Features Implemented

1. **Form validation** for all required fields
2. **Confirmation dialog** before deletion
3. **Gender filtering** in user list
4. **Search functionality** by name
5. **Session state management** for form mode (Add/Edit)
6. **Responsive layout** with columns
7. **Visual feedback** with success/error messages

## Testing the Application

1. Start the backend: `uvicorn main:app --reload` in backend directory
2. Start the frontend: `streamlit run app.py` in frontend directory
3. Test each CRUD operation:
   - Create several users
   - Edit a user's information
   - Delete a user (with confirmation)
   - Use search and filter options
4. Verify data persists after restarting the application

This implementation provides a complete CRUD application with database persistence, giving you a solid foundation for building more complex applications. The code includes detailed comments to help you understand each component's functionality.
