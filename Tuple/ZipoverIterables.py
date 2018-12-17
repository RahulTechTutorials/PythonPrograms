def main():
    '''This program is to understand the zip functionality over Tuples and other iterables'''
    fruits=('Apple','Banana','Kiwi','Orange')
    colors=('Red','Yellow','Brown','Orange')
    quantity=['1 kg','2 kg','3 kg','4 kg']
    Comblist = list(zip(fruits,colors,quantity))
    print(Comblist)
    

if __name__ == '__main__':
    main()
