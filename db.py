import sqlite3
import pandas as pd


class DatabaseManager:
    def __init__(self,database_path) -> None:
        self.conn = sqlite3.connect(database_path)
        self.cur = self.conn.cursor()

    def add_activity(
        self,
        date,
        sport,
        duration,
        distance,
        average_power,
        average_speed,
        average_heartrate
    ): 
       self.cur.execute(f"""
            INSERT INTO activity VALUES
                ('{date}','{sport}','{duration}', '{distance}','{average_power}', '{average_speed}', '{average_heartrate}')
        """)

       self.conn.commit()

    def get_activities(self):
        activities_df = pd.read_sql_query("SELECT * FROM activity",self.conn)
        return activities_df.to_dict('records')

