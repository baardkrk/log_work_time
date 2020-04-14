# Log Work Time
A simple cli for logging work-time on different projects. Stores the work-log as a json-file with 
optional descriptions of each entry. The json-file is organized as a map with the project names
as keys, and the values will be a list of log-entries related to that project.

The program runs in a shell, and blocks that shell thread while it is running. When enter is
pressed to interrupt the program, the timer is stopped, the hours worked is calculated, and the 
user is prompted to provide an optional description of the work-session

### Usage
```
$ python3 log_work_time.py <PROJECT NAME> [ENTER]
$ ... [ENTER]
Enter a description for this entry:
> This is my entered description [ENTER]
Enter a rating (out of 5) for this session:
> 3.6 [ENTER]
```
The program will give the session a rating based on how many pauses you took while working on it,
and how you felt about the session afterwards.

It is recommended to provide an alias for the program in your shell. (unless you compile it to an
executable)  
Example:
```
alias lwt='python3 <HOME_PATH>/log_work_time/log_work_time.py'
```

### Output
Example json output:
```json
{
  "my_project_name": [
    {
      "date": "2020-01-22",
      "hours_worked": 4.78,
      "pauses": 3,
      "description": "Did work on the project. Good day today!",
      "rating": 4.7
    },
    {
      "date": "2020-02-20",
      "hours_worked": 5.20,
      "pauses": 23,
      "description": "Worked more on the project. Today was not a good day...",
      "rating": 1.2
    }
  ],
  "another_project": [
    {...},{...},{...}
  ],
  "next_project_name": [...]
}
```

### TODO
- [x] implement timer
- [x] read user input
- [x] 'pause' functionality
- [ ] summary of session
- [ ] better calculation of effectiveness (ex -10 min for not taking a break per 60 minutes)
- [ ] session filename, provide file-name as optional parameter
- [ ] write to file
- [ ] read from file
- [ ] create binary executable
- [ ] add rating functionality
