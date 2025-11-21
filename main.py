from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def root():
    return {"message": "maachudale"}
users=[]
@app.post("/users/")
def create_user(user: dict):
    users.append(user)
    return user

@app.get("/users/")
def get_users():
    return users