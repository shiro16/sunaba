console.log(fn());
function fn() {
    return `foo`;
}
function fn() {
    return 'bar';
}

const hoge = function test() {
    return 'test'
}
console.log(hoge());

// error
//const hoge = function test() {
//    return 'test2'
//}