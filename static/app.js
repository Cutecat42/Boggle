count = 0;
score = 0;

inp = document.querySelector('#guess');
inp.focus();
inp.select();

setInterval(function() {
	count++;
	if (count === 60) {
		inp = document.querySelector('.remove');
		inp.remove();

		body = document.querySelector('body');
		btn = document.createElement('BUTTON');
		btn.innerHTML = 'Restart';
		btn.classList.add('restart');
		body.append(btn);
		btn.addEventListener('click', function() {
			location.reload();
		});
		setTimeout(function() {
			alert(`Game Over! You had a score of ${score}.`);
		}, 1);
	}
}, 1000);

button = document.querySelector('button');
button.addEventListener('click', validWord);

function validWord(e) {
	e.preventDefault();
	inp = document.querySelector('#guess').value;
	console.log(inp);
	check(inp);
}

async function check(inp) {
	response = await axios.get('/check-word', { params: { word: inp } });
	console.log(response);
	if (response.data == 'ok') {
		console.log('OK');
		ul = document.querySelector('.words');
		li = document.createElement('li');
		li.append(inp.toUpperCase());
		ul.append(li);

		scores = document.querySelector('.score');
		score += inp.length;
		scores.innerHTML = score;
	} else if (response.data == 'not-on-board') {
		console.log('not-on-board');
		alert('Word not on board!');
	} else if (response.data == 'guessed') {
		alert('Word already guessed!');
	} else {
		console.log('invalid word');
		alert('Invalid word!');
	}
	inp = document.querySelector('#guess');
	inp.value = '';
	inp.focus();
	inp.select();
}
