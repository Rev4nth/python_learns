# Ex-2
# Write a function say_hello which takes arbitrary number of names as argument
#and prints hello, <name>


# say_hello('goutham')
#
# # Output: Hello, goutham
#
# say_hello('goutham','ng','pg')

# Output:
# Hello, goutham
# Hello, ng
# Hello, pg
def say_hello(*names):
  for name in names:
    print "Hello" , name
def main():
  say_hello("goutham")
  say_hello('goutham','ng','pg')
if __name__ == "__main__":
  main()
