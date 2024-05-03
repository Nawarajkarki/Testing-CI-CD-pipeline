from fastapi import APIRouter, HTTPException
import subprocess

listener = APIRouter()


@listener.post("/listener")
async def webhook_listener():
    try:
        subprocess.run(["git", "pull"])
        
        subprocess.run(["bash", "/home/ec2-user/Testing-CI-CD-pipeline/cicd.sh"])
        
        return {"message": "Changes pulled successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to pull changes: {e}")
