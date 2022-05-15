import time
import click 
from datetime import datetime

@click.command
@click.option("--hours", prompt = "Enter 'True' or skip", default = False, help = "Hours before the new year"  )

def time_ny(hours):
    current_date = datetime.today ()
    new_year = datetime(2023,1,1)
    ny =  new_year - current_date

    ty_res = time.gmtime (ny.seconds)
    res = time.strftime("%H", ty_res)
    
    if hours == True:
        click.echo (f'До нового года осталось: {ny.days} дня/дней {res} часа/часов ')
    else:
        click.echo (f'До нового года осталось: {ny.days} дня/дней')

if __name__ == '__main__':
    time_ny()




