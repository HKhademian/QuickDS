// to run this code :
// node ./{file}.js
// or
// deno run ./{file}.js

const Tri = require("./lib/Tri.js");

Tri.prototype.LCP = function() {
	var node = this.root, keys = undefined;
	while((keys=Object.keys(node.children)).length == 1) {
		node = node.children[keys[0]];
	}
	return node; // this is deepest common node
};

(function test1() {
	const lcp = dict.LCP();
	const res = lcp.toString();
	console.log("LCP:", res);

})/*()*/;

(function main() {
	
	// const dict  = new Tri("Hossain", "Hassan", "Hamid");
	// const dict  = new Tri("Book", "Booklet", "Boom", "Bombs");
	// const dict  = new Tri("Admiral", "Book", "Booklet", "Boom","Bombs");
	const dict  = new Tri("Compact", "Companionate", "Complex", "Compare", "Compass");
	const lcp = dict.LCP();
	const res = lcp.toString();
	console.log("LCP:", res);

})();
