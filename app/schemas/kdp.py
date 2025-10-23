from pydantic import BaseModel

class KDPPayload(BaseModel):
    accountIdentifier: str
    htmlContent: str
