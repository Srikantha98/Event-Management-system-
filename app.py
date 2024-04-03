from flask import Flask, request, jsonify, render_template
import csv
import requests
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime, timedelta

app = Flask(__name__)

# External API URLs
WEATHER_API_URL = "https://gg-backend-assignment.azurewebsites.net/api/Weather"
DISTANCE_API_URL = "https://gg-backend-assignment.azurewebsites.net/api/Distance"

# Function to fetch weather data
def fetch_weather(city, date):
    params = {
        "code": "KfQnTWHJbg1giyB_Q9Ih3Xu3L9QOBDTuU5zwqVikZepCAzFut3rqsg==",
        "city": city,
        "date": date
    }
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code == 200:
        return response.json().get('weather', '')
    else:
        return None

# Function to calculate distance between two points
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

# Load event data from CSV file
def load_event_data(csv_file_path):
    events = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            event = {
                'event_name': row['event_name'],
                'city_name': row['city_name'],
                'date': row['date'],
                'latitude': float(row['latitude']),
                'longitude': float(row['longitude'])
            }
            events.append(event)
    return events

# REST API endpoint to add events
@app.route('/events/add', methods=['POST'])
def add_event():
    data = request.json
    # Add your database insertion logic here
    return jsonify({'message': 'Event added successfully'}), 201

# REST API endpoint to find events
@app.route('/events/find', methods=['GET'])
def find_events():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    date = request.args.get('date')

    # Load events data from CSV file
    csv_file_path = "events.csv"
    events_data = load_event_data(csv_file_path)

    # Filter events occurring within the next 14 days from the specified date
    events_within_14_days = [event for event in events_data if date <= event['date'] <= (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=14)).strftime('%Y-%m-%d')]

    # Calculate distances and fetch weather for each event
    for event in events_within_14_days:
        event['distance_km'] = calculate_distance(latitude, longitude, event['latitude'], event['longitude'])
        event['weather'] = fetch_weather(event['city_name'], event['date'])

    # Sort events by the earliest event after the specified date
    sorted_events = sorted(events_within_14_days, key=lambda x: x['date'])

    # Paginate the response with a page size of 10
    page = int(request.args.get('page', 1))
    page_size = 10
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_events = sorted_events[start_index:end_index]

    # Calculate total events and pages
    total_events = len(sorted_events)
    total_pages = (total_events + page_size - 1) // page_size   
    # Prepare the response data
    response_data = {
        "events": paginated_events,
        "page": page,
        "pageSize": page_size,
        "totalEvents": total_events,
        "totalPages": total_pages
    }

    return jsonify(response_data)

# Route handler for the root URL
@app.route('/')
def index():
    return render_template('index.html')

