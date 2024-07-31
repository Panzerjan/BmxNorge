from bmx.comi import CommissionerManager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
manager = CommissionerManager('./files/comi.json')

class Commissioner(BaseModel):
    name: str
    type: str
    club: Optional[str] = None
    status: Optional[bool] = None

class UpdateCommissioner(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    club: Optional[str] = None
    status: Optional[bool] = None

@app.post("/commissioners", status_code=201)
def add_commissioner(commissioner: Commissioner):
    response, status = manager.add_commissioner(commissioner.dict())
    if status != 201:
        raise HTTPException(status_code=status, detail=response["message"])
    return response

@app.put("/commissioners/{commissioner_id}")
def update_commissioner(commissioner_id: str, updated_data: UpdateCommissioner):
    response, status = manager.update_commissioner(commissioner_id, updated_data.dict(exclude_unset=True))
    if status != 200:
        raise HTTPException(status_code=status, detail=response["message"])
    return response

@app.delete("/commissioners/{name}")
def remove_commissioner(name: str):
    response, status = manager.remove_commissioner(name)
    if status != 200:
        raise HTTPException(status_code=status, detail=response["message"])
    return response

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)