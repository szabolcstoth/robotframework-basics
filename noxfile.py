import nox


@nox.session(reuse_venv=True)
def lint(session: nox.Session) -> None:
    session.install("robotframework-robocop", "ruff")
    session.run("ruff", "check", "tests")
    session.run("ruff", "format", "--diff", "tests")
    session.run(
        "robocop",
        "format",
        "--diff",
        "--check",
        "--no-cache",
        "--config",
        "pyproject.toml",
        "tests",
    )
    session.run(
        "robocop",
        "check",
        "--no-cache",
        "--config",
        "pyproject.toml",
        "tests",
    )
