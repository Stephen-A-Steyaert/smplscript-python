from smplscript import run

def main():
    text = input('smplscript > ')
    result, error = run(text)
    print(error.as_string() if error else result)


if __name__ == '__main__':
    main() 