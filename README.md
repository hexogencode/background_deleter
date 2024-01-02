# Background deleter


## Removes image background when user enters a link on it

The following Python libraries were used in this project:
* requests, os and PIL to manipulate with image link and file
* rembg to use the u2net model to remove the background from an image

The main functionality is in one function process_image(). However, to work with rembg I had to create a temporary file that appeared in the process of removing the background.
A small interface made for ease of use of the program. Using a wile loop, the user can enter links endlessly until writes 'stop'.
