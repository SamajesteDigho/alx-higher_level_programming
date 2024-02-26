#!/usr/bin/python3
""" This is the Base class for this model module.

    Here is defined the base class model Base use through
    out the project.
"""
import json


class Base:
    """ This is the Bass class model defining a figure

    Attributes:
        ==> __nb_objects = 0 # Representing the number of instances of Base.
        ==> id = Instance ID in activity

    Methods:
        ==> to_json_string
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON of list of dictionnaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json representation toa file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                data = [x.to_dictionary() for x in list_objs]
                file.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Converting from JSON string to JSON"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class instance with all attribut set"""
        classname = cls.__name__
        if classname == "Rectangle":
            from rectangle import Rectangle
            rec = Rectangle(width=1, height=1)
            rec.update(**dictionary)
            return rec
        elif classname == "Square":
            from square import Square
            sqr = Square(size=1)
            sqr.update(**dictionary)
            return sqr

    @classmethod
    def load_from_file(cls):
        """Loading from file"""
        classname = cls.__name__
        filename = "{}.json".format(classname)
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
                dictionaries = cls.from_json_string(content)
                data = [cls.create(**x) for x in dictionaries]
                return data
        except FileNotFoundError:
            return []
        except Exception as e:
            print("[ERROR] {}".format(e))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save object to csv file"""
        classname = cls.__name__
        filename = "{}.csv".format(classname)
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("")
            else:
                content = ""
                if classname == "Rectangle":
                    for elt in list_objs:
                        content += "{},{},{},{},{},".format(elt.id,
                                                            elt.width,
                                                            elt.height,
                                                            elt.x, elt.y)
                elif classname == "Square":
                    for elt in list_objs:
                        content += "{},{},{},{},".format(elt.id,
                                                         elt.width,
                                                         elt.x, elt.y)
                content = content[:-1]
                file.write(content)

    @classmethod
    def load_from_file_csv(cls):
        classname = cls.__name__
        filename = "{}.csv".format(classname)
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            vals = content.split(",")
            data = []
            cur = 0
            if classname == "Rectangle":
                from rectangle import Rectangle
                while cur < len(vals):
                    id = int(vals[cur])
                    width = int(vals[cur+1])
                    height = int(vals[cur+2])
                    x = int(vals[cur+3])
                    y = int(vals[cur+4])
                    rec = Rectangle(width, height, x, y, id)
                    cur += 5
                    data.append(rec)
            elif classname == "Square":
                from square import Square
                while cur < len(vals):
                    id = int(vals[cur])
                    size = int(vals[cur+1])
                    x = int(vals[cur+2])
                    y = int(vals[cur+3])
                    sqr = Square(size, x, y, id)
                    cur += 4
                    data.append(sqr)
            return data

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the rectangles and squares"""
