from icalendar import Calendar, Event
from datetime import datetime

# Create a calendar
cal = Calendar()

# Define event details
event = Event()
event.add('summary', 'Trip to Betty Bear Hut')
event.add('dtstart', datetime(2024, 3, 8, 14, 0, 0))  # Start date: March 8, 14:00
event.add('dtend', datetime(2024, 3, 10, 11, 0, 0))  # End date: March 10, 11:00
event.add('dtstamp', datetime.now())
event.add('location', 'Betty Bear Hut, Colorado')
event.add('description', 'Join us for a trip to Betty Bear Hut from March 8 to March 10!')

# Add event to the calendar
cal.add_component(event)

# Save the calendar to a .ics file
with open('betty_bear_hut_trip.ics', 'wb') as ical_file:
    ical_file.write(cal.to_ical())
