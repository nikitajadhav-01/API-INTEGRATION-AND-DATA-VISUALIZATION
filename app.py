import requests
import matplotlib.pyplot as plt
import seaborn as sns


API_KEY = "301976a2c93c3fe5244e7fecd26f2377"
CITY_NAME = "Pune"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNITS = "metric"


def get_current_weather(city, api_key):
    params = {
        "q": city,
        "appid": api_key,
        "units": UNITS
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        print("Error:", data.get("message"))
        return None

    return data



def visualize_weather(data):

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    parameters = ["Temperature (°C)", "Feels Like (°C)", "Humidity (%)"]
    values = [temp, feels_like, humidity]

    
    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 5))

    colors = ["#4C72B0", "#55A868", "#C44E52"]

    bars = plt.bar(parameters, values, color=colors)

    plt.title(f"Current Weather Data for {CITY_NAME}", fontsize=14, weight="bold")
    plt.xlabel("Parameters")
    plt.ylabel("Values")

    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2,
                 height,
                 f"{height}",
                 ha='center',
                 va='bottom',
                 fontsize=10)

    plt.tight_layout()
    plt.savefig("current_weather.png", dpi=300)
    plt.show()



def main():
    data = get_current_weather(CITY_NAME, API_KEY)
    if data:
        visualize_weather(data)


if __name__ == "__main__":
    main()
