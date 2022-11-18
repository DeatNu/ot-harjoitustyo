from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/core.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task(coverage_report)
def open_in_browser(ctx):
    ctx.run("firefox htmlcov/index.html")

