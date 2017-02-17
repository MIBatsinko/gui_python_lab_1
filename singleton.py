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

    print('test1_1:  %s\ntest1_2: %s' % (test1_1, test1_2))
    print()
    print('test2_1:  %s\ntest2_2: %s' % (test2_1, test2_2))
