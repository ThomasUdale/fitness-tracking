import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("fitness.db")
    
    cur = conn.cursor()

    cur.execute(
        """
            CREATE TABLE IF NOT EXISTS activity(
                date, 
                sport, 
                duration, 
                distance, 
                average_power, 
                average_speed, 
                average_heartrate
            )
        """
    )
