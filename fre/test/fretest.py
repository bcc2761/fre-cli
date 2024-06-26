import click
from .fretestexample import test_test_function

@click.group(help=click.style(" - access fre test subcommands", fg=(92,164,29)))
def testCli():
    pass

@testCli.command()
@click.option('--uppercase', '-u', is_flag=True, help = 'Print statement in uppercase.')
@click.pass_context
def function(context, uppercase):
    """ - Execute fre test test """
    context.forward(test_test_function)

if __name__ == "__main__":
    testCli()
