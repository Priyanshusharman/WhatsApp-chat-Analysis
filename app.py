import streamlit as st
import preprocesser
import helper
import matplotlib.pyplot as plt
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
        # find busi user
        if selected_user=='Overall':

            x, new_df=helper.most_busy_user(df)
            fig, ax= plt.subplots()

            col1, col2 = st.columns(2)
            with col1:
                st.title('Most Busy User')
                ax.bar(x.index, x.values)
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