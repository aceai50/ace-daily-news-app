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
                "tech OR technology OR AI OR artificial intelligence OR software OR programming OR coding OR machine learning OR deep learning OR "
                "neural networks OR natural language processing OR NLP OR computer vision OR AI models OR GPT OR ChatGPT OR data science OR "
                "web development OR app development OR mobile development OR frontend OR backend OR full stack OR blockchain OR cryptocurrency OR "
                "bitcoin OR ethereum OR NFTs OR cybersecurity OR ethical hacking OR penetration testing OR cloud computing OR big data OR IoT OR "
                "Internet of Things OR automation OR robotics OR RPA OR AI automation OR digital transformation OR quantum computing OR VR OR "
                "virtual reality OR AR OR augmented reality OR mixed reality OR innovation OR startups OR venture capital OR tech trends OR tech news OR "
                "SaaS OR PaaS OR microservices OR virtualization OR edge computing OR AI ethics OR tech policy OR open source OR Linux OR DevOps OR CI/CD OR Jenkins "
                "OR Kubernetes OR Docker OR Git OR GitHub OR GitLab OR agile OR scrum OR kanban OR software engineering OR software testing OR test automation OR "
                "Selenium OR Cypress OR QA OR bug tracking OR Jira OR Trello OR database OR SQL OR NoSQL OR MongoDB OR Firebase OR PostgreSQL OR MySQL OR MariaDB OR "
                "CockroachDB OR Cassandra OR Redis OR Elasticsearch OR Databricks OR Snowflake OR Hadoop OR Spark OR TensorFlow OR PyTorch OR Scikit-learn OR Keras OR "
                "LangChain OR OpenAI OR Hugging Face OR LlamaIndex OR APIs OR REST OR GraphQL OR SOAP OR JSON OR XML OR React OR Angular OR Vue OR Svelte OR Django OR Flask "
                "OR Spring Boot OR Laravel OR Ruby on Rails OR Express OR Node OR FastAPI OR TypeScript OR JavaScript OR Python OR Java OR C++ OR C# OR Rust OR Go OR Swift OR "
                "Kotlin OR PHP OR HTML OR CSS OR Tailwind OR Bootstrap OR WebAssembly OR WASM OR Deno OR Vercel OR Netlify OR AWS OR Azure OR Google Cloud OR Heroku OR DigitalOcean OR "
                "OpenStack OR Ansible OR Terraform OR Prometheus OR Grafana OR cloud-native OR hybrid cloud OR edge AI OR federated learning OR tech careers OR programming bootcamps "
                "OR hackathons OR innovation hubs OR code challenges OR algorithms OR data structures OR competitive programming OR design patterns OR software architecture OR UML OR "
                "domain-driven design OR system design OR performance optimization OR low-code OR no-code OR mobile-first OR responsive design OR user experience OR UI/UX OR accessibility OR "
                "progressive web apps OR PWAs OR software licensing OR DevSecOps OR compliance OR GDPR OR data privacy OR digital security OR encryption OR cryptography OR blockchain security "
                "OR AI governance OR explainable AI OR responsible AI OR ethical AI OR inclusive design OR localization OR internationalization OR wearable tech OR smart devices OR connected devices OR "
                "tech education OR online learning OR coding tutorials OR interactive programming OR pair programming OR mob programming OR software consulting OR freelance development OR outsourcing OR "
                "managed services OR tech forums OR community development OR Stack Overflow OR Reddit OR tech blogs OR Medium OR Substack"
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
                "tech OR technology OR AI OR artificial intelligence OR software OR programming OR coding OR machine learning OR deep learning OR "
                "neural networks OR natural language processing OR NLP OR computer vision OR AI models OR GPT OR ChatGPT OR data science OR "
                "web development OR app development OR mobile development OR frontend OR backend OR full stack OR blockchain OR cryptocurrency OR "
                "bitcoin OR ethereum OR NFTs OR cybersecurity OR ethical hacking OR penetration testing OR cloud computing OR big data OR IoT OR "
                "Internet of Things OR automation OR robotics OR RPA OR AI automation OR digital transformation OR quantum computing OR VR OR "
                "virtual reality OR AR OR augmented reality OR mixed reality OR innovation OR startups OR venture capital OR tech trends OR tech news OR "
                "SaaS OR PaaS OR microservices OR virtualization OR edge computing OR AI ethics OR tech policy OR open source OR Linux OR DevOps OR CI/CD OR Jenkins "
                "OR Kubernetes OR Docker OR Git OR GitHub OR GitLab OR agile OR scrum OR kanban OR software engineering OR software testing OR test automation OR "
                "Selenium OR Cypress OR QA OR bug tracking OR Jira OR Trello OR database OR SQL OR NoSQL OR MongoDB OR Firebase OR PostgreSQL OR MySQL OR MariaDB OR "
                "CockroachDB OR Cassandra OR Redis OR Elasticsearch OR Databricks OR Snowflake OR Hadoop OR Spark OR TensorFlow OR PyTorch OR Scikit-learn OR Keras OR "
                "LangChain OR OpenAI OR Hugging Face OR LlamaIndex OR APIs OR REST OR GraphQL OR SOAP OR JSON OR XML OR React OR Angular OR Vue OR Svelte OR Django OR Flask "
                "OR Spring Boot OR Laravel OR Ruby on Rails OR Express OR Node OR FastAPI OR TypeScript OR JavaScript OR Python OR Java OR C++ OR C# OR Rust OR Go OR Swift OR "
                "Kotlin OR PHP OR HTML OR CSS OR Tailwind OR Bootstrap OR WebAssembly OR WASM OR Deno OR Vercel OR Netlify OR AWS OR Azure OR Google Cloud OR Heroku OR DigitalOcean OR "
                "OpenStack OR Ansible OR Terraform OR Prometheus OR Grafana OR cloud-native OR hybrid cloud OR edge AI OR federated learning OR tech careers OR programming bootcamps "
                "OR hackathons OR innovation hubs OR code challenges OR algorithms OR data structures OR competitive programming OR design patterns OR software architecture OR UML OR "
                "domain-driven design OR system design OR performance optimization OR low-code OR no-code OR mobile-first OR responsive design OR user experience OR UI/UX OR accessibility OR "
                "progressive web apps OR PWAs OR software licensing OR DevSecOps OR compliance OR GDPR OR data privacy OR digital security OR encryption OR cryptography OR blockchain security "
                "OR AI governance OR explainable AI OR responsible AI OR ethical AI OR inclusive design OR localization OR internationalization OR wearable tech OR smart devices OR connected devices OR "
                "tech education OR online learning OR coding tutorials OR interactive programming OR pair programming OR mob programming OR software consulting OR freelance development OR outsourcing OR "
                "managed services OR tech forums OR community development OR Stack Overflow OR Reddit OR tech blogs OR Medium OR Substack"
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
                "tech OR technology OR AI OR artificial intelligence OR machine learning OR data science OR programming OR coding OR hackathons OR "
                "code challenges OR coding competitions OR hiring OR tech hiring OR tech jobs OR job openings OR IT jobs OR tech recruitment OR "
                "software jobs OR software engineers OR developer jobs OR software hiring OR internships OR fresher jobs OR tech careers OR tech bootcamps OR "
                "tech training OR tech workshops OR webinars OR seminars OR innovation hubs OR tech fairs OR job fairs OR career fairs OR startup fairs OR "
                "startup events OR tech expos OR technology expos OR industry events OR developer conferences OR tech conferences OR tech meetups OR tech summits OR "
                "IT summits OR hackathons in India OR coding competitions in India OR hiring in India OR tech jobs in India OR IT jobs in India OR software jobs in India OR "
                "startups in India OR Indian startups OR Make in India OR Digital India OR IndiaStack OR tech hubs in India OR Bangalore tech OR Hyderabad tech OR "
                "Chennai tech OR Pune tech OR Delhi tech OR Mumbai tech OR NCR tech OR innovation in India OR tech parks in India OR Indian IT sector OR IT companies in India OR "
                "TCS OR Infosys OR Wipro OR HCL OR Cognizant OR tech trends in India OR Indian coding culture OR coding bootcamps in India OR coding schools in India OR "
                "NASSCOM OR Indian innovation OR IIT hackathons OR NIT hackathons OR Indian engineering colleges OR Indian developers OR Indian programmers"
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
