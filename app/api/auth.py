from datetime import timedelta
from typing import Annotated

from datetime import timedelta
from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlmodel.ext.asyncio.session import AsyncSession
from jose import jwt, JWTError

from app.db.session import get_session
from app.models.user import User, UserCreate, UserLogin, Token
from app.crud import user_crud
from app.core.security import verify_password, get_password_hash, create_access_token
from app.core.settings import settings

router = APIRouter()

async def get_current_user(request: Request, session: AsyncSession = Depends(get_session)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    session_cookie = request.cookies.get("session")
    if not session_cookie:
        raise credentials_exception
    try:
        payload = jwt.decode(session_cookie, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await user_crud.get_user_by_email(session, email=email)
    if user is None:
        raise credentials_exception
    return user

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
async def register_user(user_create: UserCreate, response: Response, session: AsyncSession = Depends(get_session)):
    """
    Registers a new user, hashes the password, and returns a JWT token.
    The token is also set as an HTTP-only, secure cookie.
    """
    db_user = await user_crud.get_user_by_email(session, email=user_create.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = await user_crud.create_user(session, user_create)

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    response.set_cookie(
        key="session",
        value=access_token,
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # in seconds
        samesite="lax",
        path="/"
    )
    return {"access_token": access_token, "token_type": "bearer", "message": "User registered successfully"}

@router.post("/login", response_model=Token)
async def login_for_access_token(user_login: UserLogin, response: Response, session: AsyncSession = Depends(get_session)):
    """
    Authenticates a user and returns a JWT token.
    The token is also set as an HTTP-only, secure cookie.
    """
    user = await user_crud.get_user_by_email(session, email=user_login.email)
    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    response.set_cookie(
        key="session",
        value=access_token,
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # in seconds
        samesite="lax",
        path="/"
    )
    return {"access_token": access_token, "token_type": "bearer", "message": "Login successful"}

@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    """
    An example protected endpoint that requires authentication.
    """
    return {"message": f"Welcome, {current_user.email}! You have access to protected data."}
