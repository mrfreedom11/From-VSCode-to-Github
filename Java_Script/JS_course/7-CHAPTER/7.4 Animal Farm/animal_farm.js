// Ferma hayvonlari 💖

const pig = {
  name: 'Piggy',
  type: 'pig',
  age: 3,
  makeSound() {
    return `${this.name} ${this.age} yoshli ${this.type}, u "oink!" deydi.`;
  }
};

const sheep = {
  name: 'Shipty',
  type: 'sheep',
  age: 2,
  makeSound() {
    return `${this.name} ${this.age} yoshli ${this.type}, u "meee!" deydi.`;
  }
};

const dog = {
  name: 'Benny',
  type: 'dog',
  age: 10,
  makeSound() {
    return `${this.name} ${this.age} yoshli ${this.type}, u "woof!" deydi.`;
  }
};

// Natijani ko‘rish
console.log(pig.makeSound());
console.log(sheep.makeSound());
console.log(dog.makeSound());
