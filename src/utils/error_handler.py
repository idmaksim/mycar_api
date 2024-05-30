from fastapi import HTTPException, status


async def handle_route_error(e: Exception, status_code: status):
    print(str(e))
    print(e)
    raise HTTPException(detail=str(e), status_code=status_code)
