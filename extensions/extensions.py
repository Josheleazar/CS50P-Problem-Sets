fnme = input("File name: ")
fnme = fnme.strip().casefold()
ext = fnme[-3:]
if ext in["gif", "png"]:
    print("image/",ext, sep='')
elif ext.endswith("jpg"):
    print("image/jpeg")
elif ext.endswith("pdf"):
    print("application/pdf")
elif ext.endswith("txt"):
    print("text/plain")
elif ext.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")