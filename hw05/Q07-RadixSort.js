
function RadixSort(data) {
	// support lists, flat arguments , ...
	// all inputs to string
	data = [...arguments].flat().map(item => item.toString());

	// extract max digit count
	const digits = data.map(el => el.length).reduce((max, cur)=> cur>max?cur:max);
	
	// all inputs to same size
	data = data.map(item => item.padStart(digits, '\0'));
	
	for(let i=digits-1; i>=0; i--) {
		data = SortOnRadix(i, data);
		if(RadixSort.DEBUG) console.log("RadixSortedOn(radix="+i+"):", ...data);
	}

	//data = data.flat();
	return data;

	
	/// we can use any sort function in here
	/// a good choice is BucketSort or CountingSort
	function SortOnRadix(radix, data) {
		let buckets = [];
		
		data.forEach(item => {
			let key = item.charCodeAt(radix);
			let bucket = buckets[key] = buckets[key] || [];
			bucket.push(item);
		});

		return buckets.flat();
	}
}

(function test() {
	RadixSort.DEBUG = true;

	let data = ["COW", "DOG", "SEA", "RUG", "ROW", "MOB", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"];
	// let result = RadixSort(data, "AXE");
	let result = RadixSort(data);
	result;
})();
