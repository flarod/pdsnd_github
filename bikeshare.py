import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Specify the city you are interested in:\n') .lower()
    while city not in ['chicago', 'new york city', 'washington']:
        print('Sorry, that\'s not a valid city')
        city = input('Specify the city you are interested in:') .lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Specify the month you\'re interested in, if all state all:\n' ).lower()
    while month not in ['january', 'february', 'march', 'april','may', 'june', 'all']:
        print('Sorry, that\'s not a valid option')
        month = input('Specify the month you\'re interested in, if all state all:' ).lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Specify the day you\'re interested in, if all state all:\n').lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        print('Sorry, that\'s not a valid option')
        day = input('Specify the day you\'re interested in, if all state all:').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load city file into a dataframe
    df = pd.read_csv(CITY_DATA[city] )

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].mode()[0]
    print('The most common month was: {}.'.format(months[most_common_month-1].title()))


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day was: {}.'.format(most_common_day))


    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour was: {}h.'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station was: {}.\n'.format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station was: {}.\n'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('The most common trip was: {}.'.format(popular_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total usage time was: {} h {} min {} seconds.\n'.format(int(total_travel_time//3600), int(total_travel_time%3600)//60, int(total_travel_time%3600)%60))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average trip duration was: {} h {} min {} seconds'.format(int(mean_travel_time//3600), int(mean_travel_time%3600)//60, int(mean_travel_time%3600)%60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('This were the amount of rides per user type:\n\n{}\n'.format(user_types[:-1]))
    try:
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('This were the amount of rides per user gender (if known):\n\n{}\n'.format(gender_count))

        # TO DO: Display earliest, most recent, and most common year of birth
        min_year_birth = int(df['Birth Year'].min())
        max_year_birth = int(df['Birth Year'].max())
        mode_year_birth = int(df['Birth Year'].mode())
        print('The oldest user was born in {}.'.format(min_year_birth))
        print('The youngest user was born in {}.'.format(max_year_birth))
        print('The majority of the users were born in {}.'.format(mode_year_birth))
    except KeyError:
        print('This city has no information regarding gender or birth dates.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_stats(df):
    i = 0
    raw = input("\nWould you like to see first 5 rows of your selected parameters? type 'yes' or 'no'\n").lower()
    pd.set_option('display.max_columns',20)
    #provide option to get a limpse at the original data
    while True:
        if raw in ['no', 'n']:
            break
        print(df[i:i+5])
        raw = input('\nWould you like to see next rows of raw data? y/n \n').lower()
        i += 5
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes','y']:
            break


if __name__ == "__main__":
	main()
