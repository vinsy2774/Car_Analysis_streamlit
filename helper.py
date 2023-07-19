
def show_top_cars(df):
    top_cars = df.sort_values(['Price'], ascending=[False]).head()
    return top_cars


def show_bottom_cars(df):
    bottom_cars = df.sort_values(['Price'], ascending=[True]).head()
    return bottom_cars


def total_cars_over_fuel_type(df, col):
    fuel_type = df[col].value_counts()
    return fuel_type


def total_cars_over_drive_type(df, col):
    drive_type = df[col].value_counts()
    return drive_type


def total_cars_over_car_type(df, col):
    car_type = df[col].value_counts()
    return car_type


def total_cars_over_owner_type(df, col):
    owner_type = df[col].value_counts()
    return owner_type


def fuel_type_bar(df):
    Fuel_type = df['Fuel'].unique().tolist()
    Fuel_type.sort()
    Fuel_type.insert(0, 'All Types')
    return Fuel_type


def drive_type_bar(df):
    drive_type = df['Drive'].unique().tolist()
    drive_type.sort()
    drive_type.insert(0, 'All Types')
    return drive_type


def car_type_bar(df):
    car_type = df['Type'].unique().tolist()
    car_type.sort()
    car_type.insert(0, 'All Types')
    return car_type


def owner_type_bar(df):
    owner_type = df['Owner'].unique().tolist()
    owner_type.sort()
    owner_type.insert(0, 'All Types')
    return owner_type


def fetch_fuel_data(df, fuel_type):

    if fuel_type == 'All Types':
        return df
    else:
        return df[df['Fuel'] == fuel_type]




