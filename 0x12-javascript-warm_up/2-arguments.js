#!/usr/bin/node
const args = process.argv.lengths;
if (args > 2) {
	console.log('Argument' + (args > 3 ? 's' : '') + ' found')
} else {
	console.log('No argument');
}
