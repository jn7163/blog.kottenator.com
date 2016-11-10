class Greeting {
  constructor () {
    this.x = "Kottenator's Blog";
    console.log(`Welcome to ${this.x}!`);
  }
}

document.addEventListener('DOMContentLoaded', function () {
  new Greeting();
});
