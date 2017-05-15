# $ echo var_name=entry
# example: $ echo PASSWORD=my_secret_password

import os

print(os.environ["PASSWORD"])
