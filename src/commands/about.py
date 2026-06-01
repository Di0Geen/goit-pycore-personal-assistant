from src.address_book import AddressBook
from src.decorators.input_error import input_error

TEAM_MEMBERS = [
    {
        "name": "Mykhailo Zhar",
        "role": "[bold cyan]Team Lead[/bold cyan]",
    },
    {
        "name": "Kostiantyn Krysenko",
        "role": "[bold green]Developer[/bold green]",
    },
    {
        "name": "Olga Pushkar",
        "role": "[bold yellow]Scrum Master[/bold yellow]",
    },
    {
        "name": "Mykhailo Kovalchuk",
        "role": "[bold green]Developer[/bold green]",
    },
    {
        "name": "Gleb Kislovskyi",
        "role": "[bold green]Developer[/bold green]",
    },
]


@input_error
def about(_: AddressBook, arguments: list[str]) -> str:
    """
    Показує інформацію про команду розробників.

    Аргументи:
        None

    Повертає:
        str: Інформація про команду.
    """
    lines = [
        "[bold green]PERSONAL ASSISTANT v1.0[/bold green]",
        "  development by team:\n",
    ]

    for member in TEAM_MEMBERS:
        lines.append(f"  {member['name']}")
        lines.append(f"    Role: {member['role']}")
        lines.append("")

    return "\n".join(lines)
