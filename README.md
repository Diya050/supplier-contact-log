# Supplier Contact Log Tracker

A lightweight supplier contact tracking system built with:

* FastAPI (Python backend)
* PostgreSQL (database)
* HTML/CSS/JavaScript (frontend)



# 1. Clone Repository

```bash
git clone https://github.com/Diya050/supplier-contact-log.git
cd supplier-contact-log
```



# 2. Create & Activate Virtual Environment

### Create environment

```bash
py -3.11 -m venv venv
```

### Activate

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
./venv/Scripts/activate
```

You should see:

```bash
(venv)
```



# 3. Install Dependencies

```bash
pip install -r requirements.txt
```



# 4. Database Setup (PostgreSQL)

### Verify installation

```bash
psql --version
```

If not found, install PostgreSQL and ensure `psql` is in PATH.

**Solution:** Add psql to PATH

If PostgreSQL is already installed:

1. Open:
      - System Properties → Environment Variables
      - Under System Variables → Path → Edit

2. Add: `C:\Program Files\PostgreSQL\<version>\bin`

3. Restart PowerShell

`Note:` Replace `<version>` with your PostgreSQL version


### Create database

#### Option A (preferred)

```bash
createdb -U postgres supplier_contacts
```

#### Option B (psql shell)

```bash
psql -U postgres
```

Inside:

```sql
CREATE DATABASE supplier_contacts;
\q
```



### Verify database

```bash
psql -U postgres -l
```

Check that:

```
supplier_contacts
```



### Run schema

```bash
psql -U postgres -d supplier_contacts -f schema.sql
```



### Verify tables

```bash
psql -U postgres -d supplier_contacts
```

Inside psql:

```sql
\dt
\d contacts
\q
```

Expected table:

```
contacts
```



# 5. Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/supplier_contacts
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

Refer to `.env.example` for reference.



# 6. Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

API documentation is available at:

```
http://127.0.0.1:8000/docs
```



# 7. Open Frontend

Ensure backend is running, then open:

* `index.html` (double-click), or
* Right-click → Open with browser



# 8. Usage

### Add Contact

* Fill form
* Click **Add Contact**
* Table updates instantly

### View Contacts

* Auto-loads on page open

### Delete Contact

* Click **Delete**
* Row removed without refresh
