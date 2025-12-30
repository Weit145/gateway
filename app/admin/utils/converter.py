from proto import admin_pb2



def convert_delete_post(id:int)->admin_pb2.DeletePostRequest:
    return admin_pb2.DeletePostRequest(
        post_id = id,
    )

def convert_delete_user(id:int)->admin_pb2.DeleteUserRequest:
    return admin_pb2.DeleteUserRequest(
        user_id = id,
    )

def convert_ban_user(id:int)->admin_pb2.BanUserRequest:
    return admin_pb2.BanUserRequest(
        user_id = id,
    )