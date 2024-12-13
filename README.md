# Note Manager API Application

Using this application you can **create**, **update** and **delete** tasks. Afterwards you can display them and keep track of the things you have to do. :D

Each task has an **ID**, the **text**(note) and a **status**, which tells you if the task is **todo/done/in-progress**.

## Features
- Add new tasks.
- Update task notes.
- Delete tasks.
- Mark tasks with statuses.
- List tasks based on their status.

## Prerequisites
- **Python 3.6+**

## Setup

1. Clone the repository:
```
git clone https://github.com/dayzyy/API-NotesApp.git
```
2. Navigate to the created directory:
```
cd API-NotesApp/
```
3. Create a virtual environment:
```
python -m venv .env
```
4. Activate it:
```
source .env/bin/activate
```
5. Install all the dependecies:
```
pip install -r requirements.txt
```
6. Navigate to the api directory and run the server:

```
cd api/
python main.py
```

Now open another terminal and navigate to the project's root directory. Here you can run the commands listed below to use the application.

You can also run the following commands to see all the available commands:
```python
# Authentication related
python auth.py -h

# Note related
python notes.py -h
```

## Commands

### Authentication
```python
# To register
python auth.py register <username> <password> # Both must be at least 5 characters long. Username has to be unique

# Example
python auth.py register lukka luka123


# To log in
python auth.py login <username> <password>

# Example
python auth.py login lukka luka123


# To see if you are logged in
python auth.py status


# To log out
python auth.py logout
```

### Notes
```python
# To add a note
python notes.py add <note>

# Example
python notes.py add "Wash the dishes"


# To update a note
python notes.py update <id> <note>

# Example
python notes.py update 1 "Wash the dishes and mop the floor"


# To delete a note
python notes.py delete <id>

# Example
python notes.py delete 1


# To mark a note as in -- todo/done/in-progress.
python notes.py mark <id> <status>

# Examples
python notes.py mark 1 todo
python notes.py mark 1 done
python notes.py mark 1 in-progress


# To list the notes with provied status
python notes.py list <status>

# If you leave the status arguement empty like in the first example below, it will list all the notes no matter their status

# Examples
python notes.py list
python notes.py list todo
python notes.py list done
python notes.py list in-progress
```

### Inspired By
**roadmap.sh** https://roadmap.sh/projects/todo-list-api
