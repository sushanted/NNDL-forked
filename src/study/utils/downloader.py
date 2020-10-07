import os
import urllib2

def download_data(url,files,dir='data'):

    if not os.path.exists(dir):
        os.makedirs(dir)

    for file in files:

        local_file = dir + "/" + file
        if (not os.path.isfile(local_file)):
            remote_file_name = url +"/" + file
            remote_file = urllib2.urlopen(remote_file_name)
            with open(local_file, "w") as output:
                print("Downloading %s from %s" % (local_file,remote_file_name))
                output.write(remote_file.read())