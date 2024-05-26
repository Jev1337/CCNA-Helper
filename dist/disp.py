
from tkinter import Tk, Label
import argparse

def show_tooltip(text, x, y, duration):
    root = Tk()
    root.overrideredirect(True) 
    root.geometry(f"+{x}+{y}")
    label = Label(root, text=text, bg='white', relief='solid', borderwidth=1)
    #root.wm_attributes('-transparentcolor','black')
    label.pack()
    root.after(duration, root.destroy)
    root.mainloop()


parser = argparse.ArgumentParser()
parser.add_argument('--content', type=str, help='Content to show in tooltip')
parser.add_argument('--x', type=int, help='X position of the tooltip')
parser.add_argument('--y', type=int, help='Y position of the tooltip')
parser.add_argument('--duration', type=int, help='Duration of the tooltip')
args = parser.parse_args()

if args.content:
    show_tooltip(args.content, args.x, args.y, args.duration)
else:
    parser.print_help()
    exit(1)