from ascii_magic import AsciiArt


pathName = input("Enter the file path of your image: ")
picture = AsciiArt.from_image(pathName)
picture.to_terminal()
picture.to_html_file('ascii_art.html', columns=200, width_ratio=2)


my_art = AsciiArt.from_image(pathName)
my_art.to_html_file('ascii_art.html', columns=200, width_ratio=2)