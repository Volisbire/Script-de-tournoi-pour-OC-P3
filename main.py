from Controller.PawnPatrol import PawnPatrol
from Controller.Menucommand import Menu

control = PawnPatrol()
Menu = Menu(control, testmode=True)

Menu.show()
