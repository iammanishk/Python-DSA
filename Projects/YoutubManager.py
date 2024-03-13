import json

def load_data():
    try:
        with open("Youtube.txt", 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test

    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("Youtube.txt", 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print('\n')
    print("*" * 50)
    for index, videos in enumerate(videos, start=1):
        print(f"{index}. {videos['name']}, Duration: {videos['time']}")


def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video you want to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video you want to delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index")



def main():
    videos = load_data()
    while True:
        print("\n Welcome to Youtube Manager  |  Choose your option: ")
        print("1. List all youtube videos ")
        print("2. Add a new video ")
        print("3. Update youtube video details ")
        print("4. Delete Youtube videos ")
        print("5. Exit the app ")
        choice = int(input("Enter your choice: "))
        # print(videos)

        match choice:
            case 1:
                list_all_videos(videos)
            case 2:
                add_videos(videos)
            case 3:
                update_videos(videos)
            case 4.:
                delete_videos(videos)


if __name__ == "__main__":
    main()