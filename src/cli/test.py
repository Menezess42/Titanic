from click_extra import command, echo, pass_context, table_format_option

@command
@table_format_option
@pass_context
def show_data_table(ctx):
    """Displays data in a formatted table."""
    data = [
        (1, "Apple", 0.75),
        (2, "Banana", 0.50),
        (3, "Orange", 0.90)
    ]
    headers = ("ID", "Fruit", "Price")
    ctx.print_table(data, headers)

if __name__ == '__main__':
    show_data_table()
