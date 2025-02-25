"""
Implement a program that prompts the user for the name of a file then output's that file's media type
if the file's name ends, case insensitively, in any of these suffixes :
- .gif = image/gif
- .jpg = image/jpg
- .jpeg = image/jpeg
- .png = image/png
- .pdf = application/pdf
- .txt = text/plain
- .zip = application/zip
If the file name ends with some other suffix or has no suffix at all
    output "application/octet-stream" instead, which is a common default
"""

def main() :
    
    filename = input("File name : ")

    print(assign_extension(filename))


def assign_extension(file) :
    
    file = file.lower().strip()

    if ".jpg" in file or ".jpeg" in file or ".gif" in file or ".png" in file :
        message = "images/"
        if ".jpg" in file or ".jpeg" in file :
            message += "jpeg"
        elif ".gif" in file :
            message += "gif"
        else :
            message += "png"

    elif ".txt" in file :
        message = "text/plain"
    elif ".pdf" in file :
        message = "application/pdf"
    elif ".zip" in file :
        message = "application/zip"
    else :
        message = "application/octet-stream"

    return message
    

main()