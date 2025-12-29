
import json

user ={
    'name':'chuukwudi',
    'role':'ai engineer',
    'skills':['python','fastapi','agents']
}
def greeting(name: str) -> str:
    return f"Hello, {name}!"


def print_user_info(user:dict):
    info = f"Name: {user['name']}\nRole: {user['role']}\nSkills: {', '.join(user['skills'])}"
    print(info)

if __name__ == "__main__":
        print_user_info(user)