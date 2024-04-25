import argparse
import sys
import src.main.python.models
from src.main.python.constants import VALID_COMMANDS

def main():
    print("Welcome to SkillSync! Here is a list of commands you can use the app: ")
    for command in VALID_COMMANDS:
        print(f" - {command}")
    print("For more instructions run with --help")

    parser = argparse.ArgumentParser(
        description='Help for SkillSync, a Python CRUD application to manage your coding skills'
    )

    parser.add_argument('- create_list', help='Create a skills lists for your goals/achievements', action='store_true')
    parser.add_argument('- delete_list', help='Delete a skills list by id', action='store_true')
    parser.add_argument('- show_goals', help='List all goals', action='store_true')
    parser.add_argument('- show_achievements', help='List all achievements', action='store_true')
    parser.add_argument('- create_skill', help='Add a skill to one of your lists', action='store_true')
    parser.add_argument('- delete_skill', help='Delete a skill from one of your lists', action='store_true')
    parser.add_argument('- update_skill', help='Update a skill', action='store_true')
    parser.add_argument('- quit', help='Close the app', action='store_true')
    
    args = parser.parse_args()

    def add_skill():
        skill_name= input("Enter a name for your new skill: ")
        skill_type= input("What is this skill useful for? (e.g. web development, db management, algorithms & data structures): ")
        profficiency_level= input("What is your profficiency in this skill? (very low / low / medium / high/ very high): ").strip().lower()
        s= models.create_skill(skill_name,skill_type,profficiency_level)
        print(f"Created skill {skill_name}!")
        return s

    command = input("What would you like to do? ")
    while command not in VALID_COMMANDS:
        command = input("Please enter a valid command. For help run python skillsync --help")
    if command == "quit":
        print("See you soon!")
        sys.exit(0)
    while command != "quit":
        if command == "create_list":
            list_type= None
            while list_type not in ['A','G']:
                list_type= input("Do you want to create a list for your goals or achievements? (Type A or G) ").strip().upper()
                if list_type not in ['A','G']:
                    print("Please enter a valid value for the list type!")
                    
            list_name= input("Give a name to your list: ")
            author= input("Enter your name: ")
            
            if list_type == 'A':
                l_type= 'achievement'
                date_goal= None
            elif list_type == 'G':
                l_type= 'goal'
                date_goal= input("Enter the date until when you want to achieve your goal: ")
            skills_list= models.create_skills_list(list_name,l_type,author,date_goal)
            print(f"Creating skills list {list_name} containing {author} 's {l_type} ")
        
        elif command == "delete_list":
            print("Your lists: ")
            models.show_goals()
            models.show_achievements()
            list_id= input("Enter the id of the list you want to delete: ")
            models.delete_skills_list(list_id)
            
        elif command == "show_goals":
            models.show_goals()
        elif command == "show_achievements":
            models.show_achievements()            
        elif command == "create_skill":
            skill= add_skill()
            print("Your lists: ")
            models.show_goals()
            models.show_achievements()
            list_id= input("Enter the list's id you want to add a skill to: ")
            models.add_skill_to_list(list_id,skill)
            print("Skill {skill.name} added successfully!")
        elif command == "delete_skill":
            list_id= input("Enter the list's id you want to delete a skill from: ")
            skill_name= input(f"Enter the skill name you want to delete from {list_id}: ")
            models.delete_skill_from_list(list_id, skill_name) 
            print(f"Skill {skill_name} deleted successfully!") 
        elif command == "update_skill":
            skill_name= input(f"Enter the name of the skill you want to update: ")
            models.update_skill_in_list(list_id, skill_name, add_skill)
            
        command = input("What would you like to do next? ")
        while command not in VALID_COMMANDS:
            command = input("Please enter a valid command. For help run python skillsync --help")   


if __name__ == "__main__":
    main()