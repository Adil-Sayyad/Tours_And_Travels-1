import os
import django

# Setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tours.settings')
django.setup()

from ei.models import Category, Table1
from django.contrib.auth.models import User

def add_data():
    categories_data = [
        {
            "name": "Beaches",
            "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Mountains",
            "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Historical",
            "img": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Wildlife",
            "img": "https://images.unsplash.com/photo-1549366021-9f761d450615?auto=format&fit=crop&w=600&q=80"
        }
    ]

    locations_data = [
        # Beaches
        {
            "state": "Goa",
            "location": "North Goa",
            "district": "North Goa",
            "name": "Baga Beach",
            "category": "Beaches",
            "image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=600&q=80",
            "desc": "Baga a seaside town in Bardez, Goa, India. It comes under the jurisdiction of Calangute, which is 2 km south. Baga is known for its popular beach and Baga Creek.",
            "byair": "Nearest airport is Dabolim Airport, approximately 41 km away.",
            "bytrain": "Thivim railway station is the closest, around 19 km from Baga.",
            "byroad": "Well connected by road. Buses from Panaji are frequently available."
        },
        {
            "state": "Andaman",
            "location": "Havelock Island",
            "district": "South Andaman",
            "name": "Radhanagar Beach",
            "category": "Beaches",
            "image": "https://images.unsplash.com/photo-1589394815804-964ce0ff96c7?auto=format&fit=crop&w=600&q=80",
            "desc": "Radhanagar Beach is known as one of the most beautiful beaches in Asia. It's famous for its white sand, breath-taking sunset and turquoise blue waters.",
            "byair": "Fly to Veer Savarkar International Airport, Port Blair, then take a ferry.",
            "bytrain": "No railway network in Andaman islands.",
            "byroad": "Accessible via ferry from Port Blair and local autos/cabs on the island."
        },
        {
            "state": "Kerala",
            "location": "Thiruvananthapuram",
            "district": "Thiruvananthapuram",
            "name": "Kovalam Beach",
            "category": "Beaches",
            "image": "https://images.unsplash.com/photo-1593693397690-362cb9666c6b?auto=format&fit=crop&w=600&q=80",
            "desc": "Kovalam is an internationally renowned beach with three adjacent crescent beaches. It has been a favourite haunt of tourists since the 1930s.",
            "byair": "Trivandrum International Airport is about 15 km away.",
            "bytrain": "Trivandrum Central railway station is about 15 km away.",
            "byroad": "Well connected via state buses, taxis and auto-rickshaws."
        },
        
        # Mountains
        {
            "state": "Himachal Pradesh",
            "location": "Kullu",
            "district": "Kullu",
            "name": "Manali",
            "category": "Mountains",
            "image": "https://images.unsplash.com/photo-1605649487212-4fbddb885e33?auto=format&fit=crop&w=600&q=80",
            "desc": "Manali is a high-altitude Himalayan resort town in India’s northern Himachal Pradesh state. It has a reputation as a backpacking center and honeymoon destination.",
            "byair": "Bhuntar airport is the nearest, located at a distance of 50 km.",
            "bytrain": "Jogindernagar railway station is the nearest railhead, about 165 km away.",
            "byroad": "Well-connected via NH-21. Regular buses ply from Delhi, Chandigarh, and Shimla."
        },
        {
            "state": "West Bengal",
            "location": "Darjeeling",
            "district": "Darjeeling",
            "name": "Darjeeling",
            "category": "Mountains",
            "image": "https://images.unsplash.com/photo-1544634076-a900cecefc68?auto=format&fit=crop&w=600&q=80",
            "desc": "Darjeeling is a town in India's West Bengal state, in the Himalayan foothills. Once a summer resort for the British Raj elite, it remains the terminus of the narrow-gauge Darjeeling Himalayan Railway.",
            "byair": "Bagdogra Airport is the closest, about 90 km away.",
            "bytrain": "New Jalpaiguri (NJP) is the major nearest railway station, roughly 70 km away.",
            "byroad": "Connected by road from Siliguri. Taxis and shared jeeps are available."
        },
        {
            "state": "Jammu and Kashmir",
            "location": "Baramulla",
            "district": "Baramulla",
            "name": "Gulmarg",
            "category": "Mountains",
            "image": "https://images.unsplash.com/photo-1618641986557-1ecd230959aa?auto=format&fit=crop&w=600&q=80",
            "desc": "Gulmarg is a town, a hill station, a popular skiing destination and a notified area committee in the Baramulla district of Jammu and Kashmir, India.",
            "byair": "Srinagar Airport is approx 56 km away.",
            "bytrain": "Jammu Tawi railway station is approx 290 km away.",
            "byroad": "Accessible from Srinagar by road in about 2 hours."
        },

        # Historical
        {
            "state": "Uttar Pradesh",
            "location": "Agra",
            "district": "Agra",
            "name": "Taj Mahal",
            "category": "Historical",
            "image": "https://images.unsplash.com/photo-1564507592224-2fc8c616f734?auto=format&fit=crop&w=600&q=80",
            "desc": "The Taj Mahal is an ivory-white marble mausoleum on the right bank of the river Yamuna in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor Shah Jahan.",
            "byair": "Agra Airport is about 13 km from Taj Mahal. Often people fly into New Delhi.",
            "bytrain": "Agra Cantt is the closest major railway station.",
            "byroad": "Yamuna Expressway connects New Delhi to Agra efficiently."
        },
        {
            "state": "Karnataka",
            "location": "Vijayanagara",
            "district": "Vijayanagara",
            "name": "Hampi",
            "category": "Historical",
            "image": "https://images.unsplash.com/photo-1620766165457-a80fe59217ca?auto=format&fit=crop&w=600&q=80",
            "desc": "Hampi is an ancient village in the south Indian state of Karnataka. It’s dotted with numerous ruined temple complexes from the Vijayanagara Empire.",
            "byair": "Hubli Airport is about 143 km away.",
            "bytrain": "Hospet Junction is the nearest railway station (13 km).",
            "byroad": "Regular buses run from Bangalore and Hospet."
        },
        {
            "state": "Delhi",
            "location": "Old Delhi",
            "district": "Central Delhi",
            "name": "Red Fort",
            "category": "Historical",
            "image": "https://images.unsplash.com/photo-1587595431973-160d0d94add1?auto=format&fit=crop&w=600&q=80",
            "desc": "The Red Fort is a historic fort in the city of Delhi in India that served as the main residence of the Mughal Emperors.",
            "byair": "Indira Gandhi International Airport, New Delhi.",
            "bytrain": "Old Delhi Railway Station and New Delhi Railway Station.",
            "byroad": "Centrally located in Delhi, assessible by cabs, metro, and buses."
        },

        # Wildlife
        {
            "state": "Uttarakhand",
            "location": "Ramnagar",
            "district": "Nainital",
            "name": "Jim Corbett National Park",
            "category": "Wildlife",
            "image": "https://images.unsplash.com/photo-1603504380756-3b6d510b05b8?auto=format&fit=crop&w=600&q=80",
            "desc": "Jim Corbett National Park is a forested wildlife sanctuary in northern India’s Uttarakhand State. Rich in flora and fauna, it’s known for its Bengal tigers.",
            "byair": "Pantnagar Airport is approx 80 km away.",
            "bytrain": "Ramnagar is the nearest railway station.",
            "byroad": "Buses and cabs are easily available from Delhi and Moradabad."
        },
        {
            "state": "Assam",
            "location": "Kanchanjuri",
            "district": "Golaghat",
            "name": "Kaziranga National Park",
            "category": "Wildlife",
            "image": "https://images.unsplash.com/photo-1558066531-18e388bd9a81?auto=format&fit=crop&w=600&q=80",
            "desc": "Kaziranga National Park is a protected area in the northeast Indian state of Assam. Spread across the floodplains of the Brahmaputra River, its forests, wetlands, and grasslands are home to tigers, elephants, and the world’s largest population of Indian one-horned rhinoceroses.",
            "byair": "Jorhat Airport is the closest (approx 97 km).",
            "bytrain": "Furkating is the nearest railway station, 75 km away.",
            "byroad": "Located on NH-37, connected by buses from Guwahati, Tezpur, and Jorhat."
        },
        {
            "state": "Rajasthan",
            "location": "Sawai Madhopur",
            "district": "Sawai Madhopur",
            "name": "Ranthambore",
            "category": "Wildlife",
            "image": "https://images.unsplash.com/photo-1549366021-9f761d450615?auto=format&fit=crop&w=600&q=80",
            "desc": "Ranthambore National Park is a vast wildlife reserve near the town of Sawai Madhopur in Rajasthan, northern India. It is a former royal hunting ground and home to tigers, leopards and marsh crocodiles.",
            "byair": "Jaipur International Airport is approx 160 km away.",
            "bytrain": "Sawai Madhopur Railway Station is roughly 11 km away.",
            "byroad": "Well connected to Jaipur, Agra, and Delhi by road."
        }
    ]

    print("Clearing existing Categories and Locations...")
    Category.objects.all().delete()
    Table1.objects.all().delete()

    print("Adding Categories...")
    for cat in categories_data:
        Category.objects.create(**cat)
        print(f"Added Category: {cat['name']}")

    print("\nAdding Locations...")
    for loc in locations_data:
        Table1.objects.create(**loc)
        print(f"Added Location: {loc['name']} in {loc['category']}")

    print("\nSetting up admin superuser...")
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@travel.com", "admin")
        print("Created superuser with username: 'admin' and password: 'admin'")
    else:
        print("Superuser 'admin' already exists.")

if __name__ == '__main__':
    add_data()
    print("\nData population successful!")
