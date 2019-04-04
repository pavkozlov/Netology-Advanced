import pandas as pd


def count_top3(years: list):
    if len(years) == 1:
        my_df = pd.read_csv(f'names\yob{years[0]}.txt', names=['name', 'gender', 'count'])
        my_df = my_df.sort_values(['count'], ascending=False).head(3)
        print(list(my_df['name']))
    else:
        all_df = pd.DataFrame()
        for year in years:
            my_df = pd.read_csv(f'names\yob{year}.txt', names=['name', 'gender', 'count'])
            all_df = pd.concat([my_df, all_df])
        all_df = all_df.sort_values(['count'], ascending=False).head(3)
        print(list(all_df['name']))


count_top3([1900, 1950, 2000])
count_top3([1880])


def count_dynamics(years):
    my_dict = dict()
    for year in years:
        my_df = pd.read_csv(f'names\yob{year}.txt', names=['name', 'gender', 'count'])
        male_df = my_df[my_df['gender'] == 'M']
        female_df = my_df[my_df['gender'] == 'F']
        if 'M' in my_dict:
            my_dict['M'] = my_dict['M'] + [len(male_df)]
            my_dict['F'] = my_dict['F'] + [len(female_df)]
        else:
            my_dict['M'] = [len(male_df)]
            my_dict['F'] = [len(female_df)]
    print(my_dict)


count_dynamics([1900, 1950, 2000])
