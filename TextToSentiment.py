from SentimentAnalysis import SentimentAnalysis
from Plot import Plot
import os

if __name__ == "__main__":
    sentimentAnalysis = SentimentAnalysis()
    filenames = os.listdir("./text")
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

    read_me_text = ""
    with open("./scripts/README_template.md") as readme:
        read_me_text += readme.read()

    read_me_text += "![sentiment graph](./graph.png)"

    print(read_me_text)
    ## 確認用
    with open("./README.md", "w") as readme:
        readme.write(read_me_text)