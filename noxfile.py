import nox


@nox.session(reuse_venv=True)
def lint(session: nox.Session) -> None:
    session.install("ruff")
    session.run("ruff", "check", "--diff", "tests")
    session.run("ruff", "format", "--diff", "tests")
