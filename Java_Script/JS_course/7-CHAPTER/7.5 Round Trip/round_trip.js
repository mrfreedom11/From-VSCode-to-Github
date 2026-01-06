// Write code below 💖
const departTripTicket = {
  name : 'Dilshod',
  from : 'Uzbekistan',
  to : 'America',
  businessClass : True,
  upgrade() {
   if (this.businessClass === false) {
      this.businessClass = true;
   } else {
      console.log('Your ticket is already on business class');
   }
}


}