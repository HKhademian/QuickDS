module.exports = function Tri() {
	function Node(
		parent = undefined,  // no parent
		key = undefined, // no character
		exists = false, // no word till this node
	) {
		this.parent = parent;
		this.key = key;
		this.exists = exists;
		this.children = {}; // key->node map

		if(parent) parent.children[key] = this; // add this node to its parent

		this.child = (key) => {
			key = key.toLowerCase();
			return this.children[key] || new Node(this, key, false);
		}

		this.toString = () => {
			if(!this.parent) return this.key;
			return (this.parent.toString() || "") + this.key;
		};
	}

	this.root = new Node();
	const constructor = (data) => {
		this.add(data);
	}

	const add_rec = (str, node = this.root) => {
		if(!str || str.length<=0) {
			node.exists = (node!=this.root);
			return;
		}
		let key = str[0];
		node = node.child(key);
		return this.add_rec(str.slice(1), node);
	};

	const add_loop = (str) => {
		var node = this.root;
		for(var i=0; i<str.length; i++) {
			let key = str[i];
			node = node.child(str[i]);
		}
		node.exists = (node!=this.root);
	}

	// easy switch between loop and recursive version
	this.add = (data) => {
		if(Array.isArray(data))
			return data.forEach(el=>this.add(el));
		if(data)
			return add_loop(data);
	};

	constructor([...arguments]);
}
