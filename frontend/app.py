import streamlit as st
import requests
import time
from datetime import datetime
import os

# Configure the app
st.set_page_config(page_title="User Info Manager", page_icon="👤", layout="wide")

# FastAPI backend URL
# BACKEND_URL = "http://127.0.0.1:8000"
# Get backend URL from environment variable or use localhost as default
BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000")

# Initialize session state
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False
    st.session_state.current_user = None
    st.session_state.form_data = {
        "name": "",
        "age": 0,
        "gender": "",
        "pincode": "",
        "address": ""
    }
    st.session_state.confirm_delete = {}

def reset_form():
    """Reset form to default values"""
    st.session_state.form_data = {
        "name": "",
        "age": 0,
        "gender": "",
        "pincode": "",
        "address": ""
    }
    st.session_state.edit_mode = False
    st.session_state.current_user = None

def load_users():
    """Retrieve all users from backend"""
    try:
        response = requests.get(f"{BACKEND_URL}/users/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading users: {e}")
        return []

def create_user(user_data):
    """Send new user data to backend"""
    try:
        response = requests.post(
            f"{BACKEND_URL}/users/",
            json=user_data
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error creating user: {e}")
        return None

def update_user(user_id, user_data):
    """Update existing user in backend"""
    try:
        response = requests.put(
            f"{BACKEND_URL}/users/{user_id}",
            json=user_data
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating user: {e}")
        return None

def delete_user(user_id):
    """Delete user from backend"""
    try:
        response = requests.delete(f"{BACKEND_URL}/users/{user_id}")
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting user: {e}")
        return False

def validate_form(name, age, gender, pincode, address):
    """Validate form inputs"""
    errors = []
    
    if not name:
        errors.append("Name is required")
    if age <= 0:
        errors.append("Age must be greater than 0")
    if not gender:
        errors.append("Gender is required")
    if not pincode:
        errors.append("Pincode is required")
    elif not pincode.isdigit() or len(pincode) != 6:
        errors.append("Pincode must be 6 digits")
    if not address:
        errors.append("Address is required")
        
    return errors

def edit_user(user):
    """Load user data into form for editing"""
    st.session_state.edit_mode = True
    st.session_state.current_user = user
    st.session_state.form_data = {
        "name": user["name"],
        "age": user["age"],
        "gender": user["gender"],
        "pincode": user["pincode"],
        "address": user["address"]
    }

def main():
    st.title("👤 User Information Manager")
    
    # Create form section
    st.subheader("➕ Add New User" if not st.session_state.edit_mode else "✏️ Edit User")
    with st.form("user_form", clear_on_submit=False):
        # Form fields
        name = st.text_input("Name*", value=st.session_state.form_data["name"])
        age = st.number_input("Age*", min_value=0, max_value=120, 
                            value=st.session_state.form_data["age"])
        gender = st.selectbox("Gender*", ["", "Male", "Female", "Other"], 
                            index=["", "Male", "Female", "Other"].index(st.session_state.form_data["gender"]))
        pincode = st.text_input("Pincode*", value=st.session_state.form_data["pincode"])
        address = st.text_area("Address*", value=st.session_state.form_data["address"])
        
        # Form submission buttons
        col1, col2 = st.columns(2)
        with col1:
            submit = st.form_submit_button("💾 Save")
        with col2:
            if st.session_state.edit_mode:
                cancel = st.form_submit_button("❌ Cancel", on_click=reset_form)
        
        if submit:
            # Validate inputs
            errors = validate_form(name, age, gender, pincode, address)
            
            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Create user data dictionary
                user_data = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "pincode": pincode,
                    "address": address
                }
                
                # Create or update user
                if st.session_state.edit_mode:
                    result = update_user(st.session_state.current_user["id"], user_data)
                    if result:
                        st.success("User updated successfully!")
                        reset_form()
                else:
                    result = create_user(user_data)
                    if result:
                        st.success("User created successfully!")
                        reset_form()
    
    st.divider()
    
    # User List section
    st.subheader("👥 User List")
    
    # Search and filter options
    search_col, filter_col = st.columns(2)
    with search_col:
        search_term = st.text_input("🔍 Search by name", key="search")
    with filter_col:
        filter_gender = st.selectbox("Filter by gender", ["All", "Male", "Female", "Other"], key="filter")
    
    # Load users from backend
    users = load_users()
    
    # Apply search and filter
    if search_term:
        users = [u for u in users if search_term.lower() in u["name"].lower()]
    if filter_gender != "All":
        users = [u for u in users if u["gender"] == filter_gender]
    
    if users:
        # Display each user in an expander
        for user in users:
            user_id = user["id"]
            
            # Create expander for each user
            with st.expander(f"{user['name']} - {user['age']} ({user['gender']})", expanded=False):
                # Display user details
                st.write(f"**ID:** {user_id}")
                st.write(f"**Pincode:** {user['pincode']}")
                st.write(f"**Address:** {user['address']}")
                
                # Action buttons
                if st.button("✏️ Edit", key=f"edit_{user_id}"):
                    edit_user(user)
                    st.rerun()
                
                if st.session_state.confirm_delete.get(user_id, False):
                    st.warning("Are you sure you want to delete this user?")
                    if st.button("✅ Confirm Delete", key=f"confirm_del_{user_id}"):
                        if delete_user(user_id):
                            st.success("User deleted successfully!")
                            st.session_state.confirm_delete[user_id] = False
                            time.sleep(0.5)
                            st.rerun()
                    if st.button("❌ Cancel", key=f"cancel_del_{user_id}"):
                        st.session_state.confirm_delete[user_id] = False
                        st.rerun()
                else:
                    if st.button("🗑️ Delete", key=f"delete_{user_id}"):
                        st.session_state.confirm_delete[user_id] = True
                        st.rerun()
    else:
        st.info("No users found. Create a new user using the form above.")

if __name__ == "__main__":
    main()