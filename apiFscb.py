"""
https://developer.scb/#/documents/documentation/qr-payment/payment-confirmation.html
https://github.com/codustry/thanakan/blob/main/callback_scb/main.py #thx
"""
"""run on debugmode test""" 
"""pip3 install uvicorn"""
"""pip3 install fastapi_utils"""
"""pip3 install fastapi"""

from typing import Literal, Optional, Union
import json
import uuid
from enum import Enum
from fastapi import Body, FastAPI, Request
from fastapi_utils.api_model import APIModel
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI()

"""on qr 30 thai model"""
class PaymentConfirmation(APIModel):
    ''' transaction_id: str = Field(description="Transaction ID generated by source system")
    amount: str = Field(description="Amount of Transaction")
    transaction_date_and_time: str = Field(alias="transactionDateandTime",
    description="Date and Time of transaction in ISO 8601 format SCB EASY App Payment (BP), SCB EASY App Payment (CCFA), SCB EASY App Payment (IPP), QR30, Alipay, WeChatPay : Time in GMT+7 QRCS : Time in GMT",
    )
    currency_code: str = Field(description="Code to define currency for transaction based on ISO 4217 for transactionAmount. Thai Baht is ‘764’")
    transaction_type: Union[str] '''

    payeeProxyId : Optional[str] = None
    payeeProxyType : Optional[str] = None
    payeeAccountNumber : Optional[str] = None
    payerAccountNumber: Optional[str] = None
    payerAccountName: Optional[str] = None
    payerName: Optional[str] = None
    sendingBankCode: Optional[str] = None
    receivingBankCode: Optional[str] = None
    amount: Optional[str] = None
    transactionId: Optional[str] = None
    transactionDateandTime: Optional[str] = None
    billPaymentRef1: Optional[str] = None
    billPaymentRef2: Optional[str] = None
    billPaymentRef3: Optional[str] = None
    currencyCode: Optional[str] = None
    channelCode: Optional[str] = None
    transactionType: Optional[str] = None

"""endpoint callback"""  
@app.post("/scb/confirm/payment")
async def handle_scb_callback(confirmation: PaymentConfirmation):

    """response back"""
    response = {
        "resCode": "00",
        "resDesc ": "success",
        "transactionId": confirmation.transactionId,
        "confirmId": "abc00confirm",
    }
    """create json body name gen by uuid"""

    with open(f"{uuid.uuid4().hex}_response.json", "w") as f:
        json.dump(response, f)

    with open(f"{uuid.uuid4().hex}_confirmation.json", "w") as f:
        json.dump(confirmation.dict(), f)

    return response


@app.get("/scb/confirm/payment")
async def ok():
    """
    check !!
    """
    return "ok"

"""running on python3 apiFscb.py"""
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
