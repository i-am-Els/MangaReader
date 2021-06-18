# ------------------------------------------------------------------------------------------------------- #
import time

start_time = time.time()
half_time = 2
stop_time = 6
subfoldera = ["imagea1", "imagea2", "imagea3"]
subfolderb = ["imageb1", "imageb2", "imageb3", "imageb4", "imageb5"]
folder1 = [subfoldera, "image1 1", "image1 2", "image1 3", "image1 4"]
folder2 = [subfoldera, subfolderb, "image2 1", "image2 2", "image2 3"]
picture = [folder1, folder2]
empty_text = "NO recent reads, start reading manhwa now."
history_list = [empty_text]
dir_history = []
search_dir = []
    
# ------------------------------------------------------------------------------------------------------- #

# class WelcomeDisplay:
def welcome_page():
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        

        if elapsed_time > half_time:
            print("eMANGAreader")
            break

    current_time = 0

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time   
        
        if elapsed_time > stop_time:
            print("eMANHWArader")
            break

# ------------------------------------------------------------------------------------------------------- #

# class InfoPage:
def info_page():
    def open_index(list_name):
            for a in list_name:
                print(a)
    # -------------------------------------------------------------------- #
    def loop_history():
        print("Recent reads")
        for history in history_list:
            print(history_list.index(history), history)
    # -------------------------------------------------------------------- #
    def directory_nav(current_dir):
        dir_history.append(current_dir)
        search_dir.append(current_dir)
        open_index(current_dir)
        # ---------------------------------------------------------------- #
        def back():
            if len(dir_history) > 2:
                current_dir = dir_history[-2]
                dir_history.pop(-1)
                open_index(current_dir)
                nav(current_dir)
            elif len(dir_history) == 2:
                current_dir = dir_history[0]
                dir_history.pop(-1)
                open_index(current_dir)
                nav(current_dir)
            else:
                current_dir = dir_history[0]
                dir_history.pop(-1)
                open_index(current_dir)
                nav(current_dir)
        # ---------------------------------------------------------------- #
        def nav(current_dir):
            nav_option = input("directory index:>>> ")
            if nav_option != 'q':
                current_dir = current_dir[int(nav_option)]
                if all(isinstance(x, str) for x in current_dir):
                # call image viewer function
                    image_viewer(current_dir)
                else:
                    directory_nav(current_dir)     
            else:
                back()
        nav(current_dir)
    # -------------------------------------------------------------------- #

    # Beginning of the first class 
    print("Select Options \t\t|\t\t a. Open Manhwa folder")
    loop_history()
    option = input("Enter Choice:>>> ")

    if option == 'a':
        directory_nav(picture)

    else:
        if history_list[0] == empty_text:
            print(empty_text)
            directory_nav(picture)
        else:
            link = int(option)
            image_viewer(history_list, link)# locate link history directory

# ------------------------------------------------------------------------------------------------------- #

# class ImageViewer:
def image_viewer(dirr):

    def back():
        if len(dir_history) > 2:
            current_dir = dir_history[-2]
            dir_history.pop(-1)
            open_index(current_dir)
            nav(current_dir)
        elif len(dir_history) == 2:
            current_dir = dir_history[0]
            dir_history.pop(-1)
            open_index(current_dir)
            nav(current_dir)
        else:
            current_dir = dir_history[0]
            dir_history.pop(-1)
            open_index(current_dir)
            nav(current_dir)
    # -------------------------------------------------------------------- #
    history_list.remove(empty_text)
    print(dirr[0])
    history_list.append(dirr[0])
    # ----------------------------------------------------------------------------------- #
    def move(i):
        while i < len(dirr):
            button = input("p for previous | n for next>>> ")
            if (i == 0 or i < (len(dirr) - 1)) and button == 'n':
                i = i + 1
                print(dirr[i])
                history_list.append(dirr[i])

            elif (i == (len(dirr) - 1) or i > 0) and button == 'p':
                i = i - 1
                print(dirr[i])
                history_list.append(dirr[i])
            elif button == 'q':
                back()
            else:
                move(i = i)

    move(0)
    # ----------------------------------------------------------------------------------- #
    # returns user to info_page


    # Read for type of object, if present object is string use image viewer() else 
    # enter the directory amd run image viewer(dir)  

    # append current_dir,and present object index to history

def image_viewer_history(dirr, location):
    print(dirr[location])
    def search_in():
        for item in history_list:
            for objects in search_dir:
                if (item in objects):
                    locate = objects
        image_viewer(locate)

# ------------------------------------------------------------------------------------------------------- #

# welcome_page()
info_page()
# ------------------------------------------------------------------------------------------------------- #