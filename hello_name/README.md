## README file
This is my first python file to learn docker and containers. I kept it very simple with minimal set of instructions.


`hello_name.py` file is a very simple python file.<br>
It takes your name as an input and print out a Hello statement with your name. I have used ```try-except``` to handle the exception.

The content of the DockerFile is as follows. 
- The **FROM** field have information on what image is to be used. 
- The **WORKDIR** command sets the working directory. 
- The **COPY** instruction is to add/copy a file to a folder location.

This step is important to containerzie the application. When the container is created, this file will run from inside the container and if there is no file, then an error will pop up when the container is run.
Error: python: can't open file: No such file or directory.

So it is important to make sure the contents are copied from the existing directory to the directory created inside the container.
- Lastly, we used the **CMD** instruction to make the container executable and to ensure that it stays alive and running.