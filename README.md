# Threaded console command

With this package you can run your console commands in threads.  This process can be used to run a command multiple times.

## Usage as executable
```
# tcommand <count threads> <command ...>
# example:

tcommand 2 ls -la
```

## Usage as package
```
import ThreadedCommand as tc

tc.run(['ls', '-la'], 2)
```

**Output:**
```
Enter ctrl+c to stop...
Command:  ['ls']
Status: 2/2 active threads
```