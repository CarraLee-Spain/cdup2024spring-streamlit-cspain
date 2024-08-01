import streamlit as st

st.title('Here was our Challenge!')
st.subheader('Our turn to build something awesome!')
st.write("________________________________________________________________________________________________________')

st.title('Now to the Challenge!')
st.subheader('It\'s your time to build something awesome!')

st.write('Here are the steps to take if you\'re not sure what to do:')
st.checkbox('Make sure you have access to the Arcadis GitHub environment!')
st.html('<sup> Find out how to get access <a href="https://arcadiso365.sharepoint.com/teams/pda/SitePages/getting-access-to-github.aspx" target="_blank">via sharepoint</a></sup>')

st.checkbox('Get access to the GitHub group "CDUP2024"')
st.html('<sup> You can request access via <a href="https://github.com/orgs/Arcadis/teams/cdup2024" target="_blank">this link</a>.</sup>')

st.checkbox('Clone the GitHub repository and create a new branch')
st.html('<sup> You can access the GitHub repository <a href="https://github.com/Arcadis/CitDev-CodingExam" target="_blank">here</a></sup>')

st.checkbox('Create a new page in the "CHALLENGE_FOLDER" folder')
st.html('<sup>This means your page should be "CHALLENGE_FOLDER\\my_page.py"</sup>')

st.checkbox('Add your new page to the app.py file')
st.html('<sup>This means assigning a new st.Page, and adding it to the page_list.</sup>')

st.checkbox('Run the app to see your new page in action!')
st.html('<sup>You can do this by executing "streamlit run app.py" in the terminal.</sup>')

st.checkbox('Commit your changes and create a pull request')
st.html('<sup>Make sure to add a description of your changes, and assign a reviewer.</sup>')

st.write('Be as creative as you want, but ultimately the goal is to contribute to this project by adding a new page, and doing so by utilizing GitHub.')
