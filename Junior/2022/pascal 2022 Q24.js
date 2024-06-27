var isSquare = function (n) {
    return n > 0 && Math.sqrt(n) % 1 === 0;
};

var perfectCube = (N) => {
    let cube;

    // Iterate from 1-N
    for (let i = 0; i <= N; i++) {

        // Find the cube of
        // every number
        cube = i * i * i;

        // Check if cube equals
        // N or not
        if (cube === N) {
            return true;
        }
        else if (cube > N) {
            return false;
        }
    }
}

let count = 0;
for (let i = 1000000; i < 10000000; i++) {

    // let leftmost3 = i /10000;
    let str = i.toString();

    let left3 = parseInt(str.substring(0, 3));
    let right4 = parseInt(str.substring(3));

    if (perfectCube(left3) && isSquare(right4) && str[2] === str[6] && str[3] !== '0') {
        console.log(i);
        count++;
    }


}
console.log(count);
