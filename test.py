
class Person:
  def __init__(self, name):
    self.name = name
    print("hello", name)

def main():
  p = Person("Mark")

if __name__ == "__main__":
  main()