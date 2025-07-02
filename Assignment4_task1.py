sample = open ("sample.txt", "r+")
# Read the content of the file
content_read = sample.readline().strip()
content_read2 = sample.readline().strip()
print ("Line 1: ", content_read)
print ("Line 2: ", content_read2)
sample.close()


#error message cleanely that the file samples.txt was not found, in case file does not exist
try:
    samples = open ("samples.txt", "r")
    samples.close()
except FileNotFoundError:
     print("Error: The file 'samples.txt' was not found.")
    
