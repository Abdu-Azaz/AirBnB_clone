#!/usr/bin/python3

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '

    def do_quit(self, line):
        return True

   
    def do_EOF(self, line):
        return True
    def postcmd(self, stop, line):
        """Called after a command is executed."""
        return stop
    
if __name__ == '__main__':
    HelloWorld().cmdloop()
