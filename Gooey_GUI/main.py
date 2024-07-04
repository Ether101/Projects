from gooey import Gooey, GooeyParser

@Gooey
def main():
    parser = GooeyParser()

    parser.add_argument('num_1', action='store', help = 'First number of sum', metavar = 'First Number')
    parser.add_argument('num_2', action='store', help = 'Second number of sum', metavar = 'Second Number')
    
    # Optional
    parser.add_argument('--num_3', action='store', help = 'Third number of sum', metavar = 'Third Number')

    parser.add_argument('checkbox', action = 'store_true')

    parser.add_argument('option', choices = ['Option 1', 'Option 2', 'Option 3'])

    group = parser.add_mutually_exclusive_group('selection')
    group.add_argument('--selection_1', action='store_true')
    group.add_argument('--selection_2', action='store_true')

    parser.add_argument("file_chooser", widget="FileChooser", metavar="Select file", help="Select a file on your system")
    parser.add_argument("color_picker", widget="ColourChooser", metavar="Color Picker", help="Select any color")
    parser.add_argument("date_picker", widget="DateChooser", metavar="Date Picker", help="Pick a Date")
    parser.add_argument("password", widget="PasswordField", metavar="Password", help="Enter the password")

    args = parser.parse_args()

    print(int(args.num_1) + int(args.num_2))

main()