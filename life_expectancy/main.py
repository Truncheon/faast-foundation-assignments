from life_expectancy.cleaning import clean_data, load_data, save_data


def main():
    df = load_data()
    clean_data(df)
    save_data(df)


if __name__ == "__main__":
    main()
