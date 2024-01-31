import os
import sys
import yaml
import json

path = os.path.join(os.path.dirname(sys.argv[0]))+"/dockerPractics/build"
resume_file = path+"/resume.yaml"

def parseYAML():
    with open(resume_file, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
    
def convertToJSON():
    with open(path+"/resume.json", "w", encoding="utf-8") as jsonOut:
        json.dump(parseYAML(), jsonOut, indent=4, ensure_ascii=False)

def get_skills_with_level(level):
    data = parseYAML()
    skills = [skill["name"] for skill in data["skills"] if skill["level"] == level]
    return skills

def get_education_in_progress():
    data = parseYAML()
    education = [edu["institution"] for edu in data["education"] if edu["status"] == "in progress"]
    return education

print("Навыки с уровнем владения 'medium':")
for skill in get_skills_with_level("medium"):
    print("    "+skill)

print("Программы, на которых проходит обучение в данный момент:")
for degree in get_education_in_progress():
    print("    "+degree)