import streamlit as st

page_list = []

home_page = st.Page("baseline/homepage.py", title="Home", icon=":material/home:")
page_list.append(home_page)


CarraLee_page = st.Page("baseline/carralee_spain_page.py", title="Carra Lee's page", icon=":material/videogame_asset:")
page_list.append(CarraLee_page)


Challenge_page = st.Page("CHALLENGE_FOLDER/challenge_page.py", title="Challenge page", icon=":material/insert_drive_file:")
page_list.append(Challenge_page)

pg = st.navigation(page_list)
pg.run()
