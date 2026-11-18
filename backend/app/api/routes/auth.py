from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.services.auth_service import AuthService
from app.security.deps import get_current_admin
from app.schemas.user import Token, LoginRequest, AdminUserResponse
from app.models.user import AdminUser

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Authenticate administrator credentials and receive a secure JWT access token.
    """
    user = AuthService.authenticate_admin(db, request.username, request.password)
    return AuthService.create_login_token(user)


@router.post("/logout")
def logout(current_user: AdminUser = Depends(get_current_admin)):
    """
    Client-side token disposal endpoint.
    """
    return {"message": "Successfully logged out", "status": "ok"}


@router.get("/me", response_model=AdminUserResponse)
def get_current_user_profile(current_user: AdminUser = Depends(get_current_admin)):
    """
    Retrieve profile details for currently authenticated administrator.
    """
    return current_user
