import click
import sys

@click.group()
@click.version_option('1.0.0', prog_name='cpy')
def cli():
    """Custom CLI Tool"""
    pass

# Comando de exemplo (substitua pelos seus comandos)
@cli.command()
def go():
    """Inicia o CYP"""
    click.echo("CYP iniciado!")

# Adicione outros comandos aqui seguindo o mesmo padrão

if __name__ == '__main__':
    # Esta linha garante compatibilidade com o comportamento original
    if len(sys.argv) == 1:
        cli.main(['--help'])
    else:
        cli()