axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log((response.data));
})

// 동기 함수는 순서대로 실행되기 때문에, 시간이 오래 걸리는 함수를 동기 함수로 실행하면, 다음 코드가 실행되지 않는다.

// 비동기 함수는 순서대로 실행되지 않기 때문에, 시간이 오래 걸리는 함수를 비동기 함수로 실행하면, 다음 코드가 먼저 실행된다.