import urllib
def read_text():
    filename = input("Enter the file name:")
    file_open = open(filename)
    content_of_file = file_open.read()
    # print (content_of_file)
    file_open.close()
    check_curse(content_of_file)
def check_curse(data):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+data)
    output = connection.read()
    print (output)
    connection.close
read_text()

