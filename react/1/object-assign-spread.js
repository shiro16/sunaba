const original = { a: 1, b: 2, c: 3 };

const copy = Object.assign({}, original);
console.log(copy);
console.log(copy == original);

const assigned = Object.assign(original, { c : 10, d: 11 }, { d: 100 });
console.log(assigned);
console.log(original);

const copy2 = { ...original };
console.log(copy2);
console.log(copy2 === original);

const assigned2 = { ...original, ...{ e: 10, f: 111 }, f: 1000};
console.log(assigned2);
console.log(original);