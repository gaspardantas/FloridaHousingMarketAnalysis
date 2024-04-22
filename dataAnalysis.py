import pandas as pd
import requests
import plotly.graph_objects as go

# Function to fetch data from FRED API
def fetch_fred_data(series_id, start_date, end_date):
    api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your FRED API key
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json&observation_start={start_date}&observation_end={end_date}"
    response = requests.get(url)
    data = response.json()
    return data

# Fetch Florida Median Listing Price data for the past 30 years
florida_median_listing_price_data = fetch_fred_data("MEDLISPRIFL", "2016-01-01", "2024-01-01")
# Fetch US Mortgage Average data for the past 30 years
us_mortgage_average_data = fetch_fred_data("MORTGAGE30US", "2016-07-01", "2024-01-01")
# Fetch Housing Inventory in Florida data for the past 30 years
florida_housing_inventory_data = fetch_fred_data("ACTLISCOUFL", "2016-01-01", "2024-01-01")

# Function to convert fetched data to DataFrame
def convert_to_dataframe(data):
    if 'observations' in data:
        observations = data['observations']
        dates = [obs['date'] for obs in observations]
        values = [float(obs['value']) for obs in observations]
        df = pd.DataFrame({'Date': dates, 'Value': values})
        return df
    else:
        return None

# Convert fetched data to DataFrame
florida_median_listing_price_df = convert_to_dataframe(florida_median_listing_price_data)
us_mortgage_average_df = convert_to_dataframe(us_mortgage_average_data)
florida_housing_inventory_df = convert_to_dataframe(florida_housing_inventory_data)

# Plotting the data in different forms
fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()
fig4 = go.Figure()

# Line chart for Median Listing Price in Florida
fig1.add_trace(go.Scatter(x=florida_median_listing_price_df['Date'], y=florida_median_listing_price_df['Value'], mode='lines', name='Florida Median Listing Price'))
fig1.update_layout(title='Florida Median Listing Price (2016 - 2024)', xaxis_title='Year', yaxis_title='Median Listing Price')

# Bar chart for US Mortgage Average
fig2.add_trace(go.Bar(x=us_mortgage_average_df['Date'], y=us_mortgage_average_df['Value'], name='US Mortgage Average'))
fig2.update_layout(title='US Mortgage Average (2016 - 2024)', xaxis_title='Year', yaxis_title='Mortgage Average')

# Area chart for Housing Inventory in Florida
fig3.add_trace(go.Scatter(x=florida_housing_inventory_df['Date'], y=florida_housing_inventory_df['Value'], mode='lines', fill='tozeroy', name='Housing Inventory in Florida'))
fig3.update_layout(title='Housing Inventory in Florida (2016 - 2024)', xaxis_title='Year', yaxis_title='Housing Inventory')

# Combined chart for all three datasets
fig4.add_trace(go.Scatter(x=florida_median_listing_price_df['Date'], y=florida_median_listing_price_df['Value'], mode='lines', name='Florida Median Listing Price'))
fig4.add_trace(go.Bar(x=us_mortgage_average_df['Date'], y=us_mortgage_average_df['Value'], name='US Mortgage Average', yaxis='y2'))
fig4.add_trace(go.Scatter(x=florida_housing_inventory_df['Date'], y=florida_housing_inventory_df['Value'], mode='lines', fill='tozeroy', name='Housing Inventory in Florida', yaxis='y3'))
fig4.update_layout(title='Comparison of Median Listing Price, US Mortgage Average, and Housing Inventory in Florida (2016 - 2024)',
                   xaxis_title='Year', template='plotly_dark',
                   yaxis=dict(title='Florida Median Listing Price', side='left', showgrid=False),
                   yaxis2=dict(title='US Mortgage Average', overlaying='y', side='right', showgrid=False),
                   yaxis3=dict(title='Housing Inventory in Florida', overlaying='y', side='right', position=0.85, showgrid=False))

# Show the plots
fig1.show()
fig2.show()
fig3.show()
fig4.show()
