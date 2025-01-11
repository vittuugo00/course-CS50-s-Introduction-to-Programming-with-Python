fileName = input("file name: ").lower().strip()
file = fileName.split(".")

if(len(file) == 2):
    match file[1]:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "gif":
            print("image/gif")
        case "pdf":
            print("application/pdf")
        case "zip":
            print("application/zip")
        case "txt":
            print(f"text/{file[0]}")
        case _:
            print("application/octet-stream")
elif(len(file) == 3):
    match file[2]:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "gif":
            print("image/gif")
        case "pdf":
            print("application/pdf")
        case "zip":
            print("application/zip")
        case "txt":
            print(f"text/{file[0]}")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
