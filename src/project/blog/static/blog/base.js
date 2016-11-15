import $ from 'jquery';

class Greeting {
  constructor() {
    this.title = "Kottenator's Blog";
    console.log(`Welcome to ${this.title}!`);
  }
}

$(() => new Greeting());
