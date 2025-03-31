# Project Title: ML Movie Recommendation System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)]()

## 📜 Description

This project presents an interactive Movie Recommendation System built with Python and Machine Learning techniques. It utilizes content-based filtering by vectorizing movie data (specifically plot summaries, genres, keywords, cast, and crew) to find similarities between movies. The system is presented through a user-friendly web interface created with Streamlit, enhancing the experience by fetching and displaying movie posters using the TMDB (The Movie Database) API.

## ✨ Features

* **Interactive Web Interface:** Built with Streamlit for easy interaction and movie selection.
* **Machine Learning Powered Recommendations:** Leverages TF-IDF vectorization and Cosine Similarity from Scikit-learn to suggest relevant movies based on content.
* **Poster Display:** Fetches movie posters from The Movie Database (TMDB) API to provide a visually appealing experience.
* **Real-time Suggestions:** Select a movie and instantly get recommendations.

## ⚙️ How It Works

1.  **Data Loading & Preprocessing:** Movie data from the TMDB 5000 dataset is loaded using Pandas. Text features (overview, genres, keywords, cast, crew) are cleaned and combined into a single 'tags' column for each movie.
2.  **Vectorization:** The 'tags' column is transformed into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency) from Scikit-learn. This creates a TF-IDF matrix where rows represent movies and columns represent unique words weighted by importance.
3.  **Similarity Calculation:** Cosine Similarity is calculated between the TF-IDF vectors of all movies. This results in a similarity matrix where each value (i, j) represents the similarity score between movie i and movie j.
4.  **Recommendation Generation:** When a user selects a movie, the system looks up its corresponding row in the similarity matrix and retrieves the movies with the highest similarity scores (excluding the movie itself).
5.  **Poster Fetching:** The TMDB API is queried using the recommended movie IDs to retrieve URLs for their posters.
6.  **Streamlit Interface:** The Streamlit app (`app.py`) provides a dropdown for users to pick a movie title. Upon selection, it triggers the recommendation logic (using the precomputed similarity matrix and movie list) and displays the recommended movie titles along with their fetched posters via API calls.

## 🔧 Technology Stack

* **Language:** Python 3.9+
* **Web Framework:** Streamlit
* **Core Libraries:**
    * Pandas (Data manipulation)
    * NumPy (Numerical operations)
    * Scikit-learn (Specifically TfidfVectorizer, cosine_similarity)
    * Requests (For making API calls to fetch posters)
* **API:** The Movie Database (TMDB) API
* **Environment Management:** venv (recommended)

## 💾 Dataset

This project uses the **TMDB 5000 Movie Dataset**.
* **Source:** [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* **Key Features Used:** `title`, `overview`, `genres`, `keywords`, `cast`, `crew` from `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
* **Preprocessing:** Merged datasets, handled missing values, extracted relevant names from JSON columns (genres, keywords, cast, crew), combined key text features into a 'tags' column, converted text to lowercase. Precomputed movie list and similarity matrix are often saved as `.pkl` files (e.g., `movie_list.pkl`, `similarity.pkl`) for faster loading in the Streamlit app.

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[your-username]/[your-repo-name].git
    cd [your-repo-name]
    ```
    *(Replace `[your-username]/[your-repo-name]` with your actual GitHub username and repository name)*

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    # venv\Scripts\activate
    # On macOS/Linux
    # source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **API Key Setup:**
    * You will need an API key from The Movie Database (TMDB). Sign up at [https://www.themoviedb.org/signup](https://www.themoviedb.org/signup).
    * **Set an environment variable** named `TMDB_API_KEY` with your key value. The application (`app.py`) should be coded to read this environment variable.
      * _Example (Linux/macOS):_ `export TMDB_API_KEY="YOUR_API_KEY_HERE"`
      * _Example (Windows CMD):_ `set TMDB_API_KEY=YOUR_API_KEY_HERE`
      * _Example (Windows PowerShell):_ `$env:TMDB_API_KEY="YOUR_API_KEY_HERE"`
      *(Note: Environment variables might need to be set permanently depending on your system/workflow)*

5.  **Data/Model Files:**
    Ensure the necessary data files (e.g., `movie_list.pkl`, `similarity.pkl`, or the original CSVs if processing is done on the fly) are present in the correct directory as expected by your script (`app.py`). If precomputation is needed, you might need to run a separate preprocessing script first.

## ▶️ Usage

1.  Ensure your virtual environment is activated and dependencies are installed.
2.  Make sure the `TMDB_API_KEY` environment variable is set correctly (see Installation Step 4).
3.  Run the Streamlit application (assuming your main script is `app.py`):
    ```bash
    streamlit run app.py
    ```
4.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
5.  Select a movie from the dropdown menu in the web app to get recommendations.

## 🖼️ Screenshots / Demo

**(Please add screenshots of your Streamlit application here!)**

*Example Placeholder:*
`![Streamlit App Screenshot](path/to/your/screenshot.png)`
*Show the movie selection dropdown and the resulting recommendations with posters.*

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to:
1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.
*(Ensure you have a file named `LICENSE` containing the MIT License text in your repository)*

## 🙏 Acknowledgements

* The Movie Database (TMDB) for providing the dataset and the free API.
* The Streamlit team for the excellent web framework.
* Scikit-learn team for the machine learning tools.

## 📧 Contact

[Your Name] - [Your Email (Optional)] - [Link to your LinkedIn/Portfolio (Optional)]

Project Link: `https://github.com/[your-username]/[your-repo-name]`
*(Replace `[your-username]/[your-repo-name]`)*
