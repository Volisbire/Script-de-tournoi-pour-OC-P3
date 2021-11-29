from tkinter import *
from tkinter import Entry

from PIL import ImageTk, Image

from PawnPatrol import *

fen_princ = Tk()
img = ImageTk.PhotoImage(Image.open("chess club.png"))
panel = Label(fen_princ, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
fen_princ.title("Chess tournament v1.0.0.1")
fen_princ.geometry("900x600")

zoneMenu = Frame(fen_princ, borderwidth=3, bg="#557788")
zoneMenu.pack(fill=X)

menuPlayer = Menubutton(zoneMenu, text="Player", width="20", borderwidth=2, bg="gray", activebackground="darkorange",
                        relief=RAISED)
menuPlayer.grid(row=0, column=0)
menuTournament = Menubutton(zoneMenu, text="Tournament", width="20", borderwidth=2, bg="gray",
                            activebackground="darkorange",
                            relief=RAISED)
menuTournament.grid(row=0, column=1)

menuSave = Menubutton(zoneMenu, text="Save/Load", width="20", borderwidth=2, bg="gray", activebackground="darkorange",
                      relief=RAISED)
menuSave.grid(row=0, column=2)


def add_players():
    def next_player():
        entry_lastname.delete(0, END)
        entry_firstname.delete(0, END)
        entry_birth.delete(0, END)
        entry_sex.delete(0, END)
        entry_rank.delete(0, END)

    def register_player1():
        players.player_list.append(Player(entry_lastname.get(), entry_firstname.get(), entry_birth.get(),
                                          entry_sex.get(), entry_rank.get()))

    app = Tk()
    app.geometry('300x200')
    app.title("Chess tournament v1.0.0.1")

    lastname = Label(app, text="Lastname :")
    lastname.grid(column=0, row=0, sticky=W)

    firstname = Label(app, text="Firstname :")
    firstname.grid(column=0, row=1, sticky=W)

    birth = Label(app, text="Birth :")
    birth.grid(column=0, row=2, sticky=W)

    sex = Label(app, text="Sex :")
    sex.grid(column=0, row=3, sticky=W)

    rank = Label(app, text="Rank :")
    rank.grid(column=0, row=4, sticky=W)

    lastname_string = StringVar()
    firstname_string = StringVar()
    birth_string = StringVar()
    sex_string = StringVar()
    rank_string = StringVar()
    entry_lastname = Entry(app, width=20, textvariable=lastname_string)
    entry_firstname = Entry(app, width=20, textvariable=firstname_string)
    entry_birth = Entry(app, width=20, textvariable=birth_string)
    entry_sex = Entry(app, width=20, textvariable=sex_string)
    entry_rank = Entry(app, width=20, textvariable=rank_string)

    entry_lastname.grid(column=1, row=0, padx=10)
    entry_firstname.grid(column=1, row=1, padx=10)
    entry_birth.grid(column=1, row=2, padx=10)
    entry_sex.grid(column=1, row=3, padx=10)
    entry_rank.grid(column=1, row=4, padx=10)

    result_button1 = Button(app, text="Register", command=register_player1)
    result_button2 = Button(app, text="Next player", command=next_player)

    result_button1.grid(column=0, row=5, pady=10, sticky=W)
    result_button2.grid(column=1, row=5, pady=10, sticky=E)

    app.mainloop()


def update_rank():
    pass


menuDeroulant1 = Menu(menuPlayer, tearoff=0)
menuDeroulant1.add_command(label="Add players", command=add_players)
menuDeroulant1.add_command(label="Update rank", command=update_rank)

menuPlayer.configure(menu=menuDeroulant1)


def start_tournament():
    start_tournament_()


def add_tournament():
    def cancel_tournament():
        entry_tournament_name.delete(0, END)
        entry_place.delete(0, END)
        entry_dated.delete(0, END)
        entry_tournament_type_string.delete(0, END)
        entry_comments.delete(0, END)

    def register_tournament():
        registered_tournament(entry_tournament_name.get(), entry_place.get(), entry_dated.get(),
                              entry_tournament_type_string.get(), entry_comments.get())

    app = Tk()
    app.geometry('300x200')
    app.title("Chess tournament v1.0.0.1")

    tournament_name = Label(app, text="Tournament name :")
    tournament_name.grid(column=0, row=0, sticky=W)

    place = Label(app, text="Place :")
    place.grid(column=0, row=1, sticky=W)

    dated_type = Label(app, text="Dated :")
    dated_type.grid(column=0, row=2, sticky=W)

    tournament_type = Label(app, text="Tournament type :")
    tournament_type.grid(column=0, row=3, sticky=W)

    comments = Label(app, text="Comments :")
    comments.grid(column=0, row=4, sticky=W)

    tournament_name_string = StringVar()
    place_string = StringVar()
    dated_string = StringVar()
    tournament_type_string = StringVar()
    comments_string = StringVar()
    entry_tournament_name = Entry(app, width=20, textvariable=tournament_name_string)
    entry_place = Entry(app, width=20, textvariable=place_string)
    entry_dated = Entry(app, width=20, textvariable=dated_string)
    entry_tournament_type_string = Entry(app, width=20, textvariable=tournament_type_string)
    entry_comments = Entry(app, width=20, textvariable=comments_string)

    entry_tournament_name.grid(column=1, row=0, padx=10)
    entry_place.grid(column=1, row=1, padx=10)
    entry_dated.grid(column=1, row=2, padx=10)
    entry_tournament_type_string.grid(column=1, row=3, padx=10)
    entry_comments.grid(column=1, row=4, padx=10)

    result_button1 = Button(app, text="Register", command=register_tournament)
    result_button2 = Button(app, text="Cancel", command=cancel_tournament)

    result_button1.grid(column=0, row=5, pady=10, sticky=W)
    result_button2.grid(column=1, row=5, pady=10, sticky=E)

    result_string = StringVar()
    result_label = Label(app, textvariable=result_string)
    result_label.grid(column=1, row=5, padx=10, sticky=W)

    app.mainloop()


def add_point():
    app2 = Tk()
    app2.geometry('300x200')
    app2.title("Chess tournament v1.0.0.1")

    winner_name = Label(app2, text="Winner lastname :")
    winner_name.grid(column=0, row=0, sticky=W)

    loser_name = Label(app2, text="Loser lastname :")
    loser_name.grid(column=0, row=1, sticky=W)

    winner_name_string = StringVar()
    loser_name_string = StringVar()
    entry_winner_name = Entry(app2, width=20, textvariable=winner_name_string)
    entry_loser_name = Entry(app2, width=20, textvariable=loser_name_string)
    entry_winner_name.grid(column=1, row=0, padx=10)
    entry_loser_name.grid(column=1, row=1, padx=10)

    result_string = StringVar()
    result_label = Label(app2, textvariable=result_string)
    result_label.grid(column=1, row=5, padx=10, sticky=W)

    def draw():
        pass

    def add():
        add_point_(entry_winner_name.get())

    result_button3 = Button(app2, text="Draw", command=draw)
    result_button3.grid(column=0, row=5, pady=10, sticky=W)
    result_button4 = Button(app2, text="Add point", command=add)
    result_button4.grid(column=1, row=5, pady=10, sticky=E)

    app2.mainloop()


menuDeroulant2 = Menu(menuTournament, tearoff=0)
menuDeroulant2.add_command(label="Create tournament", command=add_tournament)
menuDeroulant2.add_command(label="Start tournament", command=start_tournament)
menuDeroulant2.add_command(label="Add point to player", command=add_point)

menuTournament.configure(menu=menuDeroulant2)


def save_tournament():
    pass


def load_tournament():
    pass


menuDeroulant3 = Menu(menuSave, tearoff=0)
menuDeroulant3.add_command(label="Save tournament", command=save_tournament)
menuDeroulant3.add_command(label="Load tournament", command=load_tournament)

menuSave.configure(menu=menuDeroulant3)

fen_princ.mainloop()
