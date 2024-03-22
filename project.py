import sys
import os
import requests
import json
import csv
from PIL import Image
from io import BytesIO

def main():
   try:
      try:
         if len(sys.argv)<=2:
            user_input = sys.argv[1]
      except IndexError as e:
         print(e)

      if len(sys.argv)==1:
         print("Missing command-line argument")

      elif (len(sys.argv)==2 and sys.argv[1]==user_input):
         arg1_ext=sys.argv[1].split(".")[-1]
         if not arg1_ext.endswith("csv"):
            
            sys.exit(f"{sys.argv[1]} is not a CSV file")
         elif not file_exist(sys.argv[1]):           
            sys.exit("File does not exist") 

         # write_to_file()        
         show_movies()
 
   except ValueError:
       pass 

def fetch_movies():
   try:
      api_key="16c5bbc2cfbf0865d1b02a76598ce276"
      
      response=requests.get(f'https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-CA') 

      response.raise_for_status()     
      resultJson=response.json()   
      results=resultJson["results"]
      mvs=json.dumps(results,indent=2)
      images=[]
   
      mvsArr=json.loads(mvs)  
      
      for item in mvsArr:      
         images.append(item['poster_path'])    
   
      movies=[]
      
      for movie in images:         
         item=f"https://image.tmdb.org/t/p/w500{movie}"         
         movies.append(item)
      return movies 

   except requests.exceptions.HTTPError as e:
        raise ValueError(f"HTTP error occurred: {e}") from e
      
   except requests.exceptions.RequestException as e:     
        raise ValueError(f"Network error occurred: {e}") from e
  
def write_to_file():   
  
   try:
      movies=fetch_movies() 

      with open("movies.csv","w") as file:
         writer=csv.writer(file)
         for item in movies:
            item=item.strip()
            writer.writerow([item])
      raise ValueError      

   except ValueError:
      raise ValueError("Wrong file")
   
def read_from_movies(fileName):
   my_movies=[]
   movies=[]
   try:
      with open(fileName,"r") as file:
         reader=csv.reader(file)
         for row in reader:               
            my_movies.append(row) 

      for i in range(len(my_movies)):
         if i%2!=0:
            continue
         movies.append(','.join(my_movies[i]))
     
      return movies
   except FileNotFoundError:
      raise FileNotFoundError("File not found")      

def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img.resize((400,450))

def slide_animation(images):
    frames = []
    for image in images:
        width, height = image.size
        for x_offset in range(-width, 401, 10): 
            frame = Image.new("RGB", (400, 450), (255, 255, 255))
            frame.paste(image, (x_offset, 0))
            frames.append(frame)
    return frames

def show_movies():
   try:
      movies=read_from_movies("movies.csv")     
      images = []
      for image_url in movies:
         image = download_image(image_url)
         images.append(image)
   
      animation_frames = slide_animation(images)      
      
      new_image = Image.new("RGB", (400, 450), (255, 255, 255))
      new_image.save("cs50PFinal.gif", save_all=True, append_images=animation_frames, duration=200, loop=0)    

   except FileNotFoundError:
      raise FileNotFoundError("File not found")

def file_exist(fileName):
    return os.path.exists(fileName)


if __name__ == "__main__":
    main()