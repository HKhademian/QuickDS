function parent(index) {
    return Math.floor((index-1)/2);
}

function child(index, i) {
    return index*2 + 1 + i;
}

function upHeapify(heap, index) {
    let debug = insert.DEBUG;

    while(index>0) {
        let parentIndex = parent(index);
        if(heap[index] > heap[parentIndex]) {
            let t = heap[parentIndex];
            heap[parentIndex] = heap[index];
            heap[index] = t;
            index = parentIndex;

            if(debug) console.log(" - upHeapify: ", ...heap);
        } else break;
    }
}

function downHeapify(heap, index) {
    let debug = insert.DEBUG;

    while( index < heap.length) {
        let childIndex = child(index, 0);
        if(heap[index]<heap[childIndex]);
        else {
            childIndex = child(index, 1);
            if(heap[index]<heap[childIndex]);
            else break;
        }

        let t = heap[childIndex];
        heap[childIndex] = heap[index];
        heap[index] = t;

        index = childIndex;

        if(debug) console.log(" - downHeapify: ", ...heap);
    }
}

function insert(heap, item) {
    let debug = insert.DEBUG;

    if(debug) console.log("before insert: ", ...heap);
    heap.push(item);
    if(debug) console.log("after insert: ", ...heap);

    // swim
    upHeapify(heap, heap.length-1);
}

function maxExtract(heap) {
    // return extraxt(heap, 0);
    let debug = insert.DEBUG;
    
    if(debug) console.log("before extract: ", ...heap);

    let res = heap.shift();
    if(heap.length <= 1) return res;
    heap.unshift(heap.pop());
    
    if(debug) console.log("after extract: ", ...heap);

    // downHeapify
    downHeapify(heap, 0);

    return res;
}


module.exports = { parent, child, insert, maxExtract, upHeapify, downHeapify, };
