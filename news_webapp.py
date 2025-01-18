from dotenv import load_dotenv
import os
from newsapi import NewsApiClient
from datetime import datetime, timedelta
import schedule
import time
import streamlit as st

load_dotenv()

api_key = "f917b824657a47c19af28b6d78d3df3c"
newsapi = NewsApiClient(api_key=api_key)

st.title("Apollo: News App")

today = datetime.today().strftime('%d-%m-%y')
st.write(f"Today's date: {today}")

st.write("enter your top headline search query below 🔍")
search = st.text_input("Enter your query to be searched: ")

if search:
    try:
       searched = newsapi.get_top_headlines(
           q=search,
           #sources="the-hindu",
           #category='business',  # Remove if using 'sources'
           language='en',
           #country='us',  # Remove if using 'sources'
           page=1
       )
       #print("Top Headlines:")
       #print(top_headlines)
    except Exception as e:
       st.write(f"An error occurred while fetching top headlines: {e}")

   #n = len(top_headlines["articles"])
    n = len(searched["articles"])
    for i in range(n):
        if i < 10:
            all_headlines_list = searched["articles"][i]
            with st.container():
                st.write(f"{i+1}. {all_headlines_list['title']} - {all_headlines_list['source']}")
                st.write(f"Description: {all_headlines_list['description']}")
                st.markdown("---")  # Horizontal separator between boxes
        else: break

    


#search for gemeral queries
st.write("enter your search for general query below 🕵️‍♂️")
search_2 = st.text_input("Enter your query ")
   

if search_2:

    today = datetime.today().strftime('%Y-%m-%d')
    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

    try:
        searched_2 = newsapi.get_everything(
            q=search_2,
            #domains='bbc.co.uk,techcrunch.com',
            from_param=yesterday,
            to=today,
            language='en',
            sort_by='relevancy',
            page=1
        )
        #print("\nAll Articles:")
        #print(all_articles)

    except Exception as e:
        st.write(f"An error occurred while fetching all articles: {e}")




    #n = len(top_headlines["articles"])
    n = len(searched_2["articles"])
    for i in range(n):
        if i < 10:
            all_headlines_list = searched_2["articles"][i]
            with st.container():
                st.write(f"{i+1}. {all_headlines_list['title']} - {all_headlines_list['source']}")
                st.write(f"Description: {all_headlines_list['description']}")
                st.markdown("---")  # Horizontal separator between boxes
        else: break

