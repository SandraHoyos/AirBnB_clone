#!/usr/bin/python3

import cmd
import os
from models.base_model import BaseModel
import models
"""
Admin Console

"""


class HBNBCommand(cmd.Cmd):
    """Interpreter"""
    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel
    }

    def do_EOF(self, args):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_clear(self, args):
        """Clear Window
        """
        os.system('clear')

    def emptyline(self):
        """Empty Line"""
        pass

    def do_create(self, args):
        """Create instances"""
        args = args.split(' ')
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            print(instance.id)
            models.storage.save()

    def do_show(self, args):
        """Print instances"""
        args = args.split(' ')
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.classes:
            if len(args) > 1:
                x = models.storage.all()
                key = args[0] + "." + args[1]
                if key in x:
                    print(x)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Destroy instances by id"""
        args = args.split(' ')
        if len(args[0]) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) <= 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key = args[0] + "." + args[1]
            if key in obj:
                del obj[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Give all instances"""
        args = args.split(' ')
        new_list = []
        # for key, value in self.__objects.items():
        #     new_json[key] = value.to_dict()
        if len(args[0]) == 0:
            for obj in models.storage.all().values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] in HBNBCommand.classes:
            for key, values in models.storage.all().items():
                if args[0] in key:
                    new_list.append(values.__str__())
            print(new_list)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
