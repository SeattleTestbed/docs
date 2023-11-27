# `auto_grader.py`
> **Automated Grading for Repy V2 Assignments**

`auto_grader.py` is a Python-based tool designed to streamline the grading
process for defense and attack programs written in [Repy
V2](https://github.com/SeattleTestbed/repy_v2). By automatically running each
attack against every defense, it produces comprehensive results in a CSV format.

## Description
With `auto_grader.py`, instructors can effortlessly assess the efficacy of
students' defense mechanisms in the face of potential attacks. For every attack
that succeeds in compromising a defense, the resulting CSV will register a `1`;
otherwise, it will display a `0`. An attack is considered successful if it
generates an output or raises an error, denoting the failure of the defense
layer. It also handles timeouts, ensuring that the script does not hang in the
event of an infinite loop.

## Prerequisites
- Python 2.7 installed on your machine.
- Repy V2 environment setup.
- Copy the required files (mentioned below) in the script's directory
   - `repy.py`
   - `restrictions.default`
   - `wrapper.r2py`
   - `encasementlib.r2py`

## Usage
```bash
python auto_grader.py defense_folder_path attack_folder_path temp_target_folder_path
```
where:
- `defense_folder_path` is the path to the folder containing defense programs.
- `attack_folder_path` is the path to the folder containing attack programs.
- `temp_target_folder_path` is the path to the temporary target folder.

## Naming Conventions
- Attack programs should be named as: "`[studentid]_attackcase[number].r2py`".
- Defense programs should start with the name
  "`reference_monitor_[studentid].r2py`".

For example, if the student id is `abc123`, the defense program should be named
as `reference_monitor_abc123.r2py` and the attack program should be named as
`abc123_attackcase1.r2py`, `abc123_attackcase2.r2py`, etc.

## Output
Two CSV files are generated:
1. `All_Attacks_matrix.csv`: Contains the result of every attack program against
   each defense.
2. `All_Students_matrix.csv`: Indicates which students successfully attacked a
   defense.

## Notes
- Students are instructed to generate output or raise an error in their attack
  program only when they successfully compromise the security layer.
- Ensure the correct environment, naming conventions, and directory structures
  are adhered to for successful script execution.

## Contributing
For modifications, improvements, or any issues, please open a pull request or
issue.

## Credits
`auto_grader.py` is the brainchild of
[@Hooshangi](https://github.com/Hooshangi).

For further details, potential contributions, or to view the code, visit
[Hooshangi/Grading-script](https://github.com/Hooshangi/Grading-script).
