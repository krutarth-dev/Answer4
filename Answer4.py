import requests
import csv

def download_data_and_convert_to_csv(link):
    # Download the data from the link
    response = requests.get(link)
    data = response.text

    # Convert the data into a proper structure
    # Modify the code below to process the data according to your specific requirements
    structured_data = data.split('\n')

    # Write the data to a CSV file
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data"])  # Write header if needed
        writer.writerows(zip(structured_data))  # Write the data rows

# Test the program
link = "https://data.nasa.gov/resource/y77d-th95.json"  # Replace with the actual link to download the data
download_data_and_convert_to_csv(link)
