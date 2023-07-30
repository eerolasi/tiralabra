from invoke import task

@task
def run(c):
    c.run("python3 src/main.py", pty=True)

@task
def test(c):
    c.run("pytest src/tests")

@task
def coverage(c):
    c.run("coverage run --branch -m pytest src/tests")
    c.run("coverage report -m")
    c.run("coverage html")

@task
def lint(c):
    c.run("pylint src")

@task
def format(c):
    c.run("autopep8 --in-place --recursive src")
    
    