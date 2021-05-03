const patty = {
    name: 'Patty Rabbit',
    email: 'patty@maple.town',
    address: { town: 'Maple Town' },
};

const rolley = { ...patty, name: 'Rolley Cocker' };
rolley.email = 'rolley@palm.town';
rolley.address.town = 'Palm Town';

console.log(patty);

const patty2 = {
    name: 'Patty Rabbit',
    email: 'patty@maple.town',
    address: { town: 'Maple Town' },
}; 

const rolley2 = JSON.parse(JSON.stringify(patty2));
rolley2.namq = 'Rolley Cocker';
rolley2.email = 'rolley@palm.town';
rolley2.address.town = 'Palm Town';

console.log(patty2);