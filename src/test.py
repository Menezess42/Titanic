import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    import matplotlib.pyplot as plt
    return (plt,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
