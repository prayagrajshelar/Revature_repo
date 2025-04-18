from db_utils import init_db, fetch_all_movies, insert_movies, delete_movie, get_movies_by_year
from data_analysis import top_rated_movies, average_statistics, search_movie
from file_operations import export_to_csv
from graphical_analysis import (
    plot_avg_rating_yearwise,
    plot_movies_by_genre,
    plot_top_rated_movies
)


def menu():
    print("\n IMDb Movie Dataset Analysis \n")
    print("1. View All Movies.")
    print("2. Top 10 movies by rating.")
    print("3. Average Statistics (Rating, Revenue, Runtime) ")
    print("4. Add a new Movie.")
    print("5. Export to CSV")
    print("6. Delete a Movie by Title")
    print("7. Plot: Top 10 Movies by Rating")
    print("8. Plot: Avg Rating by Year")
    print("9. Plot: Top Genres")
    print("10. Search Movie by Title")
    print("11. Search Movies by Release Year")
    print("12. Exit")

def main():
    init_db()
    while True:
        menu()
        choice = input("\nEnter Your Choice: ")
        if choice == "1":
            fetch_all_movies()
        elif choice == "2":
            top_rated_movies()
        elif choice == "3":
            average_statistics()
        elif choice == "4":
            insert_movies()
        elif choice == "5":
            export_to_csv()
        elif choice == "6":
            delete_movie()
        elif choice == "7":
            plot_top_rated_movies()
        elif choice == "8":
            plot_avg_rating_yearwise()
        elif choice == "9":
            plot_movies_by_genre()
        elif choice == "10":
            search_movie()
        elif choice == '11':
            year = input("Enter release year to search: ")
            if not year.isdigit():
                print("Please enter a valid numeric year.")
            else:
                movies = get_movies_by_year(int(year))
                if not movies.empty:
                    print(movies[['title', 'year', 'rating']])
                else:
                    print("No movies found for the given year.")
        elif choice == "12":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()