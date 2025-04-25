# First steps

You will need to prepare your environment for this tutorial in order to successfully complete the following learning course.

## Virtual environment

!!! note "Skip installing `virtualenv`"
    You can skip using `virtualenv` if you don't want to use an isolated Python environment, or if you already have one.

We will use `virtualenv` to create a virtual environment for this learning course.

``` bash
mkdir -p robot_course && cd $_
python3 -m pip install virtualenv
python3 -m virtualenv robot_environment
```

!!! info "Installing `virtualenv`"
    To learn more about how to install `virtualenv`, please refer to its [official documentation](https://virtualenv.pypa.io/en/latest/installation.html).

Activate your virtual environment.

``` bash
source robot_environment/bin/activate
```

Install Robot Framework in your virtual environment.

``` bash
pip install robotframework
```

You can leave your virtual environment at any time using the `deactivate` command.

## Basic structure

Create the first Robot Framework related folders and files In the `tests` folder,.

``` bash
mkdir -p tests && cd $_
mkdir 01-greetings
touch 01-greetings/01-greetings.robot
```
