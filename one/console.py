#!/usr/bin/python3
"""command line interpreter"""

import cmd
import json
import re
import sys
import * from models
import storage from models


class HBNBCommand(cmd.Cmd):
    """class of command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, *args):
        """ Usage: EOF
            Functio: exit the program

        """
        print()
        return True

    def do_quit(self, *args):
        """ Usage: quit
            Function: exit the program
        """
        # quit()
        return True

    def do_create(self, line):
        """ Usage: 1. create <class name> | 2. <class name>.create()
            Function: create class instance
        """
        if line != "" or line is not None:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_intance = storage.classes()[line]()
                obj_intance.save()
                print(obj_intance.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Usage: 1. show <class name> | 2. <class name>.(id)
            Function: show class instance details
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                if class_name in storage.classes():
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        print(instance_dict)
                else:
                    print("** class doesn't exist **")

    def do_destory(self, line):
        """ Usage: 1. show <class name> | 2. <class name>.(id)
            Function: show class instance details
        """
        if line == "" or line is None:
            print("** class name missing **")

        else:
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                if class_name in storage.classes():
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        del storage.all()[key]
                        storage.save()
                        return
                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        """ Usage: 1. all | 2. <class name> | 3. <class name>.all()
            Function: print string presesntation of all  instance
        """
        instance_obj = storage.all()
        instance_list = []

        if line == "" or line is None:
            for key, value in storage.all().items():
                instance_list.append(str(value))
            print(instance_list)
        else:
            if line not in storage.classes():
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    class_name, instance_id = key.split(".")
                    if line == class_name:
                        instance_list.append(str(value))
                        print(instance_list)

    def do_update(self, line):
        """usage: 1. update <class name> <id> <attribute> <value> | \
           2. <class name> <id> <attribute> <value> \
           3. <class name>.update((<id> <dictionary>) \
           Functio: update the instance ofthe class
        """
        checks = re.search(r"^(\w+)\s([\S]+?)\s({.+?})$", line)
        if checks:
            class_name = checks.group(1)
            instance_id = checks.group(2)
            update_dict = checks.group(3)

            if class_name is None:
                print("** class name missing **")
            elif instance_id is None:
                print("** instance id missing **")
            elif update_dict is None:
                print("** attribute name missing **")
            else:
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                else:
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        update_dict = json.loads(update_dict)

                        attributes = storage.attributes()[class_name]
                        for key, value in update_dict.items():
                            if key in attributes:
                                value = attributes[key](value)
                                setattr(instance_dict, key, value)
                                storage.save()
        else:
            class_name = checks.group(1)
            instance_id = checks.group(2)
            attribute = checks.group(3)
            value = checks.group(4)

            if class_name is None:
                print("** class name missing **")
            elif instance_id is None:
                print("** instance id missing **")
            elif attribute is None:
                print("** attribute name missing **")
            elif value is None:
                print("** value missing **")
            else:
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                    else:
                        instance_dict = storage.all()[key]
                        attributes_dict = storage.attributes()[class_name]
                        value = attributes[key](value)
                        setattr(instance_dict, key, value)
                        storage.save()

    def emptyline(self):
        pass

    def precmd(self, line):
        if not sys.stdin.isatty():
            print()

        checks = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if checks:
            class_name = checks.group(1)
            command = checks.group(2)
            args = checks.group(3)

            if args is None:
                line = f"{command} {class_name}"
                return ''
            else:
                args_checks = re.search(r"^\"([^\"]*)\"(?:, (.*))?$", args)
                instance_id = args_checks[1]

                if args_checks.group(2) is None:
                    line = f"{command} {class_name} {instance_id}"
                else:
                    attribute_part = args_checks.group(2)
                    line = f"{command} {class_name} {instance_id} \
                             {attribute_part}"
                return ''

        return cmd.Cmd.precmd(self, line)

    def do_count(self, line):
        """usage: 1. count <class name> | 2. <class name>.count()
           Function: count all the instance of the class
        """
        count = 0

        for key in storage.all().keys():
            class_name, instance_id = key.split(".")
            if line == class_name:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
