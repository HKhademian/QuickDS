const { BST, } = require('./lib/BST.js');

(function test() {
	// BST.DEBUG = true;
	let tree = new BST();
	let A = tree.insert('A');
	tree.insert('F');
	tree.insert('E');
	let D = tree.insert('D');
	tree.insert('C');
	tree.insert('B');
	let G = tree.insert('G');
	tree.insert('H');
	tree.insert('I');
	
	tree.print();

	let params = [];
	tree.root.inOrder(visit=(el)=>params.push(el.key));
	console.log("inorder: ", ...params);

	console.log( "A:", A.successor.key , A.proccessor.key );
	console.log( "G:", G.successor.key , G.proccessor.key );
	console.log( "D:", D.successor.key , D.proccessor.key );
	console.log( "X:", D.min.key , D.max.key );
})();
