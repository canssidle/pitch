## Project name
PITCH

### Description
This web-app allows the user to submit their pitches,have them voted and commented upon.

### Author
Canssidle Wairimu

The user can:

> sign in to the application
> The user can create the pitch
> The user can comment on other pitches


### Setup/Installation Requirements
Prerequisites
python3.6
pip
Virtual environment(virtualenv)



### Creating the virtual environment

   $ python3.6 -m venv --without-pip virtual
   $ source virtual/bin/env
   $ curl https://bootstrap.pypa.io/get-pip.py | python

### Installing Flask and other Modules

   $ python3.6 -m pip install Flask
   $ python3.6 -m pip install Flask-Bootstrap
   $ python3.6 -m pip install Flask-Script


### Run the application:

   $ chmod a+x start.sh
   $ ./start.sh

### Testing the Application
> Didn't create the tests


### Technologies Used
>Visual Studio was the source code editor of choice.
>Git and Github were used as my local and online repositories respectively.
>Flask was used as the micro-framework
>Heroku was used in deploying the live site

### Behaviour driven development/ Specifications
|---------------------------------------------|-------------------------------------|---------------------------------------------------
|Behaviour                                    |  Sample Input                       |Sample Output
|---------------------------------------------|-------------------------------------|---------------------------------------------------
|DIsplay the home page and sign in            |Enters their necessary credentials   |One can update thier profile
|Display a section for pitching their projects|Submits the project                  |outputs their project
|Display the comment section                  |One comments on the project          |outputs the comments

### Contact details
Contact me through my email: canssidlewairimu@gmail.com
### License
MIT License Copyright (c) {2019} Canssidle 



