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
                if class_name in storage,classes():
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        print(instance_dict)

                else:
                    print("** class doesn't exist **")
 
    
    def do_destory(self, line)
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
                if class_name in storage,classes():
                     key = f"{class_name}.{instance_id}"
                     if key not in storage.all():
                         print("** no instance found **")
                     else:
                         delstorage.all()[key]
                         storage.save()
                         return
                else:
                    print("** class doesn't exist **")

    
    def do_all(self, line):










                    


