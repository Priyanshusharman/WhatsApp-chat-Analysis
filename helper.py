import pandas as pd
from urlextract import  URLExtract
extract =URLExtract()
from wordcloud import WordCloud
import emoji
from collections import Counter
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

# most common words
def most_common_words(selected_user,df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    f=open('stop_hinglish.txt','r')
    stop_words=f.read()
    words=[]
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    return pd.DataFrame(Counter(words).most_common(20))

#most emoji use
def most_emojies_use(selected_user,df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    emojies=[]
    for message in df['message']:
        emojies.extend(emoji.emoji_list(message))
    emojis_extracted = [emoji_dict['emoji'] for emoji_dict in emojies]
    most_common_emojies = pd.DataFrame(Counter(emojis_extracted).most_common(20))

    return most_common_emojies

#most active time
def most_active_months(selected_user,df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+"-"+str(timeline['year'][i]))
    timeline['time'] = time

    return timeline
def most_active_day(selected_user,df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    df["date"] = df['message_date'].dt.date
    day_df = df.groupby(['date']).count()['message'].reset_index()
    return day_df
# most active day
def most_active_day_name(selected_user,df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    day=df['day_name'].value_counts()
    return day
# Monthly Busey Week
def month_activity(selected_user,df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]
    day=df['month'].value_counts()
    return day

#heat map of active user
def Active_user_heatmap(selected_user,df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user]

    activaty_table=df.pivot_table(index="day_name",columns='period',values='message',aggfunc='count').fillna(0)
    return activaty_table