const { BST, BST_Node, } = require('./BST');

const RED = 1, BLACK = 0;

class RedBlackTreeNode extends BST_Node {
	constructor(key = undefined, parent = undefined, left = undefined, right = undefined, color = undefined) {
		super(key, parent, left, right);
		this.color = color || RED;
	}

	get text() {
		let side = this.isLeft ? "L" : this.isRight? "R" : "";
		let [op,cl] = this.color==BLACK? ["[","]"] : this.color==RED? ["{","}"] : ["(",")"];
		return side + op + this.key+ cl;
	}
}

function RedBlackTree() {
	BST.call(this);
	let bstInsertNode = this.insertNode;

	this.newNode = RedBlackTreeNode;

	/// insert given node to parent node (redblack-style)
	this.insertNode = (parent, node) => {
		if(!node) return;

		//first add it like normal bst
		bstInsertNode(parent, node);
		node.color = RED;

		repairAfterInsert(node);
	};

	function repairAfterInsert(node) {
		let parent = node.parent;
		if(!parent) return repairAfterInsertCase1(node);
		if(parent.color == BLACK) return repairAfterInsertCase2(node);
		let uncle = node.uncle;
		if(uncle && uncle.color == RED) return repairAfterInsertCase3(node, parent, uncle);
		return repairAfterInsertCase4(node, parent);
	}

	function repairAfterInsertCase1(node) {
		node.color = BLACK;
	}

	function repairAfterInsertCase2(node) {
	}

	function repairAfterInsertCase3(node, parent, uncle) {
		parent.color = BLACK;
		uncle.color = BLACK;
		let grandParent = parent.parent;
		grandParent.color = RED;
		return repairAfterInsert(grandParent);
	}

	function repairAfterInsertCase4(node, parent) {
		if(node.isRight && parent.isLeft) {
			parent.rotateLeft();
			node = node.left;
		} else if(node.isLeft && parent.isRight) {
			parent.rotateRight();
			node = node.right;
		}

		repairAfterInsertCase4Step2(node);
	}

	function repairAfterInsertCase4Step2(node) {
		let parent = node.parent;
		let grandParent = parent.parent;
		if(node.isLeft) {
			grandParent.rotateRight();
		} else {
			grandParent.rotateLeft();
		}
		grandParent.color = RED;
		parent.color = BLACK;
	}
}

module.exports = {
	BST, BST_Node,
	RedBlackTree, RedBlackTreeNode,
}
