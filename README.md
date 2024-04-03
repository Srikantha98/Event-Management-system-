 
**Event Management System**

**Overview**

This project is an Event Management System built using Flask, which enables users to manage and discover events based on their location and date. The system integrates with external APIs to provide weather forecasts and calculate distances between locations.

![Event Management System](<image_url>)

**Features**

**Add Events:**
Users can add events to the system via a REST API endpoint. 

**Find Events:**
Users can search for events within a specified radius and date range using the `/events/find` endpoint. 

**Weather Integration:**
The system fetches weather data for each event location to provide users with weather information. 

**Distance Calculation:**
It calculates the distance between the user's location and each event location to facilitate event searching. 

**Installation 

1. **Install Flask:** 
   
   First, you need to install Flask, which is a Python web framework used for developing web applications. You can install Flask using pip:

   ```bash 
   pip install flask
   ```

2. **Clone the repository:** 

    ```bash 
    git clone <repository_url> 
    ```

3. **Install dependencies:** 

    ```bash 
    pip install -r requirements.txt 
    ```

## Run the application: 

```bash 
python app.py 
```

After running the application, you can access it in your web browser at `http://localhost:5000`.

## Usage 

### Adding Events: 
Send a POST request to `/events/add` with JSON data containing details of the event. 

**Example:** 

```bash 
POST /events/add 
{ 
    "event_name": "Music Festival", 
    "city_name": "New York", 
    "date": "2024-05-20", 
    "latitude": 40.7128, 
    "longitude": -74.0060 
} 
```

### Finding Events: 
Send a GET request to `/events/find` with query parameters for latitude, longitude, and date. 

**Example:** 

```bash 
GET /events/find?latitude=40.7128&longitude=-74.0060&date=2024-05-15&page=1 
```

## Configuration 

External API URLs are defined in the `app.py` file and can be modified as needed. The path to the events CSV file is specified in the `load_event_data` function and should be updated if the file location changes. 

## Contributing 

Contributions are welcome! Please follow these guidelines: 

1. Fork the repository 
2. Create a new branch 
3. Make your changes 
4. Submit a pull request 

## Deployment

This project is deployed on Vercel. Click https://event-management-system-gold.vercel.app/ to view the deployed application.

## Contact 

For any questions or feedback, please contact [Srikantha.l@campusuvce.in](mailto:Srikantha.l@campusuvce.in).
```
 
