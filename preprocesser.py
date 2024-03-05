import re
import pandas as pd
def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    if '\u202f' in data:
        pattern = '\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s[ap]m\s-'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    da = []
    for data in dates:
        da.append(re.sub('\u202f', " ", data))
    dates = da

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    try:
        df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')
    except ValueError:
        try:
            df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')
        except ValueError:
            df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p -')
    user = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            user.append(entry[1])
            messages.append(entry[2])
        else:
            user.append('group_notification')
            messages.append(entry[0])

    df['user'] = user
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['year'] = df['message_date'].dt.year
    df['month'] = df['message_date'].dt.month_name()
    df['month_num'] = df['message_date'].dt.month
    df['day'] = df['message_date'].dt.day
    df['day_name'] = df["message_date"].dt.day_name()
    df['hour'] = df['message_date'].dt.hour
    df['minute'] = df['message_date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    return df