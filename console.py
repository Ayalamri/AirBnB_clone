#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

"""Contains the entry point of the command interpreter"""

import cmd
import models

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            print(models.storage.all().get(key, "** no instance found **"))
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            objs = models.storage.all()
            if key not in objs:
                print("** no instance found **")
                return
            del objs[key]
            models.storage.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = models.storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
            return
        try:
            cls_name = arg.split()[0]
            print([str(obj) for obj in objs.values()
                   if obj.__class__.__name__ == cls_name])
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(cls_name, obj_id)
            objs = models.storage.all()
            if key not in objs:
                print("** no instance found **")
                return
            obj = objs[key]
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            if hasattr(obj, attr_name):
                attr_value = type(getattr(obj, attr_name))(attr_value)
                setattr(obj, attr_name, attr_value)
                models.storage.save()
            else:
                print("** attribute doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
elif command.startswith("show User"):
    args = command.split(" ")
    if len(args) == 3:
        object_id = args[2]
        print(storage.get("User", object_id))
    else:
        print("** instance id missing **")

elif command.startswith("create User"):
    new_user = User()
    new_user.save()
    print(new_user.id)

elif command.startswith("destroy User"):
    args = command.split(" ")
    if len(args) == 3:
        object_id = args[2]
        storage.delete("User", object_id)
        storage.save()
    else:
        print("** instance id missing **")

elif command.startswith("update User"):
    args = command.split(" ")
    if len(args) < 5:
        if len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
    else:
        obj_id = args[1]
        attribute_name = args[2]
        value = args[3]
        user = storage.get("User", obj_id)
        if user:
            setattr(user, attribute_name, value)
            user.save()
        else:
            print("** no instance found **")

elif command.startswith("all User"):
    objs = storage.all("User")
    for obj in objs.values():
        print(obj)

import cmd
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        new_obj = eval(class_name)()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Show details of a specific instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    # Implement other commands like do_destroy, do_update, do_all similarly...

if __name__ == '__main__':
    HBNBCommand().cmdloop()
