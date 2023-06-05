db = db.getSiblingDB('mcs');
db.createUser(
    {
        user: "mongoitmmvp",
        pwd: "mongoitmmvppassword",
        roles: [
            {
                role: "readWrite",
                db: "itmmvp"
            }
        ]
    }
);
db.createCollection('users');

db = db.getSiblingDB('dev');
db.createUser(
    {
        user: "mongoitmmvp",
        pwd: "mongoitmmvppassword",
        roles: [
            {
                role: "readWrite",
                db: "dev"
            }
        ]
    }
);
db.createCollection('users');