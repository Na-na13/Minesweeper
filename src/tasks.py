from invoke import task

@task
def start(ctx):
    ctx.run("python3 ui.py")