from SentimentAnalysis import SentimentAnalysis


if __name__ == "__main__":
    sentimentAnalysis = SentimentAnalysis()
    sentimentAnalysis.read_file("./text/20221221.txt");
    print(sentimentAnalysis.analyze())