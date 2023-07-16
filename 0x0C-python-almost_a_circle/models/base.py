#!/usr/bin/python3
"""scripts contains a base class for the model"""
import json
import csv
import turtle


class Base:
    """A class that serve as the base class for all other class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dict): is a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instance who inherits of base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                result = [objs.to_dictionary() for objs in list_objs]
            f.write(Base.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """ return the list represented by json_string

        Args:
            json_string (str): the string representing a list of dictionaries
            """
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set

        Args:
            dictionary (dict): dictionary containing the attributes
        """
        shapes = {
                'Rectangle': (1, 1, 0, 0),
                'Square': (1, 0, 0, None)
            }
        if cls.__name__ in shapes.keys():
            shape = cls(*shapes[cls.__name__])
            shape.update(**dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                instances_data = cls.from_json_string(f.read())
                return [cls.create(**d) for d in instances_data]
        except IOError:
            return []

    @staticmethod
    def build_field(c):
        """build the fieldnames for the csv reader or writer based on class"""
        if c.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instances who inherits from Base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                fieldnames = cls.build_field(cls)
                csv_writer = csv.DictWriter(f,
                                            fieldnames=fieldnames)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a CSV string representation to a python object"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, encoding="utf-8") as f:
                reader = csv.DictReader(f,
                                        fieldnames=cls.build_field(cls))
                list_dicts = [dict((k, int(v)) for k, v in d.items())
                              for d in reader]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): a list of rectangle objects to draw.
            list_squares (list): a list of square objects to draw
        """
        shap = turtle.Turtle()
        shap.screen.bgcolor("black")
        shap.hideturtle()

        def _displayshape(color, objects):
            """displays the shape"""
            shape.color(color)
            for obj in objects:
                shap.penup()
                shap.goto(obj.x, obj.y)
                shap.pendown()

            for i in range(2):
                shap.forward(obj.width)
                shap.left(90)
                shap.forward(obj.height)
                shap.left(90)

        _displayshape("blue", list_rectangles)
        _displayshape("pink", list_squares)

        turtle.exitonclick()
