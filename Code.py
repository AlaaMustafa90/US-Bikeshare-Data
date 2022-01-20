import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['january','february','march','april','may','june','all']
day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city_inquiry, month_inquiry, day_inquiry = False, False, False
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        if not city_inquiry:
            city = input("What is the city you're inquiring about (chicago, new york city, washington)? ")
            city = city.lower()
            if city not in CITY_DATA:
                print("Apperciate choosing from the below/n(chicago, new york city, washington)")
                continue
            else:
                city_inquiry = True
        print("\n")
    # get user input for month (all, january, february, ... , june)
        if not month_inquiry:
            month = input("Can you please specify the month (all, january, february, ... , june)? ")
            month = month.lower()
            if month not in month_list:
                print("Apperciate choosing from (all, january, february, ... , june)")
                continue 
            else:
                month_inquiry = True
        print("\n")
    # get user input for day of week (all, monday, tuesday, ... sunday)
        if not day_inquiry:
            day = input("Can you please specify the day (all, monday, tuesday, ... sunday)? ")
            day = day.lower()
            if day not in day_list:
                print("Apperciate choosing from the below'/n(all, monday, tuesday, ... sunday)")
                continue 
            else:
                day_inquiry = True
                break
        print("\n")
        
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
    df = pd.read_csv(CITY_DATA.get(city), parse_dates = ['Start Time', 'End Time'])
    
    df['start month'] = df['Start Time'].dt.month_name()
    df['start day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['start month'] == month.title() ]
    if day != 'all':
        day = day
        df = df[df['start day'] == day]
    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    
    if month == "all":
        most_common_month = df['start month'].value_counts().idxmax()
        print("The most common month: ", most_common_month)
    else:
        print("You have specified the month earlier", month)
    
    
    # display the most common day of week
    
    if day == "all":
        most_common_day_of_week = df['start day'].value_counts().idxmax()
        print("The most common day: ", most_common_day_of_week)
    else:
        print("You have specified the day earlier", day)
    # display the most common start hour
    
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour: ", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start Station: ", most_common_start_station)
    # display most commonly used end station
    most_common_End_station = df['End Station'].value_counts().idxmax()
    print("The most common End Station: ", most_common_End_station)
    # display most frequent combination of start station and end station trip
    most_common_Start_and_End_station = df[['Start Station', 'End Station']].mode().loc[0]

    print("The most common Start and End Station: {}, and {}". 
        format(most_common_Start_and_End_station[0],most_common_Start_and_End_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel time: ", total_travel_time)
    # display mean travel time
    travel_time_mean = df['Trip Duration'].mean()
    print("Travel time mean: ", travel_time_mean)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users =  df['User Type'].value_counts()
    print("counts of user types:\n", users)
    # Display counts of gender
    if 'Gender' in df:
        gender =  df['Gender'].value_counts()
        print("counts of Gender:\n", gender)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
       earliest =  df['Birth Year'].min()
       most_recent =  df['Birth Year'].max()
       most_common = df['Birth Year'].value_counts().idxmax()
       print("earliest date of birth: ", earliest)
       print("most recent date of birth: ", most_recent)
       print("most common date of birth: ", most_common)
       print("\nThis took %s seconds." % (time.time() - start_time))
       print('-'*40)
    else:
        print('Birth Year cannot be calculated because Gender does not appear in the dataframe')

def show_raw_data(df):
    choice = input("Would you like to view the raw data [Yes, No]")
    count = 0 
    if choice.lower() == "yes":
        for row in df.iterrows():
            print(row)
            count += 1
            if count != 0 and count % 5 == 0:
                choice = input("Would you like to view the raw data [Yes, No]")
                if choice.lower() != "yes":
                    break        
               
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:
            print("No Data available, please rechoose your fliters")
            continue
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

    
if __name__ == "__main__":
    main()