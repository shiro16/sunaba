type User = {
    username: string;
    address: {
        zipcode: string;
        town: string;
    }
};

const isUser = (arg: unknown): arg is User => {
    const u = arg as User;

    return (
        typeof u?.username === 'string' &&
        typeof u?.address?.zipcode === 'string' &&
        typeof u?.address?.town == 'string'
    );
};

const u1: unknown = JSON.parse('{}');
const u2: unknown = JSON.parse('{ "username": "patty", "address": "hoge"}');
const u3: unknown = JSON.parse('{ "username": "patty", "address": { "zipcode": "111", "town": "hoge" } }');

[u1, u2, u3].forEach((u) => {
    if (isUser(u)) {
        console.log(`${u.username} is User`);
    } else {
        console.log("It's not User");
    }
});