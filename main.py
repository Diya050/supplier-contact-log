from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from datetime import date
from typing import Optional

import psycopg2
import psycopg2.extras
import os

load_dotenv()

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection helper
def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))


# Request schema
class ContactCreate(BaseModel):
    supplier_name: str
    contact_name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    last_contacted: Optional[date] = None
    notes: Optional[str] = None


# create a contact log
@app.post("/contacts", status_code=status.HTTP_201_CREATED)
def create_contact(contact: ContactCreate):

    # validation for last_contacted date
    if contact.last_contacted:
        if contact.last_contacted > date.today():
            raise HTTPException(
                status_code=422,
                detail="last_contacted cannot be in the future"
            )

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        cursor.execute(
            """
            INSERT INTO contacts
            (
                supplier_name,
                contact_name,
                phone,
                email,
                last_contacted,
                notes
            )
            VALUES (%s,%s,%s,%s,%s,%s)
            RETURNING *;
            """,
            (
                contact.supplier_name,
                contact.contact_name,
                contact.phone,
                contact.email,
                contact.last_contacted,
                contact.notes
            )
        )

        new_contact = cursor.fetchone()
        conn.commit()
        return new_contact

    finally:
        cursor.close()
        conn.close()


# get all contact logs
@app.get("/contacts", status_code=status.HTTP_200_OK)
def get_contacts():

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        cursor.execute(
            """
            SELECT *
            FROM contacts
            ORDER BY created_at DESC
            """
        )

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


# delete a contact log
@app.delete("/contacts/{id}", status_code=status.HTTP_200_OK)
def delete_contact(id: int):

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        cursor.execute(
            """
            DELETE FROM contacts
            WHERE id = %s
            RETURNING id;
            """,
            (id,)
        )

        deleted = cursor.fetchone()

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Contact not found"
            )

        conn.commit()

        return {
            "message": "Contact deleted successfully"
        }

    finally:
        cursor.close()
        conn.close()