from  azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Create client using endpoint and key
cog_key="https://github.com/MicrosoftLearning/AI-102-AIEngineerhttps://github.com/MicrosoftLearning/AI-102-AIEngineer"
cog_endpoint="https://servicioenvf.cognitiveservices.azure.com/"
credential = AzureKeyCredential(cog_key)
cog_client = TextAnalyticsClient(endpoint=cog_endpoint, credential=credential)

print(type(cog_client))

def detect_language():
     # Get language
    text=input("Escribe texto: ")
    detectedLanguage = cog_client.detect_language(documents=[text])[0]
    print('\nLanguage: {}'.format(detectedLanguage.primary_language.name))

def eval_sentiement():
    # Get sentiment
    text=input("Escribe texto: ")
    sentimentAnalysis = cog_client.analyze_sentiment(documents=[text])[0]
    print("\nSentiment: {}".format(sentimentAnalysis.sentiment))    

if __name__=="__main__":
    #PROBANDO DETECTAR LENGUAJE
    #detect_language()
    #PROBANDO DETECTAR SENTIMENT
    eval_sentiement()
   
