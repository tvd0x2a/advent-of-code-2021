import click
import os.path


@click.command()
@click.option('--f', type=click.File(), default=f'{os.path.splitext(os.path.basename(__file__))[0]}.txt')
def cli(f):
    content = f.read()
    p1: int = None
    increases = 0
    for s in content.splitlines():
        n = int(s)
        if p1 is not None and n > p1:
            increases += 1
        p1 = n
    print(f'part 1: {increases}')

    p2: int = None
    increases2 = 0
    l: str
    rows = [int(l) for l in content.splitlines()]
    for i in range(2, len(rows)):
        n = rows[i] + rows[i-1] + rows[i-2]
        if p2 is not None and n > p2:
            increases2 += 1
        p2 = n
    print(f'part 2: {increases2}')


if __name__ == '__main__':
    cli()
