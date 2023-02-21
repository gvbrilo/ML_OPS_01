# <p align=center>`Individual Project : Machine Learning Operations`<p>
<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

####  _Ingeniero: Lorenzo Prado Melgarejo_

#
### This Project is meant to display the technical abilities that a Data Engineer must have in order to be efficient in this new era full of changes - Feel free to fork this project  , i use basic techniques in this project and i know that you can improve and contribute.
#

## <p align=center> _Enjoy Learning from this project or Improving it_ <p>
#

 # <p align=center> Explanatory video : <p align=center>[_Youtube Explication_ ](https://cloudaffaire.com) <p> 

## Content Of the Project:

- ## **ETL Process** : 
    - Transformation_Dataset_Hosts.ipynb
    - Transformation_Datasets_Score.ipynb

- ## **Queries in the API :**
    - Data_Queries.ipynb

- ## **API Code**
    - main.py

- ## **EDA Process :** 
    - EDA.ipynb

- ## **ML Process**
    - Recommendation_System.ipynb 

- ## **Initial Databases :** 
    - Datasets_Hosts
        - amazon_prime_titles.csv
        - disney_plus_titles.csv
        - hulu_titles.csv
        - netflix_titles.csv
    - Datasets_Score
        - 1.csv
        - 2.csv
        - 3.csv
        - 4.csv
        - 5.csv
        - 6.csv
        - 7.csv
        - 8.csv


- ## **Processed Databases :**
    - Datasets_Hosts
        - df_total_hosts.csv  -  (Used in ETL) 
    - Datasets_Score
        - df_total_score.csv  -  (Used in ML)
    - df_total_data.csv - (Used in API) 

- ## **Explanatory Summary :** 
    - README.md

- ## **Required API Dependencies :** 
    - Requeriments.txt

#
# <p align=center>ETL - Cleaning Data <p><p align=center><img src=Images_src\ETL.png><p>

## **Filter 1**: _generate 'id' field_ :

- Each id will consist of the first letter of the platform name,followed by the show_id already present in the datasets (example 'as123')

## **Filter  2**: _fill rating field with 'G'_:

- The null values ​​of the field must be replaced by the "G" (corresponds to the maturity rating :"general for all audiences")

 ## **Filter  3**: _lower case fields_:   

- text fields will be in lower case, no exceptions

 ## **Filter  4**: _divide duration field_: 

- the duration field should be converted to fields: duration_int and duration_type . The first will be an integer and the second a string indicating the unit of measurement: min(minutes) or season(seasons)

#
# <p align=center>API - Queries<p><p align=center><img src=Images_src\API_1.png><p>

## **Request 1**: _Movie with longer duration and optional filters of year, platform and duration_ :

    - get_max.duration(year, platform, duration.type)  

## **Request 2**: _Number of movies per platform with a score greater than xx in a given year_:

    - get_score_count(platform, scored, year)

 ## **Request 3**: _number of movies per platform with platform filter_:   

    - get_count_platform(platform)

 ## **Request 4**: _Actor who repeats himself the most according to platform and year_: 

    - get_actor(platform, year)


#
# <p align=center>Deploy API<p><p align=center><img src=Images_src\DETA.SPACE.png><p>

## **Requisit 1**: _DETA.SPACE_ :

- First we will use DETA.SPACE a developer-friendly cloud platform, helping out users to build and deploy their ideas  

## **Requisit 2**: _FAST_API_:

- FastAPI is a Web framework for developing RESTful APIs in Python.

#
# <p align=center>EDA - Exploratory Data Analysis<p><p align=center><img src=Images_src\EDA.png><p>

## _investigate relationships between variables in datasets, see if there are outliers or anomalies, null values, and see if there are any interesting patterns worth exploring in further analysis_

    - File : EDA.ipynb

#
# <p align=center>ML - Machine Learning<p><p align=center><img src=Images_src\ML.png><p>

## _And last Maching learning , We will train our machine learning model to build a movie recommendation system for users, where given a user id and a movie, it tells us if it is recommended or not for said user and we will deploy it with a graphical interface using Gradio._

    - File : ML_Recomendation_System.ipynb
