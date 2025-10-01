# Netflix Data Analysis

This Python project focuses on analyzing Netflix's content distribution, including release trends, rating distributions, runtime analysis, and the breakdown of movies vs. shows. The analysis is performed using `pandas`, `matplotlib`, and `seaborn`.

## Features

- Visualize how Netflix content releases have changed over the years.
- Analyze rating distributions of Netflix titles.
- Study movie runtime distributions.
- Compare the number of movies vs. shows available on Netflix.

## Project Structure

```
Netflix-Data-Analysis/
├── data/                       # Raw Netflix data (e.g., netflix_titles.csv)
├── outputs/                    # Output graphs and charts
├── scripts/
│   ├── NFLX_Content-Released.py
│   ├── NFLX_Movie-Runtime-Distribution.py
│   ├── NFLX_movies_shows.py
│   └── NFLX_Rating-Distribution.py
├── requirements.txt
└── README.md
```

## Requirements

Python 3.x and the following libraries:

- pandas
- matplotlib
- seaborn

Install them using:

```bash
pip install -r requirements.txt
```

## How to Run

Simply run each Python script to generate the visualizations:

```bash
python scripts/NFLX_Content-Released.py
python scripts/NFLX_Movie-Runtime-Distribution.py
python scripts/NFLX_movies_shows.py
python scripts/NFLX_Rating-Distribution.py
```

## Author

Mohammad Mohebifard  
Licensed under the MIT License.
