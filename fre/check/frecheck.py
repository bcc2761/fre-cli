import click
from .frecheckexample import check_test_function

@click.group(help=" - access fre check subcommands")
def checkCli():
    pass

@checkCli.command()
@click.option('--uppercase', '-u', is_flag=True, help = 'Print statement in uppercase.')
@click.pass_context
def function(context, uppercase):
    """ - Execute fre check test """
    context.forward(check_test_function)

if __name__ == "__main__":
    checkCli()
