from gyazo import Api
from keys import gyazo_access

week_num = 'Ten'

def upload_Total():
    client = Api(access_token=gyazo_access)

    with open('D:\Data_Science_Documents\Twitch_Directory\graphs\Total_all_weeks.png', 'rb') as f:
        image = client.upload_image(f)
        total_url = image.to_json()
        total_url = total_url.split('"')[-2]
    return total_url

def upload_summa():
    client = Api(access_token=gyazo_access)

    with open(f'D:\Data_Science_Documents\Twitch_Directory\graphs\Week{week_num}Summa.png', 'rb') as f:
        image = client.upload_image(f)
        summa_url = image.to_json()
        summa_url = summa_url.split('"')[-2]
    return summa_url

def upload_day():
    client = Api(access_token=gyazo_access)

    with open(f'D:\Data_Science_Documents\Twitch_Directory\graphs\Week{week_num}Day.png', 'rb') as f:
        image = client.upload_image(f)
        day_url = image.to_json()
        day_url = day_url.split('"')[-2]
    return day_url

day_link =upload_day()
summa_link =upload_summa()
total_link =  upload_Total()


def read_ReadMe():
    read_me_file = open('D:\Data_Science_Documents\Twitch_Directory\README.md', 'r')
    readme_lines = read_me_file.readlines()


    readme_lines[21] = f'![Total_all_weeks]({total_link})'

    readme_lines[-5] = f'![Day]({day_link})'

    readme_lines[-1] = f'![summa]({summa_link})'
    print(readme_lines)
    read_me_file = open('D:\Data_Science_Documents\Twitch_Directory\README.md', 'w')
    read_me_file.writelines(readme_lines)

read_ReadMe()