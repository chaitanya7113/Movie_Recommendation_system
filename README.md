# 🎬 Hollywood Silver Screen

**Hollywood Silver Screen** is a content-based movie recommendation system built with Python. It helps users discover new Hollywood movies similar to their favorites using film metadata and similarity algorithms.

---

## 🔑 Project Objective

The goal of this project is to build a smart and simple movie recommender that suggests Hollywood movies based on the one selected by the user. This project was created to explore machine learning concepts like similarity metrics and feature engineering in the context of real-world media data.

---

## 🧠 How It Works

1. **Dataset Loading:** A preprocessed dataset of Hollywood movies is used, containing details like title,genres, keywords, cast, and crew .
2. **Text Feature Engineering:** Movie metadata is converted into a text format for processing.
3. **Similarity Calculation:** Cosine similarity is used to compare movie descriptions and identify similar ones.
4. **Recommendation Output:** When a user enters a movie title, its gives movie information and at bottom there is show recommend button by clicking the system returns the top similar movies based on the similarity matrix.
5. **Movie Poster** Movie Poster is evaluate through the tmdb api

---

## 🛠 Tech Stack

- **Python 3**
- **pandas** – for data handling
- **scikit-learn** – for vectorization and similarity calculation
- **pickle** – for storing preprocessed files
- **Streamlit** – for building a user interface

---

## 🚀 Installation & Usage

### Prerequisites

- Python 3.x
- Install required packages:

---

## 📊  Dataset & Preprocessing

- **Dataset** - Dataset is taken from kaggel TMDB 5000 Movie Dataset in csv format link:-https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

- **Clean Dataset** - In this process csv file is clean by removeing unwanted column data and refine the data in pure textual form by using pandas ans ast library. We keep main contains detalis like movie_title ,
moive id , keyword , cast , crew(direcator only) and etc.

- **vectorization** - machine learning algorithms can't understand the textual information so we converted into numercial vector in the array form (only 'tags' cloumns are used)

- **Similarity** - Cosine similarity is used to compare movie descriptions and identify similar ones.The vector array is used in cosinie similarity , each movie assign a array of cosine similarity and convert into a similarity.pkl file due large size of this file we compresse this file into 'similarity.pkl.gz'

- **convert into pickle**- We convert the refine movies_data into a pickle file that store move data into binary formate





