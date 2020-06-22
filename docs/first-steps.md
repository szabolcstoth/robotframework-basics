# First steps

In order to successfully finish the following exercises, you need to prepare your environment for this learning course.

## Virtual environment

We are going to use `virtualenv` to create a virtual environment for this learning course.

``` bash
mkdir -p robot_course && cd $_
python3 -m pip install virtualenv
python3 -m virtualenv robot_environment
```

!!! info "Installing virtualenv"
    For more information about installing `virtualenv`, please refer to its [official documentation](https://virtualenv.pypa.io/en/latest/installation.html).

Activate your virtual environment.

``` bash
source robot_environment/bin/activate
```

Install Robot Framework inside your virtual environment.

``` bash
pip install robotframework
```

You can leave your virtual environment anytime using the `deactivate` command.

## Basic structure

Create the first Robot Framework related folders and files inside `tests` folder.

``` bash
mkdir -p tests && cd $_
mkdir 01-greetings
touch 01-greetings/01-greetings.robot
```
