from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2PasswordBearer
# from typing import Annotated

from routes.detenido import router as detenido_router
from routes.remision import router as remision_router

app = FastAPI()
app.include_router(detenido_router)
app.include_router(remision_router)

# from depends.auth import User,get_current_active_user, fake_users_db,UserInDB,fake_hash_password,HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#
#     return {"access_token": user.username, "token_type": "bearer"}
# @app.get("/users/me")
# async def read_users_me(
#     current_user: Annotated[User, Depends(get_current_active_user)],
# ):
#     return current_user