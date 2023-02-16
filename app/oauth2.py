from jose import JWTError, jwt
from . import schemas
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

ouath2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# create a token based on phone number as a user_id and expiration duration
def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# extract token and check it's credentials validation
def verify_access_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        phone: str = payload.get('user_id')
        if not phone:
            raise credentials_exception
        token_data = schemas.TokenData(phone=phone)
    except JWTError:
        raise credentials_exception
    return token_data

# in any path operation takes the token of requests as a dependency and
# send it to verify_access_token
def get_current_user(token:str=Depends(ouath2_scheme)):
    credential_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials!', headers={'WWW.Authenticate:': "Bearer"})
    return verify_access_token(token, credential_exception)
