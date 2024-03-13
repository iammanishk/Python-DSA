import sqlite3

conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
     )
 ''')

def  list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(?, ?)", (name, time))
    conn.commit()
    
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Welcome to Youtube Manager  |  Choose your option: ")
        print("1. List all youtube videos ")
        print("2. Add a new video ")
        print("3. Update youtube video details ")
        print("4. Delete Youtube videos ")
        print("5. Exit the app ")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_all_videos()
        elif choice == 2:
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            add_video(name, time)
        elif choice == 3:
            video_id = input("Enter the id of the video you want to update: ")
            name = input("Enter the name of the video: ")
            time = input("Enter the time of the video: ")
            update_video(video_id,name, time)
        elif choice == 4:
            video_id = input("Enter the id of the video you want to delete: ")
            delete_video(video_id)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
            
    conn.close()
if __name__ == '__main__':
    main()