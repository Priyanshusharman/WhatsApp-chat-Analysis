from urlextract import  URLExtract
extract =URLExtract()
from wordcloud import WordCloud
def fetch_stats(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
        # fetch number of message
    num_messages=df.shape[0]
    #featch number of words
    words = []
    for message in df['message']:
        words.extend(message.split())
    # featch number of media message
    num_media=df[df['message']=='<Media omitted>\n'].shape[0]
    # featch number of link
    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media, len(links)

def most_busy_user(df):
    x=df['user'].value_counts().head()
    df = round((df['user'].value_counts()/df.shape[0]*100),2).reset_index().rename(columns={'index':'name','user':'precent'})
    return x, df

#wordcloud
def create_wordcloude(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')

    img=wc.generate(df['message'].str.cat(sep=" "))
    return img