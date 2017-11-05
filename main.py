from model import Model
from view import View
from controller import Controller


def main():
    m = Model()
    v = View()
    c = Controller(m, v)

    c.start_program()


if __name__ == '__main__':
    main()