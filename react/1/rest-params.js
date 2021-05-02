const showNames = (a, b, ...rest) => {
    console.log(a);
    console.log(b);
    console.log(rest);
};

showNames('John', 'Jane', 'Johnny', 'Jenny', 'Julia');

const showAllArgs = (...args) => { 
    console.log(args);
};

showAllArgs('A','B','C','D');

const sum = (i, ...[j, k, l]) => i + j + k + l;

console.log(sum(1, 2, 3, 4));
console.log(sum(1, 2, 3, 4, 5));