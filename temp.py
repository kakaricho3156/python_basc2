def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    tokyo_tmp = 0.0
    count = 0
    for weather in weather_information:
        if weather["prefecture"] == "東京都":
            tokyo_tmp += weather["temperature"]
            count = count + 1

    print(tokyo_tmp / count)
    print("//////////////")

    # print(weather_information[0]["temperature"])
    # ↑こうすればtemperatureの値を取り出すことができる
    total_temp = 0.0
    for weather in weather_information:
        total_temp += weather["temperature"]

    avg = total_temp / len(weather_information)

    print(avg)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    oosaka_station = ""

    for weather in weather_information:
        if weather["prefecture"] == "大阪府" and len(oosaka_station) > 0:
            oosaka_station += "," + weather["station"]
        elif weather["prefecture"] == "大阪府":
            oosaka_station += weather["station"]

    print(oosaka_station)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    temp = 0.0
    count = 0

    for weather in weather_information:
        if weather["prefecture"] == "福岡県":
            temp += weather["temperature"]
            count += 1

    print(temp / count)


if __name__ == "__main__":
    main()
