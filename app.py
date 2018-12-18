from passlib.context import CryptContext
from tinydb import TinyDB, Query
import argparse

parser = argparse.ArgumentParser(description="Securely process and store passwords")
parser.add_argument("-u", "--user", help="User name", dest="user", required=True)
parser.add_argument("-p", "--password", help="User's password", dest="password", required=True)
parser.add_argument("-n", "--new", help="Create new user", dest="new", action="store_true")
parser.add_argument("-a", "--admin", help="Is admin user", dest="admin", action="store_true")
args = parser.parse_args()

db = TinyDB('./db/pass.json')
user_table = db.table("user")
Context = Query()
User = Query()

pass_ctx = CryptContext.from_path("./crypt.ini")


def eval_hash_from_user(user, password):
    res = user_table.get(User.name == user)
    hsh = None

    if res:
        hsh = res["hash"]

    ok, new_hash = pass_ctx.verify_and_update(password, hsh)

    if ok and new_hash:
        update_hash(args.user, new_hash)

    return ok


def update_hash(user, new_hash):
    user_table.upsert({"name": user, "hash": new_hash}, User.name == user)
    print("Hash Updated")


def create_user(user, password, admin):
    if admin:
        category = "admin"
    else:
        category = None

    n_hash = pass_ctx.hash(password, category=category)
    update_hash(user, n_hash)
    print("User created successfully")


if args.new:
    create_user(args.user, args.password, args.admin)
    exit(0)

valid = eval_hash_from_user(args.user, args.password)

if valid:
    print("Login Success!")
else:
    print("Login Failed!")

