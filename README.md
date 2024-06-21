# Bangazon Platform API

## System Dependencies

1. Follow installation guide for installing [pipx](https://pipx.pypa.io/stable/installation/).
2. Run `pipx install poetry`.
3. Run the command below for your operating system.

### Mac OS

```sh
brew install libtiff libjpeg webp little-cms2
```

### Linux

```sh
sudo apt install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev
```

## Setup

1. Clone this repository and change to the directory in the terminal.
2. Run `poetry install`
3. Run `poetry shell`
4. Run `pip install setuptools`
5. Run migrations and install starter data with the `./seed_data.sh` script.
6. Open the project in VS Code if you haven't yet.
7. Ensure that the correct Python Interpreter is chosen in VS Code.
8. Start your debugger.

## Postman Request Collection

1. Open Postman
1. Click File > Import from the navbar
1. Either click and drag the `Bangazon Python API.postman_collection.json` file or choose it by clicking the **files** link in the window.
1. Your should be prompted to import **Bangazon Python API**.
1. Click the Import button to complete the process.

To test it out...

1. Click on the Collections icon on the left
2. Expand the Profile sub-collection
3. Double-click on Login and send the request.

You should get a response back that looks like this.

```json
{
    "valid": true,
    "token": "9ba45f09651c5b0c404f37a2d2572c026c146690",
    "id": 5
}
```

## User Authentication

Look in the `users.json` file for the usernames. Every password is _Admin8*_.

## Changing Your Database

You can run the `./seed-data.sh` script any time to make changes to database models, or just want to roll back your data to its original state. It deletes the database, any existing migrations, and then re-creates the database based on your current models, and inserts starter data.
