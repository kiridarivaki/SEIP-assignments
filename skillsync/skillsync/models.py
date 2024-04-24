import math
from constants import PROF_LEVEL_VALUES 

# Dictionaries to store goals and achievements with unique IDs as keys
goals = []
achievements = []
id_counter = 1 

# Function to create skills lists (goals or achievements)
def create_skills_list(name, list_type, author, date_goal):
    global id_counter  
    if list_type not in ['goal', 'achievement']:
        raise ValueError(f"List type '{list_type}' is not valid")

    new_list = {    #each "list" the user creates is in fact a dictionary 
        'id': id_counter,
        'name': name,
        'list_type': list_type,
        'author': author,
        'skills' : []
    }

    if list_type == 'goal':
        new_list['date_goal']= date_goal
        goals.append(new_list)
    elif list_type == 'achievement':
        achievements.append(new_list)

    id_counter += 1 
    return new_list


# Function to retrieve a list by ID from goals or achievements
def get_list_by_id(id):
    found= False
    for l in goals:
        if l["id"]== id:
            found = True
            return l
    for l in achievements:
        if l["id"]== id:
            found = True
            return l 
    
    if not found :
        raise ValueError(f"Skills list with id '{id}' does not exist")


# Function to delete a skills list by ID
def delete_skills_list(id):
    try:
        l= get_list_by_id(id)
        if l in goals:
            del goals[l]
        elif l in achievements:
            del achievements[l]
    except Exception as e:
        raise ValueError(f"Skills list with id '{id}' does not exist")

def show_goals():
    print("Goals: ")
    for skills_list in goals:
            print(f' List {skills_list["id"]}:')
            for key, value in skills_list.items():
                print(f" {key}: {value}")

def show_achievements(): 
    print("Achievements: ")
    for skills_list in achievements:
            print(f' List {skills_list["id"]}:')
            for key, value in skills_list.items():
                print(f" {key}: {value}")
        


# Functions to create and manage skills
def create_skill(name, skill_type, profficiency_level):
    if profficiency_level not in PROF_LEVEL_VALUES:
        raise ValueError(f"{profficiency_level} is not a valid profficiency level")
    else:
        skill = {
            'name': name,
            'skill_type': skill_type,
            'profficiency_level': profficiency_level
        }
    return skill


def add_skill_to_list(list_id, skill):
    skills_list = get_list_by_id(list_id)
    skills_list['skills'].append(skill)


def get_skill_from_list(list_id, skill_name):
    skills_list = get_list_by_id(list_id)
    if 'skills' not in skills_list:
        raise ValueError(f"Skills list with id '{list_id}' has no skills")

    for skill in skills_list['skills']:
        if skill['name'] == skill_name:
            return skill

    raise ValueError(f"Skill '{skill_name}' not found in list with id '{list_id}'")


def delete_skill_from_list(list_id, skill_name):
    skills_list = get_list_by_id(list_id)
    if 'skills' not in skills_list:
        raise ValueError(f"Skills list with id '{list_id}' has no skills")

    for skill in skills_list['skills']:
        if skill['name'] == skill_name:
            skills_list['skills'].remove(skill)
            return

    raise ValueError(f"Skill '{skill_name}' not found in list with id '{list_id}'")

#function to update skill in all lists
def update_skill_in_list(skill_name, new_skill):
    for l in goals:
        for skill in l:
            if skill.name == skill_name:
                delete_skill_from_list(l.list_id, skill_name)  
                add_skill_to_list(l.list_id, new_skill) 
    for l in achievements:
        for skill in l:
            if skill.name == skill_name:
                delete_skill_from_list(l.list_id, skill_name)  
                add_skill_to_list(l.list_id, new_skill) 
            
    
