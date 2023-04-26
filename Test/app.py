import requests

# URL of the API endpoint
url = 'http://localhost:5000/predict'

# Input data in CSV format
input_data = '-1.19896767411718,-1.47410047094211,1.8403259873066,-4.51582435488105,0.327567428246331,-0.174469282834848,0.959725705478786,-1.0264562279545,1.70043458447966,-0.0789417612044958,1.66266714493598,0.485619299748722,-0.93302495795613,-1.11878656487932,0.14125304079379,-2.81188754821512,-0.504745809870121,0.891222663154531,-1.51202243652326,-0.769854286810439,-0.453169416973525,0.334614040441455,-0.364541412466894,-0.310185782073785,-0.30259949355198,-1.24392415371264,-1.12345654520885,-0.73435108581633,89.17,"0"'

# Make a POST request to the API with the input data
response = requests.post(url, data=input_data)

try:
    # Try to parse the response as JSON
    prediction = response.json()['prediction']
    print(f'Prediction: {prediction}')
except ValueError:
    # If the response is not JSON, print the content as text
    print(f'Error: {response.text}')
