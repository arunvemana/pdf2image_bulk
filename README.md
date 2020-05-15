# pdf2image_bulk
`converting all pdf file pages to images from a particular folder`
## Requirment packages
poppler
pdf2image
### poppler
* Go to this page[http://blog.alivate.com.au/poppler-windows/] and download the binary of your choice. In this example we will download and use poppler-0.68.0_x86.
* Extract the archive file poppler-0.68.0_x86.7z into C:\Users\Program Files. Thus, the directory structure should look something like this:
```
C:
    └ Program Files
        └ poppler-0.68.0_x86
            └ bin
            └ include
            └ lib
            └ share
```
* Add `C:\Program Files\poppler-0.68.0_x86\bin` to your system `PATH` by doing the following: Click on the Windows start button, search for `Edit the system environment variables`, click on `Environment Variables...`, under `System variables`, look for and double-click on `PATH`, click on `New`, then add `C:\Users\Program Files\poppler-0.68.0_x86\bin`, click `OK`
### pdf2image
* pip3 install pdf2image

## Steps and Descriptions
* All the pdf's file u want to convert place it in a pdf_files folder of the script current path.
* images will be saved with filename_extracted folder inside pdf_files in `jpg` formate.
