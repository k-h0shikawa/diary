from transformers import pipeline, AutoModelForSequenceClassification, BertJapaneseTokenizer
import codecs
 
class SentimentAnalysis:
    def __init__(self):
        """
        コンストラクタ
        """
        model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment') 
        tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
        self.nlp = pipeline("sentiment-analysis",model=model,tokenizer=tokenizer)
        self.document = None
 
    def analyze(self,text = None):
        '''
        感情分析
        Returns:
        --------
            {'label':str,'score':float}  ネガポジの結果と確率を辞書形式で返す   
       
        '''
        return self.nlp(self.document if text is None else text)
 
    def read_file(self,filename,encoding='utf-8'):
        '''
        ファイルの読み込み
 
        Parameters:
        --------
            filename : str　 分析対象のファイル名 
        '''
        with codecs.open(filename,'r',encoding,'ignore') as f:
            self.read_text(f.read())
 
    def read_text(self,text):
        '''
        テキストの読み込み
 
        Parameters:
        --------
            text : str  分析対象のテキスト
        '''
        # 形態素解析を用いて名詞のリストを作成
        print(text)
        self.document = text