# @Time: 2021/5/16 18:39  
# @Author: flying
# @Desc:

class Animal(object):
    def run(self):
        print('Animal is running........')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


def main():
    dog  = Dog()
    dog.run()
    cat = Cat()
    cat.run()
    print('cat属于Animal类:' , isinstance(cat,Animal))



#  多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
#  由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思
def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == '__main__':
    main()

    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())


