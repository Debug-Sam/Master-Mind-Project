from controllers.datacontroller import DataController as DC
from views.menu import Menu as MN

print(__name__)
if __name__ == "__main__":
    print(MN.introduction())
    var_menu = MN()

    while True:
        var_menu.menu()
