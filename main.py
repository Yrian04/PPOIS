from src.view.terminal import Terminal
from src.view.consoleInputer import ConsoleInputer
from src.DAO.fileRepository import FileRepository
from src.controller.interpreter import Interpreter
from src.controller.commands.listCommand import ListCommand
from src.controller.commands.addCommand import AddCommand
from src.controller.commands.removeCommand import RemoveCommand
from src.controller.commands.publishLawCommand import PublishLawCommand
from src.controller.commands.collectTaxesCommand import CollectTaxesCommand
from src.controller.commands.provideSecurityCommand import ProvideSecurityCommand
from src.controller.commands.provideSocialSupportCommand import ProvideSocialSupportCommand
from src.controller.commands.enhanceInfrastructureCommand import EnhanceInfrastructureCommand
from src.controller.commands.exitCommand import ExitCommand
from src.controller.commands.helpCommand import HelpCommand

commands = {
    ListCommand.name: ListCommand,
    AddCommand.name: AddCommand,
    RemoveCommand.name: RemoveCommand,
    PublishLawCommand.name: PublishLawCommand,
    CollectTaxesCommand.name: CollectTaxesCommand,
    ProvideSecurityCommand.name: ProvideSecurityCommand,
    ProvideSocialSupportCommand.name: ProvideSocialSupportCommand,
    EnhanceInfrastructureCommand.name: EnhanceInfrastructureCommand,
    ExitCommand.name: ExitCommand,
    HelpCommand.name: HelpCommand,
}

terminal = Terminal(
    ConsoleInputer(),
    Interpreter(commands),
    FileRepository("file.txt")
)

while True:
    try:
        print(terminal.work())
    except Exception as e:
        print(e)
