

var promiseTRRARNOSG = promiseThatResolvesRandomlyAfterRandomNumnberOfSecondsGenerator = function() {
  return new Promise(function(resolve, reject) {
    let randomNumberOfSeconds = Math.random()*10;
    setTimeout(function() {
      let randomiseResolving = Math.random()*10;
      if (randomiseResolving > 5) {
        resolve({
          randomNumberOfSeconds: randomNumberOfSeconds,
          randomiseResolving: randomiseResolving
        });
      } else {
        reject({
          randomNumberOfSeconds: randomNumberOfSeconds,
          randomiseResolving: randomiseResolving
        });
      }
    }, randomNumberOfSeconds * 1000);
  });
};


console.log('starting execution of function that returns a promise...')
console.log(
  promiseTRRARNOSG()
  .then((resolvedVal) => {console.log(`accepted value: ${resolvedVal.randomNumberOfSeconds}`)})
  .catch((rejectedVal) => {console.log(`rejected value: ${rejectedVal.randomNumberOfSeconds}`)}));

// OR
async function asyncFunc () {
  try{
const result = await promiseTRRARNOSG()
console.log(`In async: accepted: ${result.randomNumberOfSeconds}`)
  } catch (e){
    console.log('In async: promise was rejected!')
  }
}
console.log('starting execution of async func...')
asyncFunc()
/*
const performance = require('perf_hooks').performance;
let startTime = performance.now();
async function fetchAllUsersDetailsParallelyWithStats() {
  let singleUsersDetailsPromises = [];
  for (name of ["nkgokul", "BrendanEich", "gaearon"]) {
    let promise = fetchSingleUsersDetailsWithStats(name);
    console.log(
      "Created Promise for API call of " + name + " at " + executingAt()
    );
    singleUsersDetailsPromises.push(promise);
  }
  console.log("Finished adding all promises at " + executingAt());
  let allUsersDetails = await Promise.all(singleUsersDetailsPromises);
  console.log("Got the results for all promises at " + executingAt());
  console.log(allUsersDetails);
}async function fetchSingleUsersDetailsWithStats(name) {
  console.log("Starting API call for " + name + " at " + executingAt());
  userDetails = await fetch("https://api.github.com/users/" + name);
  userDetailsJSON = await userDetails.json();
  console.log("Finished API call for " + name + " at " + executingAt());
  return userDetailsJSON;
}
fetchAllUsersDetailsParallelyWithStats();



var parallel = async function() {
  startTime = performance.now();
  promisesArray = [];
  console.log(executingAt());
  promisesArray.push(promiseTRSANSG(3));
  promisesArray.push(promiseTRSANSG(4));
  result = await Promise.all(promisesArray);
  console.log(result);
  console.log(executingAt());
}
parallel();

*/
// gather stats for all 3 people at the same time!
//https://hackernoon.com/understanding-async-await-in-javascript-1d81bb079b2c