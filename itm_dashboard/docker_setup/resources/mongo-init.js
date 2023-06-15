db = db.getSiblingDB('dashboard');
db.createUser(
    {
        user: "simplemongousername",
        pwd: "simplemongopassword",
        roles: [
            {
                role: "readWrite",
                db: "dashboard"
            }
        ]
    }
);
db.createCollection('users');
