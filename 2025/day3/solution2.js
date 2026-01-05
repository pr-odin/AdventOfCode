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

	// if (line != "811111111111119") continue;

	const arrLen = 12;

	let numArr = new Array(arrLen);

	numArr.fill(0);


	let startIndex = 0;

	for (let j = 0; j < arrLen; j++) {


		// console.log(`Full run with ${line}`)

		for (let i = startIndex; i < line.length; i++) {

			const curr = line[i];

			// console.log(`New run with ${curr}`)

			const num = +curr;


			// console.log(`calulation ${i + (arrLen - j)}`)
			// console.log(`lineLen ${line.length}`)
			if (numArr[j] < num && i + (arrLen - j) <= line.length) {


				startIndex = i + 1;
				// console.log(`startIndex ${startIndex}`);
				numArr[j] = num;
				continue;
			}
		}

	}

	let numArrString = "";

	for (const n of numArr) {
		numArrString += `${n}`;
	}

	const totalNumber = numArrString;
	const totalAsInt = +totalNumber;
	result += totalAsInt;

	// console.log(numArr);
	console.log(totalNumber);
}

console.log(result);

