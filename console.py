#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Conatiains the functionality for the HBNBconsole"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City, 'Amenity': Amenity,
               'Review': Review
               }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, ;longitude': float
             }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [*args> or <**kwargs>]])
        (Brackets denote iptional fields in usage example.)
        """
        _cmd = _cls = _id = _args = '' # initialize line elements

        # scan for general formatting - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try: # parse line left to right
            pline = line[:] # parsed line

            # isolate <class name>
            _cls = pline[:pline.find('.')]

            # isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # if parantheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ') # pline convert to tuple

                # isolate _id, stripping quotes
                _id = pliine[0].replace('\"', '')
                # possible bug here:
                # empty quotes register as empty _id when replaced

                # if arguments exists beyond _id
                pline = pline[2].strip() # pline is now str
                if pline:
                    # ckeck for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
                        # _args = _args.replace('\"', '')
                line = ' '.join([_cmd, _cls, _id, _args])

            except Exception as mess:
                pass
            finally:
                return line

        def postcmd(self, stop, line):
            """Prints if isatty is false"""
            if not sys.__stdin__.isatty():
                print('hbnb) ', end='')
            return stop

        def do_quit(self, command):
            """ Method to exit the HBNB console"""
            exit()

        def help_quit(self):
            """ Prints the help documentation for quit """
            print("Exits the program with formatting\n")

        def do_EOF(self, arg):
            """ Handles WOF to exit program """
            print()
            exit()

        def help_EOF(self):
            """ Prints the help docum,entation for quit """
            print("Exits the program without formatting\n")

        def emptyline(self):
            """ Overrides an object of any class"""
            pass

        def do_create(self, args):
            """ Create an object of any class"""
            try:
                if not args:
                    raise SyntaxError()
                arg_list = args.split(" ")
                kw = {}
                for arg in arg_list[1:]:
                    arg_splited = arg.split("=")
                    arg_splited = eval(arg_splited[1])
                    if type(arg_splited[1] is str:
                        arg_splited[1] = arg_splited[1].replace("_", " ").replace
