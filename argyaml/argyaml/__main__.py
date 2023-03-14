from argyaml import BaseHandler


def run(command: str | None = None) -> None:
    """
    Run argyaml cli tool
    """
    import os
    from sys import argv
    BaseHandler(
        args=[command] + argv[1:] if command else None,
        config_path=os.path.join(os.path.dirname(__file__), 'cli-config.yaml'),
        handlers_dir='argyaml.handlers').run()


def init():
    raise NotImplementedError('Init script is not implemented')
    run('init')


def generate():
    run('generate')


if __name__ == '__main__':
    run()
