import nox

nox.options.default_venv_backend = "uv|virtualenv"

@nox.session(
    python=["3.7", "3.8", "3.9", "3.10", "3.11", "3.12", "3.13"]
)
def test(session):
    session.install(".")
    session.run("pytest", "tests/")
