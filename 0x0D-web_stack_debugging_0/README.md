# 0x0D Web stack debugging #0 :wrench:

> Debugging is the process of finding and fixing errors in software that prevents it from running correctly. As you become a more advanced programmer and an industry engineer, you will learn how to use debugging tools such as gdb or built-in tools that IDEs have. However, it’s important to understand the concepts and processes of debugging manually. This project covers the optimal framework and blueprint for debugging web stack (remote containers this scenario) bugs

Challenge:

Get Apache to run on the container and to return a page containing Hello Holberton when querying the root of it. After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains Hello Holberton. Paste the command(s) you used to fix the issue in your answer file.
Here we can see that after starting my Docker container, I curl the port 8080 mapped to the Docker container port 80, it does not return a page but an error message. Note that you might also get the error message curl: (52) Empty reply from server.


## Tasks :heavy_check_mark:

0. Bash script that once executed, will bring the webstack to a working state.