from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import AdminUser
from app.security.passwords import hash_password, verify_password
from app.security.jwt import create_access_token
from app.schemas.user import Token, AdminUserResponse
from app.core.config import settings


class AuthService:

    @staticmethod
    def authenticate_admin(db: Session, username: str, password: str) -> AdminUser:
        user = db.query(AdminUser).filter(AdminUser.username == username).first()
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect administrative username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Administrative user account is inactive"
            )

        # Update last login
        user.last_login = datetime.utcnow()
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def create_login_token(user: AdminUser) -> Token:
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        token_jwt = create_access_token(
            data={"sub": user.username, "role": user.role, "id": user.id},
            expires_delta=access_token_expires
        )
        return Token(
            access_token=token_jwt,
            token_type="bearer",
            user=AdminUserResponse.model_validate(user)
        )

    @staticmethod
    def ensure_default_admin(db: Session) -> AdminUser:
        """Create default administrative user if one does not already exist."""
        admin = db.query(AdminUser).filter(AdminUser.username == settings.DEFAULT_ADMIN_USERNAME).first()
        if not admin:
            admin = AdminUser(
                username=settings.DEFAULT_ADMIN_USERNAME,
                email=settings.DEFAULT_ADMIN_EMAIL,
                hashed_password=hash_password(settings.DEFAULT_ADMIN_PASSWORD),
                role="administrator",
                is_active=True
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
        return admin
