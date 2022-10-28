// 코드를 작성해 주세요
const buttons = document.querySelectorAll('button');
document.querySelector('#scissors-button > img').id = 'scissors';
document.querySelector('#rock-button > img').id = 'rock';
document.querySelector('#paper-button > img').id = 'paper';

const player1 = document.querySelector('#player1-img');
const player2 = document.querySelector('#player2-img');

const countA = document.querySelector('.countA');
const countB = document.querySelector('.countB');

const result = document.querySelector('.modal-content');
const modal = document.querySelector('.modal');

function CloseModal() {
  modal.style.display = 'none';
}

buttons.forEach((button) => {
  button.addEventListener('click', play);
});

modal.addEventListener('click', CloseModal);

let change = 0;
function player2change() {
  if (change === 0) {
    player2.src = './img/rock.png';
  } else if (change === 1) {  
    player2.src = './img/scissors.png';
  } else if (change === 2) {
    player2.src = './img/paper.png';
  }
  change = (change + 1) % 3;
};

function play(event) {
  const player1Choice = event.target.id;
  player1.src = `./img/${player1Choice}.png`;
  const timer = setInterval(player2change, 100);
  setTimeout(() => {
    clearInterval(timer);
    const player2ChoiceNum = Math.floor(Math.random() * 3);
    const choices = ['scissors', 'rock', 'paper'];
    const player2Choice = choices[player2ChoiceNum];
  
    player2.src = `./img/${player2Choice}.png`;
  
    if (player1Choice === player2Choice) {
      result.innerText = '비겼습니다!';
    } else if (
      (player1Choice === 'rock' && player2Choice === 'scissors') ||
      (player1Choice === 'scissors' && player2Choice === 'paper') ||
      (player1Choice === 'paper' && player2Choice === 'rock')
    ) {
      result.innerText = '이겼습니다!';
      countA.innerText = Number(countA.innerText) + 1;
    } else {
      result.innerText = '졌습니다!';
      countB.innerText = Number(countB.innerText) + 1;
    }
    modal.style.display = 'flex';
  }, 3000);
}