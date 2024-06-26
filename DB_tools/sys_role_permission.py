from DB_tools.sys_permission import permission_datas

# 计算出所有权限的数量
all_permission = 0
for permission_data in permission_datas:
    all_permission += permission_data["method"].__len__()

role_permission_datas = [
    {
        "role_id": 1,
        "permission_id": list(range(1, all_permission + 1)),
    },
    {
        "role_id": 2,
        "permission_id": list(range(1, 44)),
    },
    {
        "role_id": 3,
        "permission_id": [1, 2, 3, 4, 5, 6, 7, 29, 36, 43],
    },
]
