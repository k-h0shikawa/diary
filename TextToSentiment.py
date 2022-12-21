from SentimentAnalysis import SentimentAnalysis
from Plot import Plot
import os

if __name__ == "__main__":
    sentimentAnalysis = SentimentAnalysis()
    filenames = os.listdir("./text");
    sentiments = list()
    days = list()
    for filename in filenames:
        sentimentAnalysis.read_file("./text/" + filename)
        sentiment = sentimentAnalysis.analyze()[0]
        
        days.append(filename[:-4:])

        if (sentiment["label"] == "ネガティブ"):
            sentiments.append(-sentiment["score"])
        else:
            sentiments.append(sentiment["score"])
    ## 確認用
    print(days)
    print(sentiments)

    plot = Plot(days, sentiments)
    plot.save()

    with open("./scripts/README_template.md", mode="a") as readme:
        readme.write("![sentiment graph](./image/graph.png)")

    ## 確認用
    with open("./scripts/README_template.md") as readme:
        print(readme.read())