\# 🛡️ SafeHer AI



> \*\*AI-Powered Women's Safety Route Assistant\*\*



SafeHer AI is an intelligent web application designed to help women travel more safely by analyzing travel routes, calculating a safety score, identifying nearby emergency services, and providing AI-powered safety recommendations before every journey.



\---



\# 📌 Problem Statement



Women often travel through unfamiliar locations, especially during the evening and night. Traditional navigation applications focus only on the shortest or fastest route and do not consider the safety of the traveler.



SafeHer AI aims to bridge this gap by providing route safety insights, emergency service locations, and personalized AI recommendations to support safer travel decisions.



\---



\# 💡 Solution



SafeHer AI combines Artificial Intelligence with open-source mapping technologies to analyze travel routes and provide users with:



\- 🛣️ Route Distance

\- ⏱️ Estimated Travel Time

\- 🛡️ Safety Score

\- ⚠️ Risk Level

\- 👮 Nearby Police Stations

\- 🏥 Nearby Hospitals

\- 🤖 AI-Generated Safety Recommendations

\- 📱 WhatsApp Emergency SOS



\---



\# ✨ Features



\- AI-Powered Route Safety Analysis

\- Interactive Route Visualization

\- Safety Score Calculation

\- Nearby Police Station Detection

\- Nearby Hospital Detection

\- AI-Based Travel Safety Suggestions

\- WhatsApp Emergency SOS

\- Clean and User-Friendly Interface



\---



\# 🛠️ Tech Stack



\## Frontend

\- Streamlit



\## Backend

\- Python



\## APIs \& Services

\- OpenStreetMap (OSM)

\- Nominatim Geocoding API

\- OSRM Routing API

\- Overpass API

\- OpenAI GPT-5 API



\## Libraries

\- Streamlit

\- Folium

\- Streamlit-Folium

\- Requests

\- Plotly

\- Python-Dotenv

\- OpenAI



\---



\# 📂 Project Structure



```

SafeHer\_AI/

│

├── app.py

├── README.md

├── requirements.txt

├── .env.example

│

├── services/

│   ├── geocoding.py

│   ├── routing.py

│   ├── nearby\_places.py

│   ├── map\_generator.py

│   ├── safety\_score.py

│   ├── openai\_ai.py

│   └── sos.py

│

└── assets/

&#x20;   └── screenshots/

```



\---



\# ⚙️ Installation



\## 1. Clone the repository



```bash

git clone https://github.com/yourusername/SafeHer\_AI.git

```



\## 2. Navigate to the project folder



```bash

cd SafeHer\_AI

```



\## 3. Create a virtual environment (Recommended)



\### Windows



```bash

python -m venv venv

venv\\Scripts\\activate

```



\### Linux / macOS



```bash

python3 -m venv venv

source venv/bin/activate

```



\## 4. Install the required dependencies



```bash

pip install -r requirements.txt

```



\## 5. Configure Environment Variables



Create a `.env` file in the project root and add your OpenAI API Key.



```env

OPENAI\_API\_KEY=your\_openai\_api\_key

```



\## 6. Run the application



```bash

streamlit run app.py

```



\## 7. Open the application



Visit the following URL in your browser:



```

http://localhost:8501

```



\---



\# 📊 How It Works



1\. Enter Source Location

2\. Enter Destination Location

3\. Select Travel Time (Day/Night)

4\. Click \*\*Analyze Route\*\*

5\. The application:

&#x20;  - Calculates the optimal route

&#x20;  - Computes the Safety Score

&#x20;  - Displays nearby Police Stations

&#x20;  - Displays nearby Hospitals

&#x20;  - Generates AI Safety Recommendations

&#x20;  - Provides WhatsApp SOS support



\---

# 📸 Screenshots

## Home Screen
![Home Screen](assets/screenshots/home.png)

## Route Analysis
![Route Analysis](assets/screenshots/route.png)

## Interactive Map
![Interactive Map](assets/screenshots/map.png)

## AI Recommendations
![AI Recommendations](assets/screenshots/ai.png)

## WhatsApp SOS
![WhatsApp SOS](assets/screenshots/sos.png)

\# 🚀 Future Scope



\- Live GPS Tracking

\- Real-Time Crime Hotspot Integration

\- Weather-Aware Route Analysis

\- Trusted Contact Live Monitoring

\- Voice-Based SOS

\- Multi-Language Support

\- Predictive AI Risk Analysis



\---



\# 👥 Team



\*\*Team Name:\*\* THE VISIONARIES



\---



\# 📄 License



This project was developed for educational and hackathon purposes.



\---



\# ❤️ Acknowledgements



We would like to thank:



\- OpenAI

\- OpenStreetMap Community

\- OSRM Project

\- Overpass API

\- Streamlit



for providing the open-source technologies that made this project possible.

