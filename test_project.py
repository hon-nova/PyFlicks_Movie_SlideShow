from project import fetch_movies, read_from_movies, write_to_file,file_exist
import pytest

def test_project():
  
  assert file_exist("cs50PFinal.gif")

def test_fetch_movies():   
    assert fetch_movies() is not None

def test_read_show_file():
    with pytest.raises(FileNotFoundError):
        read_from_movies("readme.txt")

def test_write_to_file():
    with pytest.raises(ValueError):
        write_to_file()