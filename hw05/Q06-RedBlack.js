const { BST, } = require('./lib/BST.js');
const { RedBlackTree, } = require('./lib/RedBlackTree.js');

(function test() {
	// BST.DEBUG = true;
	let tree = new RedBlackTree();
	// let tree = new BST();
	tree.insert('A');
	tree.insert('F');
	tree.insert('E');
	tree.insert('D');
	tree.insert('C');
	tree.insert('B');
	tree.insert('G');
	tree.insert('H');
	tree.insert('I');
	tree.print();
})();
