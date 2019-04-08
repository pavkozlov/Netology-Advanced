import pandas as pd


def count_top3(years: list):
    all_df = pd.DataFrame()
    for year in years:
        my_df = pd.read_csv(f'names/yob{year}.txt', names=['name', 'gender', 'count'])
        all_df = pd.concat([my_df, all_df])
    all_df = all_df.groupby('name').sum().reset_index()
    all_df = all_df.sort_values(['count'], ascending=False).head(3)
    print(list(all_df['name']))


count_top3([1900, 1950, 2000])
count_top3([1880])


def count_dynamics(years):
    my_dict = dict()
    male_dynamics = list()
    female_dynamics = list()
    for year in years:
        my_df = pd.read_csv(f'names/yob{year}.txt', names=['name', 'gender', 'count'])
        my_df = my_df.groupby('gender').sum().reset_index()

        male_df = my_df[my_df['gender'] == 'M']
        female_df = my_df[my_df['gender'] == 'F']

        male_dynamics += list(male_df['count'])
        female_dynamics += list(female_df['count'])

    my_dict['M'] = male_dynamics
    my_dict['F'] = female_dynamics
    print(my_dict)


count_dynamics([1900, 1950, 2000])
