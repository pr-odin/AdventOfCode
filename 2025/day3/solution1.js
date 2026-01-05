const fs = require('node:fs');
const path = "input.txt";

let lines;
let result = 0;

try {
	const data = fs.readFileSync(path, 'utf8');

	const split = data.trim().split('\n')

	lines = split;

} catch (err) {
	console.error(err);
}

for (const line of lines) {
	// console.log(line);

	let first = 0;
	let second = 0;

	for (let i = 0; i < line.length; i++) {

		const curr = line[i];

		const num = +curr;

		if (first < num && i + 1 < line.length) {
			second = line[i + 1];
			first = num;
			continue;
		}

		if (second < num) {
			second = num;
			continue;
		}
	}

	const totalNumber = `${first}${second}`;

	const totalAsInt = +totalNumber;
	result += totalAsInt;

	// console.log("First: %d, Second: %d", first, second);
	console.log(totalNumber);
}

console.log(result);

