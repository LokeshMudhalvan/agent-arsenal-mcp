from server import mcp
import tools.gmail 

if __name__ == "__main__":
    print("mcp server starting")
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)