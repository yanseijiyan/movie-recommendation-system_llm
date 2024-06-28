# LLM Movie Recommendation System

This project implements a movie recommendation system that leverages Large Language Models (LLMs) to provide personalized movie recommendations based on user ratings and movie details.

## Project Structure

llm-movie-recommendation-system/
├── app/
│ ├── init.py
│ ├── recommendation.py
├── data/
│ ├── movies.csv
│ ├── ratings.csv
├── main.py
├── requirements.txt
└── README.md

## Setup

### Prerequisites

- Python 3.6 or higher
- Git

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/llm-movie-recommendation-system.git
    cd llm-movie-recommendation-system
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Add your OpenAI API Key:**

    Replace `'YOUR_OPENAI_API_KEY'` in `app/recommendation.py` with your actual OpenAI API key.

### Data Preparation

1. **Download MovieLens Dataset:**

    Download the [MovieLens Dataset](https://grouplens.org/datasets/movielens/) and place the `movies.csv` and `ratings.csv` files in the `data/` directory.

## Usage

### Running the Application

1. **Start the Flask Server:**

    ```bash
    python main.py
    ```

2. **Make a POST Request to Get Recommendations:**

    You can use a tool like `curl` or Postman to make a POST request to the `/recommend` endpoint. Here's an example using `curl`:

    ```bash
    curl -X POST http://127.0.0.1:5000/recommend -H "Content-Type: application/json" -d '{"user_id": 1}'
    ```

    This will return a JSON response with movie recommendations.

### Example Response

```json
[
    {
        "title": "Toy Story (1995)",
        "genres": "Adventure|Animation|Children|Comedy|Fantasy",
        "recommendation": "I think this is a great movie for kids and adults who enjoy animated adventures!"
    },
    {
        "title": "Jumanji (1995)",
        "genres": "Adventure|Children|Fantasy",
        "recommendation": "A fun and adventurous movie with a magical twist!"
    }
]
```
## Project Details

### Files
        app/__init__.py: Initializes the Flask app.
        app/recommendation.py: Contains the recommendation logic and integration with the OpenAI API.
        data/movies.csv: Contains movie details.
        data/ratings.csv: Contains user ratings for movies.
        main.py: Runs the Flask server and handles the API endpoint.
### How It Works
        Data Loading: The system loads movie details and user ratings from CSV files.
        User Similarity Calculation: Using cosine similarity, it calculates the similarity between users based on their ratings.
        Movie Recommendation: For a given user, it recommends movies that similar users have liked.
        LLM Integration: The system uses OpenAI's API to provide natural language recommendations for the movies.


## Contributing
        Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License
        This project is licensed under the MIT License.