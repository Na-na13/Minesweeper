from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/ui.py")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def test(ctx):
    ctx.run("python3 src/tester.py")
