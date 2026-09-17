# Create a Flask API that reads sales_data.csv file and returns total revenue
# the API should have an endpoint /total_revenue that returns the total revenue as a JSON response
# the structure of the sales_data.csv file is as follows:
# order_id,product,region,sales,order_date
# 1001,Monitor,South,1306,2024-12-26
# the total revenue can be calculated by summing up the sales column
# convert the total revenue to an integer and return it as a JSON response.
# Additionally, create another endpoint /highest_region that returns the region 
# with the highest sales along with the total sales for that region as a JSON respons

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Read the CSV file into a DataFrame
df = pd.read_csv('sales_data.csv')

# Calculate total revenue
total_revenue = df['sales'].sum()

# Find the region with the highest sales
highest_region = df.groupby('region')['sales'].sum().idxmax()
highest_region_sales = df.groupby('region')['sales'].sum().max()

@app.route('/total_revenue', methods=['GET'])
def get_total_revenue():
    return jsonify({'total_revenue': int(total_revenue)})

@app.route('/highest_region', methods=['GET'])
def get_highest_region():
    return jsonify({
        'region': highest_region,
        'total_sales': int(highest_region_sales)
    })

if __name__ == '__main__':
    app.run(debug=True) 


