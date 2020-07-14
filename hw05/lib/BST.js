class BST_Node{
	constructor(key = undefined, parent = undefined, left = undefined, right = undefined) {
		this.key = key;
		this.parent = parent;
		this.left = left;
		this.right = right;
	}

	get text() {
		let side = this.isLeft ? "L: " : this.isRight? "R: " : "";
		return side + "(" + this.key + ")";
	}

	get isLeft() { return this == this.parent?.left; }
	get isRight() { return this == this.parent?.right; }
	get isLeaf() { return !this.left && !this.right; }
	get isRoot() { return !this.parent; }

	get hasParent(){ return !!this.parent; }
	get hasLeft() { return !!this.left; }
	get hasRight() { return !!this.right; }

	get root() { return this.parent?.root || this;}
	get grandParent() { return this.parent?.parent; }
	get uncle (){ return this.parent?.sibling; }
	get sibling () {
		let parent = this.parent;
		return !parent ? undefined : this == parent.left ? parent.right : parent.left;
	}

	get successor() {
		if(this.hasRight) return this.right.min;
		let node = this; // not this.parent
		while(node.isRight) {
			node = node.parent;
		}
		return node.parent || node;
	}

	get proccessor() {
		if(this.hasLeft) return this.left.max;
		let node = this; // not this.parent
		while(node.isLeft) {
			node = node.parent;
		}
		return node.parent || node;
	}

	get min() {
		let node = this;
		while(node.hasLeft) node = node.left;
		return node;
	}

	get max() {
		let node = this;
		while(node.hasRight) node = node.right;
		return node;
	}

	rotateLeft() {
		if(BST.DEBUG) console.log("RotateLeft("+this.key+")")

		let other = this.right;
		if(!other) return;
		let alpha = this.left;
		let beta = other.left;
		let gama = other.right;
		
		this.right = beta;
		if(beta) beta.parent = this;
		
		other.parent = this.parent;
		if(!this.parent) {
			this.parent = other;
		} else if (this.isLeft) {
			this.parent.left = other;
		} else if(this.isRight) {
			this.parent.right = other;
		}
		other.left = this;
		this.parent = other;
	}

	rotateRight() {
		if(BST.DEBUG) console.log("RotateRight("+this.key+")")
		
		let other = this.left;
		if(!other) return;
		let alpha = other.left;
		let beta = other.right;
		let gama = this.right;
		
		this.left = beta;
		if(beta) beta.parent = this;
		
		other.parent = this.parent;
		if(!this.parent) {
			this.parent = other;
		} else if (this.isLeft) {
			this.parent.left = other;
		} else if(this.isRight) {
			this.parent.right = other;
		}
		other.right = this;
		this.parent = other;
	}

	// https://stackoverflow.com/a/8948691
	write(buffer = [], prefix = "", childrenPrefix="") {
		buffer.push(prefix);
		buffer.push(this.text);
		buffer.push('\n');
	
		const writeChild = (child, hasNext, buffer, childrenPrefix) => {
			let pref = childrenPrefix + (hasNext?"├─── ":"└─── ");
			if(child) {
				let childPref = childrenPrefix + (hasNext?"│    ":"     ");
				return child.write(buffer, pref, childPref);
			} else {
				buffer.push(pref);
				buffer.push("X");
				buffer.push('\n');
				return buffer;
			}
		}
	
		if(this.hasLeft || this.hasRight) {
			// first show right for better visiuals
			buffer = writeChild(this.right, true, buffer, childrenPrefix);
			buffer = writeChild(this.left, false, buffer, childrenPrefix);
		}
		
		return buffer;
	}

	printNode = (node) => {
		console.log(node.text);
	}

	preOrder( visit = this.printNode, params = undefined ) {
		visit(this, params);
		this.left?.preOrder( visit, params );
		this.right?.preOrder( visit, params );
	}

	postOrder( visit = this.printNode, params = undefined ) {
		this.left?.postOrder( visit, params );
		this.right?.postOrder( visit, params );
		visit(this, params);
	}

	inOrder( visit = this.printNode, params = undefined ) {
		this.left?.inOrder( visit, params );
		visit(this, params);
		this.right?.inOrder( visit, params );
	}
}


function BST() {
	this.root = undefined;

	// to support any augmented DSs
	this.newNode = BST_Node;

	/// create new node from key, add it to bst and return it
	this.insert = (key) => {
		let node = new this.newNode(key=key);
		this.insertNode(root=this.root, node=node);
		this.root = node.root;
		if(BST.DEBUG) {
			console.log(key + " inserted " + (node.isRoot ? "AS ROOT" : ((node.isLeft? " as Left of " : " as Right of ") + node.parent.key)));
		}
		return node;
	}

	/// insert node to bst-style parent
	this.insertNode = (parent, node) => {
		if(!node || !parent) return;

		if(node.key > parent.key) {
			if(parent.hasRight) {
				return this.insertNode(parent.right, node);
			} else {
				node.parent = parent;
				parent.right = node;
			}
		} else {
			if(parent.hasLeft) {
				return this.insertNode(parent.left, node);
			} else {
				node.parent = parent;
				parent.left = node;
			}
		}
	}
	this.print = () => {
		if(this.root)
			console.log(this.root.write().join(''));
		else
			console.log("EMPTY TREE");
	}
}

BST.DEBUG = false;

module.exports = {
	BST, BST_Node,
}
