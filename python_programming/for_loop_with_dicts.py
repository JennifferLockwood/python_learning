# for_loop_with_dicts.py

def main():
    person = {'name':'Andrew Erlichson', 'favorite_color':'blue',
              'hair':'brown'}

    for key in person:
        print("key is " + key + ", value is " + person[key])

main()
