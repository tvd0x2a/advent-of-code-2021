import click
import os.path


@click.command()
@click.option('--f', type=click.File(), default=f'{os.path.splitext(os.path.basename(__file__))[0]}.txt')
def cli(f):
    content = f.read()
    part1(content)
    part2(content)


def part1(content: str):
    x = 0
    y = 0
    for command in content.splitlines():
        direction, val_s = command.split(' ')
        val = int(val_s)
        match direction:
            case 'forward':
                x += val
            case 'up':
                y -= val
            case 'down':
                y += val
    p1 = x * y
    print(f'part 1: {p1}')


def part2(content: str):
    x = 0
    y = 0
    aim = 0
    for command in content.splitlines():
        direction, val_s = command.split(' ')
        val = int(val_s)
        match direction:
            case 'forward':
                x += val
                y += aim * val
            case 'up':
                aim -= val
            case 'down':
                aim += val
    result = x * y
    print(f'part 2: {result}')


if __name__ == '__main__':
    cli()
