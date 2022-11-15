# CMPE Lab 2

## Installation

- First of all, we are running our program on Ubuntu and using Python3.8
```shell
sudo apt update
sudo apt-get upgrade
sudo apt-get update
sudo apt-get install python3.8 python3.8-dev python3.8-distutils python3.8-venv
```

- Install the requirements
```shell
sudo python3.8 -m pip install requirements.txt
```

## Usage

- We use `Invoke` to manage the compiling and testing, you can use command below to see the task list
```shell
invoke --list
# or
inv --list
```

- Run the build or test.

```shell
invoke all
```

- After testing, you can remove all the build file.
```shell
invoke clean
```