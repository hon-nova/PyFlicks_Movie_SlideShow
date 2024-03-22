# PROJECT TITLE: PyFlicks: A Pythonic Movie Slideshow
#### Video Demo:  [PyFlicks: A Pythonic Movie Slideshow](https://youtu.be/byh574wQntY)


## I. Description:
_**What is in this project?**_

    - The project is about showing 20 movie images which are fetched from an API. 
    - Movie URL: [Movie URL](https://api.themoviedb.org/3/movie/upcoming?).
    - Inspiration: The idea comes from the lecture 6. The instructor David Malan wrote:

```python

images=[]
for arg in sys.argv[1:]:
    image=Image.open(arg)
    images.append(image)

images[0].save("costumes.gif",save_all=True,append_images=[images[1]],duration=200,loop=0)

```
    - The output of the program is a `.gif` file that contains 20 movie images. When displaying them there will be one at a time. By presenting the images sequentially, users can clearly observe each movie poster without feeling overwhelmed by the simultaneous display of all 20 images. 


## II. Workflow:

    - [x] Step 1: 
        - Description: Fetch data from an api, and write the data to a file called `movies.csv`
    - [x] Step 2: 
        - Description: Read the data from the file `movies.csv`
    - [x] Step 3: 
        - Description: Display them in the UI using the `PIL` library

## III. Functions: 

    a. `fetch_movies()`
    - Description: Obtains a list of 20 movies from the API and saves them in a variable called `movies`.
    - Images: Each movie is represented by an image URL starting with "https" and ending with ".jpg".
    b. `write_to_file()`
    - Description: Saves all movie images to a CSV file named `movies.csv`.
    c. `read_from_movies()`
    - Description: Reads movie data from the movies.csv file for further processing.
    d. `download_image(_url)`
    - Description: Converts image URLs to displayable format and resizes them to a width of 400px and height of 450px.
    e. `slide_animation(_list)`
    - Description: Generates a series of frames to simulate a sliding animation effect for a list of images.
    f. `show_movies()`
    - Description: Initiates the slideshow of movie images by invoking the three functions: read_from_movies(), download_image(_url), and slide_animation(_list).
    g. Output:
    - Description: Details the output of the project, including the creation of a GIF file named `cs50PFinal.gif`.
    - Animation: The GIF runs infinitely with a frame duration of 200 milliseconds, background as white and displaying the sliding animation effect.


## IV. How to Run the Program:

    1. In `main()` enable function `write_to_file()` and run the program with: $`python project.py movies.csv`
    2. Next, when the file `movies.csv` is already filled up with data, enable function `show_movies()`, then run the program again with  $`python project.py movies.csv`.

    >It will take about 70-120 seconds for the program to execute and generate the end product. That is the `.gif` file located in the root directory of the project. During this time frame, please do not touch your keyboard or you will get a `KeyboardInterrupt` warning message. Because of this act, the `.gif` image will not be generated as desired and you will need to run the program again.

    3. Open the file `cs50PFinal.gif` and observe the images with its animation

## V. Python Libraries Used:
```python

pip install requests
pip install pillow

```


## VI. Constraints:

> **_Writing to File_**: 

     When writing to the file `movies.csv`, the `w` mode is intentionally used instead of `a`. This decision is made to ensure that each time the project runs, the file will contain exactly 20 records. Using `a` mode would append additional records to the file, potentially causing the GIF generation process to take significantly longer. Testing has shown that when the `movies.csv` file contains 40 records or more, the resulting GIF may fail to be generated, resulting in a blank or transparent GIF file (as shown 0 KB).

## VII. Movie Image SlideShow Preview

![PyFlicks](cs50PFinal.gif)

**_THANK YOU_**



