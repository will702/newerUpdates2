from kivy.utils import platform
def check_permission():
    try:
        if platform == 'android':
            from android.permissions import Permission, request_permissions


            def callback(permission, results):
                if all([res for res in results]):
                    pass
                else:
                    pass


            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE], callback)
    except:
        pass