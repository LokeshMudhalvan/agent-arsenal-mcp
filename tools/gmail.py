import grpc
from server import mcp
from . import gmailSvc_pb2
from . import gmailSvc_pb2_grpc

@mcp.tool()
def list_gmails(count: int, account: str):
    """
        Get the top { count } emails content in the specified 
        user's gmail { account }
    """
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = gmailSvc_pb2_grpc.GmailServiceStub(channel)
        response = stub.FetchMails(gmailSvc_pb2.FetchGmailMessagesRequest(
            count=count, 
            account=account
        ))

        return response 