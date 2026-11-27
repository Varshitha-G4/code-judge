##### Make sure to activate virtual environment first

# DAY 1

### Setup Fast API
``` pip install "fastapi[standard]" ```

Added decorators to add path

/health endpoint to check if the setup is working fine


# Day 2 – FastAPI Concepts & Validation

## 1. UUID (Universally Unique Identifier)

UUIDs are used to uniquely identify each code submission.

```python
from uuid import UUID, uuid4
```

- `uuid4()` – Generates a random UUID (version 4).
- `UUID` – Represents and validates an existing UUID.

Why UUID instead of integers?
- Very low probability of ID collisions.
- IDs can be generated independently across multiple servers.
- Harder to guess than sequential IDs.
- Useful when multiple workers or instances are involved.

## 2. Literal (from typing)

`Literal` restricts a variable to specific predefined values.

```python
from typing import Literal

language: Literal["python"]
```

Only `"python"` is accepted.

Multiple allowed values:

```python
language: Literal["python", "java", "cpp"]
```

Use case: Restrict programming languages supported by the Code Judge.

## 3. Pydantic BaseModel

`BaseModel` is used to define data models (schemas) and validate incoming data.

```python
from pydantic import BaseModel

class SubmissionIn(BaseModel):
    problem_id: int
    language: str
    code: str
```

It defines:
- Expected field names.
- Expected data types.
- Automatic request validation.

If the incoming data doesn't match the schema, FastAPI returns HTTP 422 (Unprocessable Entity).

## 4. Pydantic Field

`Field` adds additional validation constraints to individual fields.

```python
from pydantic import BaseModel, Field

class SubmissionIn(BaseModel):
    problem_id: int = Field(gt=0)
    code: str = Field(min_length=1, max_length=20000)
```

Common Field constraints:

| Constraint | Meaning |
|---|---|
| `gt` | Greater than |
| `ge` | Greater than or equal to |
| `lt` | Less than |
| `le` | Less than or equal to |
| `min_length` | Minimum string length |
| `max_length` | Maximum string length |

Examples:

- `Field(gt=0)` – Value must be greater than zero.
- `Field(min_length=1)` – String cannot be empty.
- `Field(max_length=20000)` – Maximum 20,000 characters.


**Remember:**
- Pydantic validates the structure and constraints of incoming requests.


