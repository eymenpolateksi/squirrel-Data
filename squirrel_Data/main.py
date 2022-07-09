import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamon = data[(data["Primary Fur Color"] == "Cinnamon")]
gray = data[(data["Primary Fur Color"] == "Gray")]
black = data[(data["Primary Fur Color"] == "Black")]


squirrel_dict = {
    "color": ["Cinnamon", "Gray", "Black"],
    "count": [len(cinnamon), len(gray), len(black)]
}
squirrel_count = pandas.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_count.csv")