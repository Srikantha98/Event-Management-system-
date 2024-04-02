#Event Management System

This project is an Event Management System built using Flask, 
which allows users to add and search for events based on their location and date. 
It integrates with external APIs to fetch weather data and calculate distances between locations. 
#Features Add Events: 
Users can add events to the system via a REST API endpoint. 
#Find Events:
Users can search for events within a specified radius and date range using the /events/find endpoint. 
#Weather Integration: 
The system fetches weather data for each event location to provide users with weather information. 
#Distance Calculation: 
It calculates the distance between the user's location and each event location to facilitate event searching. 
Installation Clone the repository: 
bash Copy code git clone <repository_url> 
Install dependencies: 
Copy code pip install -r requirements.txt 
#Run the application: Copy code python app.py Usage Adding 
#Events: Send a POST request to /events/add with JSON data containing details of the event. 
$Example: bash Copy code POST /events/add { "event_name": "Music Festival", "city_name": "New York", "date": "2024-05-20", "latitude": 40.7128, "longitude": -74.0060 } 
#Finding Events: 
Send a GET request to /events/find with query parameters for latitude, longitude, and date. 
$Example: bash Copy code GET /events/find?latitude=40.7128&longitude=-74.0060&date=2024-05-15&page=1 Configuration External API URLs are defined in the app.py file and can be modified as needed. 
The path to the events CSV file is specified in the load_event_data function and should be updated if the file location changes. Contributing Contributions are welcome! Please follow these 
guidelines: 
Fork the repository Create a new branch Make your changes Submit a pull request License This project is licensed under the MIT License - see the LICENSE file for details. Contact For any questions or feedback, please contact Srikantha.l@campusuvce.in
