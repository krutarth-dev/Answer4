import requests
# Utilizing the requests library to download the data
import csv

def download_data_and_convert_to_csv(link):
    # Downloading the data from the link
    response = requests.get(link)
    data = response.text

    # Converting the data into a proper structure
    structured_data = data.split('\n')

    # Writing the data to the CSV file
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data"])  
        writer.writerows(zip(structured_data))  

# Testing
link = "https://data.nasa.gov/resource/y77d-th95.json"  # Replace with the actual link to download the data
download_data_and_convert_to_csv(link)
