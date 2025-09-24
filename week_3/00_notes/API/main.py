from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path
import logging
from datetime import datetime

from logging_config import setup_logging
from Model.DataLoad_CSV import DataLoad_CSV


#Setup logging
setup_logging()

logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="CSV to JSON Reader API",
    description="API to read CSV files and return contents as JSON with filtering and pagination",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data directory for storing CSV files
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


# API Endpoints
@app.get("/")
async def root():
    return {"message": "This is a test case scenario for reference."}

@app.get("/csv/get_employees", response_class=JSONResponse )
async def read_csv():

    file_path = r"C:\Users\AC129VR\OneDrive - EY\Documents\GitHub\python-bootcamp-exercise\week_3\00_notes\API\PythonTraining-Employees02.csv"
    
    try:
        fl = DataLoad_CSV(file_path)
        fl.load_csv()
        fl.validate()
        fl.get_data()
        
        # Convert to JSON-serializable format
        response = json.dumps(fl.get_data())
        
        return response
        
    except Exception as e:
        logger.error(f"Error processing CSV: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing CSV: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
