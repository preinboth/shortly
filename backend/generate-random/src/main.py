import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    uvicorn.run(
        "src.server:api",
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT")),
        # log_config=logging_config,
        reload=True,
    )
