const { maxExtract, insert,  } = require('./lib/MaxHeap');

(function test() {
    insert.DEBUG = true;
    let heap = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1];
    console.log(maxExtract(heap));
})();