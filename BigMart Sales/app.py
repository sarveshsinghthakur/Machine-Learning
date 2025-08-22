import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the trained model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set page title
st.title('BigMart Sales Prediction')

# Create input form
st.header('Enter Product Details')

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    item_weight = st.number_input('Item Weight', min_value=0.0, max_value=50.0, value=10.0)
    item_fat_content = st.selectbox('Item Fat Content', ['Low Fat', 'Regular'])
    item_visibility = st.number_input('Item Visibility', min_value=0.0, max_value=1.0, value=0.1)
    item_type = st.selectbox('Item Type', [
        'Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household',
        'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 
        'Health and Hygiene', 'Hard Drinks', 'Canned', 'Breads', 
        'Starchy Foods', 'Others'
    ])
    item_mrp = st.number_input('Item MRP', min_value=0.0, max_value=500.0, value=100.0)

with col2:
    outlet_identifier = st.selectbox('Outlet Identifier', [
        'OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019',
        'OUT027', 'OUT035', 'OUT045', 'OUT046', 'OUT049'
    ])
    outlet_establishment_year = st.number_input('Outlet Establishment Year', min_value=1900, max_value=2023, value=2000)
    outlet_size = st.selectbox('Outlet Size', ['Small', 'Medium', 'High'])
    outlet_location_type = st.selectbox('Outlet Location Type', ['Tier 1', 'Tier 2', 'Tier 3'])
    outlet_type = st.selectbox('Outlet Type', [
        'Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'
    ])

# Encoders dictionary
le_dict = {
    'Item_Fat_Content': {'Low Fat': 1, 'Regular': 2},
    'Item_Type': {'Dairy': 4, 'Soft Drinks': 14, 'Meat': 10, 'Fruits and Vegetables': 6, 'Household': 9, 
                  'Baking Goods': 0, 'Snack Foods': 13, 'Frozen Foods': 5, 'Breakfast': 2, 
                  'Health and Hygiene': 8, 'Hard Drinks': 7, 'Canned': 3, 'Breads': 1, 
                  'Starchy Foods': 15, 'Others': 11},
    'Outlet_Identifier': {'OUT010': 0, 'OUT013': 1, 'OUT017': 2, 'OUT018': 3, 'OUT019': 4, 
                         'OUT027': 5, 'OUT035': 6, 'OUT045': 7, 'OUT046': 8, 'OUT049': 9},
    'Outlet_Size': {'Small': 2, 'Medium': 1, 'High': 0},
    'Outlet_Location_Type': {'Tier 1': 0, 'Tier 2': 1, 'Tier 3': 2},
    'Outlet_Type': {'Grocery Store': 0, 'Supermarket Type1': 1, 'Supermarket Type2': 2, 'Supermarket Type3': 3}
}

# Create a button to make prediction
if st.button('Predict Sales'):
    input_data = np.array([[
        0,  # Placeholder for Item_Identifier
        item_weight,
        le_dict['Item_Fat_Content'][item_fat_content],
        item_visibility,
        le_dict['Item_Type'][item_type],
        item_mrp,
        le_dict['Outlet_Identifier'][outlet_identifier],
        outlet_establishment_year,
        le_dict['Outlet_Size'][outlet_size],
        le_dict['Outlet_Location_Type'][outlet_location_type],
        le_dict['Outlet_Type'][outlet_type]
    ]])

    prediction = model.predict(input_data)
    st.success(f'Predicted Sales: ₹{prediction[0]:,.2f}')

    # If model has feature importances
    if hasattr(model, 'feature_importances_'):
        st.header('Feature Importance')
        feature_names = ['Item Weight', 'Item Fat Content', 'Item Visibility', 'Item Type', 'Item MRP',
                        'Outlet Identifier', 'Outlet Establishment Year', 'Outlet Size',
                        'Outlet Location Type', 'Outlet Type']
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': model.feature_importances_[1:]
        }).sort_values('Importance', ascending=False)
        st.bar_chart(importance_df.set_index('Feature'))

    # === Regression Metrics (Dummy Evaluation on Test Data) ===
    # (In real scenario, load your X_test, y_test here)
    # Example: Assume y_test and y_pred exist
    try:
        y_test = np.array([100, 200, 300, 400, 500])   # Dummy test labels
        y_pred = model.predict(np.array([
            [0, 12, 1, 0.2, 4, 120, 1, 2005, 1, 0, 2],
            [0, 8, 2, 0.1, 6, 220, 2, 2010, 0, 1, 1],
            [0, 15, 1, 0.05, 10, 310, 3, 2008, 2, 2, 3],
            [0, 5, 2, 0.3, 7, 90, 4, 1999, 2, 1, 0],
            [0, 20, 1, 0.4, 14, 450, 5, 2015, 1, 2, 2]
        ]))

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        st.subheader("Model Evaluation")
        st.write(f"**MAE:** {mae:.2f}")
        st.write(f"**MSE:** {mse:.2f}")
        st.write(f"**RMSE:** {rmse:.2f}")
        st.write(f"**R² Score:** {r2:.2f}")

        # Residual Plot
        fig, ax = plt.subplots()
        ax.scatter(y_test, y_test - y_pred, alpha=0.7)
        ax.axhline(y=0, color='red', linestyle='--')
        ax.set_xlabel("Actual Sales")
        ax.set_ylabel("Residuals (y_true - y_pred)")
        ax.set_title("Residual Plot")
        st.pyplot(fig)

    except Exception as e:
        st.warning("Evaluation skipped. Provide test data for metrics and plots.")

    st.subheader("Data Distribution Plots")

    # Histogram for Item MRP
    st.write("#### Item MRP Distribution (Histogram)")
    fig_hist, ax_hist = plt.subplots()
    # Dummy data for demonstration, replace with actual data if available
    dummy_mrp_data = np.random.normal(loc=150, scale=50, size=1000)
    ax_hist.hist(dummy_mrp_data, bins=30, edgecolor='black')
    ax_hist.set_xlabel("Item MRP")
    ax_hist.set_ylabel("Frequency")
    ax_hist.set_title("Histogram of Item MRP")
    st.pyplot(fig_hist)

    # Pie chart for Outlet Type
    st.write("#### Outlet Type Distribution (Pie Chart)")
    fig_pie, ax_pie = plt.subplots()
    # Dummy data for demonstration, replace with actual data if available
    outlet_types = ['Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3']
    outlet_counts = [100, 400, 150, 50] # Example counts
    ax_pie.pie(outlet_counts, labels=outlet_types, autopct='%1.1f%%', startangle=90)
    ax_pie.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    ax_pie.set_title("Distribution of Outlet Types")
    st.pyplot(fig_pie)