if st.button("Run"):


    #All the top headlines
    st.header("Topheadline: 📈")

    try:
        top_headlines = newsapi.get_top_headlines(
            q='',
            #sources="the-hindu",
            #category='business',  # Remove if using 'sources'
            language='en',
            #country='us',  # Remove if using 'sources'
            page=1
        )
        #print("Top Headlines:")
        #print(top_headlines)
    except Exception as e:
        st.write(f"An error occurred while fetching top headlines: {e}")

    #n = len(top_headlines["articles"])

    n = len(top_headlines["articles"])

    for i in range(n):
        if i < 10:
            all_headlines_list = top_headlines["articles"][i]
            with st.container():
                st.write(f"{i+1}. {all_headlines_list['title']} - {all_headlines_list['source']}")
                with st.expander("Click me to expand"):
                    st.write(f"Description: {all_headlines_list['description']}")
                st.markdown("---")  # Horizontal separator between boxes
        else: break

    #Tech top headline
    st.header("Tech Top Headline: 👨‍💻")

    try:
        tech_top_headlines = newsapi.get_top_headlines(
            q= (
                "tech OR AI OR artificial intelligence OR software OR programming OR coding OR machine learning OR "
                "deep learning OR data science OR web development OR app development OR mobile development OR frontend OR "
                "backend OR full stack OR blockchain OR cryptocurrency OR cybersecurity OR ethical hacking OR penetration testing OR "
                "cloud computing OR big data OR IoT OR Internet of Things OR automation OR robotics OR Python OR Java OR JavaScript OR "
                "TypeScript OR C++ OR C# OR Ruby OR Go OR Swift OR Kotlin OR PHP OR HTML OR CSS OR React OR Angular OR Vue OR Django OR "
                "Flask OR Spring OR Node OR Express OR DevOps OR CI/CD OR Jenkins OR Kubernetes OR Docker OR Git OR GitHub OR open source OR "
                "Linux OR API OR REST OR GraphQL OR database OR SQL OR NoSQL OR MongoDB OR Firebase OR PostgreSQL OR MySQL OR agile OR scrum OR "
                "SaaS OR PaaS OR microservices OR virtualization OR AI models OR GPT OR ChatGPT OR natural language processing OR VR OR virtual reality OR "
                "AR OR augmented reality OR quantum computing OR innovation OR tech news OR tech trends OR startups OR venture capital"
                ),
            #sources="the-hindu",
            #category='business',  # Remove if using 'sources'
            language='en',
            #country='us',  # Remove if using 'sources'
            page=1
        )
        #print("Top Headlines:")
        #print(top_headlines)
    except Exception as e:
        st.write(f"An error occurred while fetching top headlines: {e}")

    #n = len(tech_top_headlines["articles"])

    n = len(tech_top_headlines["articles"])

    for i in range(n):
        if i < 10:
            all_headlines_list = tech_top_headlines["articles"][i]
            with st.container():
                st.write(f"{i+1}. {all_headlines_list['title']} - {all_headlines_list['source']}")
                with st.expander("Click me to expand"):
                    st.write(all_headlines_list['description'])
                st.markdown("---")  # Horizontal separator between boxes
        else: break


    #Tech news in india
    st.header("Tech in India news 🥭")
    try:
        # Get today's and yesterday's dates dynamically
        today = datetime.today().strftime('%Y-%m-%d')
        yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        # Fetch articles sorted by relevancy
        articles_relevant = newsapi.get_everything(
            q= (
                "tech OR AI OR artificial intelligence OR software OR programming OR coding OR machine learning OR "
                "deep learning OR data science OR web development OR app development OR mobile development OR frontend OR "
                "backend OR full stack OR blockchain OR cryptocurrency OR cybersecurity OR ethical hacking OR penetration testing OR "
                "cloud computing OR big data OR IoT OR Internet of Things OR automation OR robotics OR Python OR Java OR JavaScript OR "
                "TypeScript OR C++ OR C# OR Ruby OR Go OR Swift OR Kotlin OR PHP OR HTML OR CSS OR React OR Angular OR Vue OR Django OR "
                "Flask OR Spring OR Node OR Express OR DevOps OR CI/CD OR Jenkins OR Kubernetes OR Docker OR Git OR GitHub OR open source OR "
                "Linux OR API OR REST OR GraphQL OR database OR SQL OR NoSQL OR MongoDB OR Firebase OR PostgreSQL OR MySQL OR agile OR scrum OR "
                "SaaS OR PaaS OR microservices OR virtualization OR AI models OR GPT OR ChatGPT OR natural language processing OR VR OR virtual reality OR "
                "AR OR augmented reality OR quantum computing OR innovation OR tech news OR tech trends OR startups OR venture capital"
                ),
            from_param=yesterday,
            to=today,
            language='en',
            sources="the-times-of-india,the-hindu",
            sort_by='relevancy',
            page=1
        )
        # Fetch articles sorted by popularity
        articles_popular = newsapi.get_everything(
            q='India OR Hindustan',
            from_param=yesterday,
            to=today,
            language='en',
            sources="the-times-of-india,the-hindu",
            sort_by='popularity',
            page=1
        )
    
    except Exception as e:
        st.write(f"An error occurred while fetching articles: {e}")


     # Combine and deduplicate articles


    combined_articles = {article['url']: article for article in articles_relevant['articles']}
    combined_articles.update({article['url']: article for article in articles_popular['articles']})
    # Display combined results
    #print(f"\nDaily News for {today}:")
    for idx, article in enumerate(combined_articles.values(), start=1):
        if idx < 6:
            st.write(f"{idx}. Title: {article['title']}")
            st.write(f"   Source: {article['source']['name']}")
            with st.expander("Click me to expand"):
                st.write(f" Description: {article["description"]}")
                st.write(f"   URL: {article['url']}\n")
            st.markdown("---")
        else: break




    #Tech, hiring, other news in India
    st.header("Tech events, hiring, other news in India  👨‍💻+🥭")

    try:
        # Get today's and yesterday's dates dynamically
        today = datetime.today().strftime('%Y-%m-%d')
        yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        # Fetch articles sorted by relevancy
        articles_relevant = newsapi.get_everything(
            q=(
                "tech OR technology OR AI OR artificial intelligence OR machine learning OR coding OR programming OR hackathons OR "
                "coding competitions OR hiring OR tech jobs OR IT jobs OR software jobs OR internships OR fresher jobs OR tech careers OR "
                "tech bootcamps OR job fairs OR career fairs OR developer conferences OR tech meetups OR tech summits OR startups OR Indian startups OR "
                "Make in India OR Digital India OR innovation in India OR IIT hackathons OR NIT hackathons OR Indian IT sector OR IT companies OR "
                "TCS OR Infosys OR Wipro OR HCL OR Cognizant OR Bangalore OR Hyderabad OR Chennai OR Pune OR Delhi OR Mumbai"
                ),
            from_param=yesterday,
            to=today,
            language='en',
            sources="the-times-of-india,the-hindu",
            sort_by='relevancy',
            page=1
        )
        # Fetch articles sorted by popularity
        articles_popular = newsapi.get_everything(
            q='India OR Hindustan',
            from_param=yesterday,
            to=today,
            language='en',
            sources="the-times-of-india,the-hindu",
            sort_by='popularity',
            page=1
        )
    
    except Exception as e:
        st.write(f"An error occurred while fetching articles: {e}")


     # Combine and deduplicate articles


    combined_articles = {article['url']: article for article in articles_relevant['articles']}
    combined_articles.update({article['url']: article for article in articles_popular['articles']})
    # Display combined results
    #print(f"\nDaily News for {today}:")
    for idx, article in enumerate(combined_articles.values(), start=1):
        if idx < 6:
            st.write(f"{idx}. Title: {article['title']}")
            st.write(f"   Source: {article['source']['name']}")
            with st.expander("Click me to expand"):
                st.write(f" Description: {article["description"]}")
                st.write(f"   URL: {article['url']}\n")
            st.markdown("---")
        else: break
