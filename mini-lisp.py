# -*- coding: utf-8 -*-
from yacc import yacc, lisp_str
import cmd
 
class MiniLisp(cmd.Cmd):
    """
    MiniLisp evalúa expresiones sencillas con sabor a lisp
    """
 
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "ml> "
        self.intro  = "Bienvenido a MiniLisp"
 
    def do_exit(self, args):
        """Exits from the console"""
        return -1
 
    def do_EOF(self, args):
        """Exit on system end of file character"""
        print "Good bye!"
        return self.do_exit(args)
 
    def do_help(self, args):
        print self.__doc__
 
    def emptyline(self):
        """Do nothing on empty input line"""
        pass
 
    def default(self, line):
        """Called on an input line when the command prefix
           is not recognized.
           In that case we execute the line as Python code.
        """
        result = yacc.parse(line)
        s = lisp_str(result)
        if s != 'nil':
            print s
 
if __name__ == '__main__':
        ml = MiniLisp()
        ml.cmdloop()
