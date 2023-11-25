import matplotlib.pyplot as plt

def most_common_weather(weather_data):
    # Calculate frequency distribution
    frequency_distribution = {}
    for weather, frequency in weather_data.items():
        if frequency in frequency_distribution:
            frequency_distribution[frequency].append(weather)
        else:
            frequency_distribution[frequency] = [weather]

    # Find the most common weather type
    max_frequency = max(frequency_distribution.keys())
    most_common_weather_types = frequency_distribution[max_frequency]

    
    print("Frequency Distribution:")
    for frequency, weather_types in frequency_distribution.items():
        print(f"{frequency} times: {', '.join(weather_types)}")

    print("\nMost Common Weather Type(s):")
    print(f"{max_frequency} times: {', '.join(most_common_weather_types)}")

  
    weather_types = list(weather_data.keys())
    frequencies = list(weather_data.values())

    plt.scatter(weather_types, frequencies, color='blue', marker='o')
    plt.title('Weather Type Frequency Scatter Plot')
    plt.xlabel('Weather Type')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.show()


weather_data = {
    "Sunny": 30,
    "Cloudy": 25,
    "Rainy": 15,
    "Snowy": 10,
    "Foggy":5,
    }
most_common_weather(weather_data)
