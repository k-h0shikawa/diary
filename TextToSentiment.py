from SentimentAnalysis import SentimentAnalysis
from Plot import Plot
import os

if __name__ == "__main__":
    sentimentAnalysis = SentimentAnalysis()
    filenames = os.listdir("./text");
    sentiments = list();
    days = list();
    for filename in filenames:
        sentimentAnalysis.read_file("./text/" + filename)
        sentiment = sentimentAnalysis.analyze()[0]
        
        days.append(filename[:-4:])

        if (sentiment["label"] == "ネガティブ"):
            sentiments.append(-sentiment["score"])
        else:
            sentiments.append(sentiment["score"])
    print(days)
    print(sentiments)

    Plot(days, sentiments)