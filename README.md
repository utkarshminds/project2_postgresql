# project2_postgresql
Postgresql project

#Step 1 - open terminal and create a github branch
#type git status
#git branch BRANCH_NAME
#git checkout BRANCH_NAME
#git status
#python -m venv myenv
#myenv/scripts/activate
#pip install numpy, pandas, streamlit, matplotlib, psycopg2, openai

#download and install postgresql and pg admin 4
#open pg admin 4
#create a database named worldmap
#download world.sql
#open command prompt or powershell and type 
#psql -U postgres -d worldmap -f world.sql
#above command will import tables, data into worldmap database
#go to pg admin 4 and open worldmap database then schemas, then public, then tables and select table "city"and right click select view all rows
#it should all rows of the table city
#in case of psql command not found error
#add C:/Program files/PostgreSql/16/bin path in environment variables of user and system for variable PATH
#check bin path before updating env var PATH
#restart terminal and type
#psql -U postgres -d worldmap -f world.sql again
