# SEIP Lab assignments 
<p>This repository contains lab assignments for proffessor Spinellis' 2024 course "Software Engineering in Practice"</p>

## Assignments

1. AI Ethics: contributed content (module "AI in Media") to guide.md in ai-ethics repo 
2. [CI/CD Tools: created CRUD app "SkillSync"](#skillsync)
3. [Security-Part1: basic cryptography operations](#crypto)
4. [Security-Part2: fuzzing](#fuzzing)

### SkillSync 
- **Directory structure**
```
skillsync
    └─── src───main
         │      ├───python
         │      │   └───source code files
         │      └───scripts
         │   
         └───unittest
            ├───python
            └───test files
        
```

- **Build automation tool**
<p>Used pybuild to automate the building and testing process. Challenges I tackled in this step included setting up a venv for my python project, setting PYTHONPATH, specifying import absolute paths and overriding plugin's coverage restrictions for building the app. </p>

- **Docker Implementation**
<p>Created a docker image "skillsync" with in which the app builds and runs by creating a container which is then removed after exiting (docker run -it --rm skillsync)</p>

- **PGP Cryptography**
<p>This is my public key fingerprint: FAF5 AE4D 6CE5 4580 C828  9513 9C09 A14C 1FFA EAD2
</p>

- **Fuzzing exercises**
<p>More info here [fuzzing.md](fuzzing.md)</p>
