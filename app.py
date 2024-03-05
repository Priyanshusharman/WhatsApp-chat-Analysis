import streamlit as st
import preprocesser
import helper
import matplotlib.pyplot as plt
import seaborn as sns
st.sidebar.title("Text Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    st.sidebar.success('File uploaded successfully!')
    bdata=uploaded_file.getvalue()
    data=bdata.decode("utf-8")
    df=preprocesser.preprocess(data)
    st.dataframe(df)
    # fetch  uique users
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("show analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages, words, num_media, link = helper.fetch_stats(selected_user,df)

        col1, col2, col3, col4 =st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(words)
        with col3:
            st.header("Total media")
            st.title(num_media)
        with col4:
            st.header("Total link")
            st.title(link)

         # most_active_months
        st.title("Monthly Timeline")
        time_line = helper.most_active_months(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(time_line['time'], time_line['message'],color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #most active day
        st.title("Daily Timeline")
        day_df=helper.most_active_day(selected_user,df)
        fig, ax = plt.subplots()
        ax.plot(day_df['date'],day_df['message'],color='darkgreen')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #most active Week
        st.title("Activity Map")
        week=helper.most_active_day_name(selected_user,df)
        month_activity_df = helper.month_activity(selected_user, df)
        col1, col2 =st.columns(2)
        with col1:
            st.header("Most Busy Day")
            fig, ax = plt.subplots()
            ax.bar(week.index, week.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header("Most Busy Month")
            fig, ax = plt.subplots()
            ax.bar(month_activity_df .index, month_activity_df .values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        #activity heat mmap
        st.title("User HeatMap")
        headmap_table=helper.Active_user_heatmap(selected_user,df)
        fig, ax =plt.subplots()
        ax = sns.heatmap(headmap_table)
        st.pyplot(fig)


        # find busi user
        if selected_user=='Overall':

            x, new_df=helper.most_busy_user(df)
            fig, ax= plt.subplots()

            col1, col2 = st.columns(2)
            with col1:
                st.title('Most Busy User')
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.header("persentage")
                st.dataframe(new_df)
        st.title("Most word use")
        img=helper.create_wordcloude(selected_user,df)
        fig, ax =plt.subplots()
        ax.imshow(img)
        st.pyplot(fig)

        #most words user
        st.title("Most common words")
        most_commen = helper.most_common_words(selected_user,df)
        # col1, col2 = st.columns(2)
        # with col1:
        fig, ax =plt.subplots()
        ax.barh(most_commen[0],most_commen[1])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        # with col2:
        # st.dataframe(most_commen)

        # most common emojies
        st.title("Emoji Analysis")
        emoji_df = helper.most_emojies_use(selected_user,df)
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
            st.pyplot(fig)




