class Greeting {
  constructor () {
    this.x = "My Little Blog";
    console.log(`Welcome to ${this.x}!`);
  }
}

document.addEventListener('DOMContentLoaded', function () {
  new Greeting();
});
