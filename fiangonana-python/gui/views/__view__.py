from abc import ABC , abstractclassmethod

class View (ABC) :
    @abstractclassmethod
    def set_layout_config(self):
        print("Layout config might not be definded")

    @abstractclassmethod
    def remove_layout(self):
        print("There is no layout to avoid")
