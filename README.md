# image-like-bot

this project is a bot that can count the number of likes on a post on instagram and then like it.

## Setup

1. Fork this repository
2. Clone your forked repository
3. Create virtual environment

    ```bash
    python3 -m venv venv
    ```

4. activate virtual environment

   ```bash
    source venv/bin/activate
    ```

5. Install requirements

    ```bash
     pip install -r requirements.txt
     ```

## Implementation

- Database Schema

    ```json
    {
        "image": {
            {
                "image_id": "str",
                "created_at": "datetime",
                "updated_at": "datetime",
                "likes": [
                    {
                        "user_id": "str",
                        "created_at": "datetime"
                    }
                ],
                "dislikes": [
                    {
                        "user_id": "str",
                        "created_at": "datetime"
                    }
                ]
            }
        }
    }
    ```

### project file structure

```bash
.
├── README.md
├── .gitignore
├── bot.py
├── worker.py
├── requirements.txt
├── db.py
├── db.json
```
