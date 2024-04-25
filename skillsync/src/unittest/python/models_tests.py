import pytest
import src.main.python.main 
from src.main.python.constants import PROF_LEVEL_VALUES

# Test to create a skills list and retrieve it
def test_create_and_retrieve_skills_list():
    # Create a skills list
    skills_list = create_skills_list("My Goal", "goal", "Author", "2024-12-31")

    # Retrieve the skills list by ID
    retrieved_list = get_list_by_id(skills_list["id"])

    assert retrieved_list == skills_list

# Test to ensure ValueError is raised with an invalid list type
def test_invalid_skills_list_type():
    with pytest.raises(ValueError):
        create_skills_list("Invalid List", "invalid_type", "Author", "2024-12-31")

# Test to delete a skills list and verify it's removed
def test_delete_skills_list():
    # Create a skills list
    skills_list = create_skills_list("My Goal", "goal", "Author", "2024-12-31")

    # Delete the skills list
    delete_skills_list(skills_list["id"])

    # Verify that it raises an error when trying to retrieve the deleted list
    with pytest.raises(ValueError):
        get_list_by_id(skills_list["id"])

# Test to create a skill and add it to a list
def test_add_and_get_skill():
    # Create a skills list
    skills_list = create_skills_list("My Goal", "goal", "Author", "2024-12-31")

    # Create a skill
    skill = create_skill("Python", "Programming", PROF_LEVEL_VALUES[0])

    # Add the skill to the list
    add_skill_to_list(skills_list["id"], skill)

    # Retrieve the skill from the list
    retrieved_skill = get_skill_from_list(skills_list["id"], "Python")

    assert retrieved_skill == skill

# Test to delete a skill from a list
def test_delete_skill_from_list():
    # Create a skills list and add a skill
    skills_list = create_skills_list("My Goal", "goal", "Author", "2024-12-31")
    skill = create_skill("Python", "Programming", PROF_LEVEL_VALUES[0])
    add_skill_to_list(skills_list["id"], skill)

    # Delete the skill from the list
    delete_skill_from_list(skills_list["id"], "Python")

    # Verify the skill is gone
    with pytest.raises(ValueError):
        get_skill_from_list(skills_list["id"], "Python")

# Test to update a skill in a list
def test_update_skill():
    # Create a skills list and add a skill
    skills_list = create_skills_list("My Goal", "goal", "Author", "2024-12-31")
    skill = create_skill("Python", "Programming", PROF_LEVEL_VALUES[0])
    add_skill_to_list(skills_list["id"], skill)

    # Create a new skill to update
    new_skill = create_skill("Python3", "Programming", PROF_LEVEL_VALUES[1])

    # Update the skill in the list
    update_skill_in_list("Python", new_skill)

    # Retrieve the updated skill from the list
    updated_skill = get_skill_from_list(skills_list["id"], "Python3")

    assert updated_skill == new_skill
