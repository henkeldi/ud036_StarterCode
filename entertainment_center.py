"""
This module creates a website with movies.
"""

import fresh_tomatoes as ft
import media


def main():
    """Creates a movie website"""

    movie1 = media.Movie(
        "The Redemption",
        "https://images-na.ssl-images-amazon.com/images/" +
        "M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRl" +
        "YWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
        "https://www.youtube.com/watch?v=6hB3S9bIaco"
    )

    movie2 = media.Movie(
        "The Godfather",
        "https://images-na.ssl-images-amazon.com/images/" +
        "M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM" +
        "2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@." +
        "_V1_SY1000_CR0,0,700,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=sY1S34973zA"
    )

    movie3 = media.Movie(
        "The Godfather: Part II",
        "https://images-na.ssl-images-amazon.com/images/" +
        "M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4Yj" +
        "I1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@." +
        "_V1_SY1000_CR0,0,702,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=9O1Iy9od7-A"
    )

    movie4 = media.Movie(
        "The Dark Knight",
        "https://images-na.ssl-images-amazon.com/images/" +
        "M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyM"
        "Tk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=EXeTwQWrcwY"
    )

    movie5 = media.Movie(
        "12 Angry Men",
        "https://images-na.ssl-images-amazon.com/images/" +
        "M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhN" +
        "GUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@." +
        "_V1_SY1000_CR0,0,649,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=A7CBKT0PWFA"
    )

    movie6 = media.Movie(
        "Schindler's List",
        "https://images-na.ssl-images-amazon.com/images/" +
        "M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOT" +
        "U5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=gG22XNhtnoY"
    )

    movies = [movie1, movie2, movie3, movie4, movie5, movie6]
    ft.open_movies_page(movies)


if __name__ == '__main__':
    main()
