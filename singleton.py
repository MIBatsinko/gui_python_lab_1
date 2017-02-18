class Singleton():
    def __new__(this):
        if not hasattr(this, '_instance'):
            orig = super(Singleton, this)
            this._instance = orig.__new__(this)
        return this._instance

if __name__ == '__main__':
    class ClassS(Singleton):
        pass

    test1_1, test1_2 = ClassS(), ClassS()
    test2_1, test2_2 = Singleton(), Singleton()

    try:
        test1_1.singleton, test1_2.singleton = "Test 1.1", "Test 1.2"
        test2_1.singleton, test2_2.singleton = "Test 2.1", "Test 2.2"

        print(test1_1.singleton, test1_2.singleton)
        print(test2_1.singleton, test2_2.singleton)

        del test2_1.singleton
        print(test2_1.singleton, test2_2.singleton)
    except AttributeError:
        print("AttributeError!")
