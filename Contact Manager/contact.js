// JavaScript (script.js)
let editMode = false;
let currentEditIndex = null;

function addContact() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;

    if (name && email && phone) {
        if (editMode) {
            // Edit existing contact
            const contactList = document.getElementById('contactList');
            const li = contactList.children[currentEditIndex];
            li.innerHTML = `
                Name: ${name}<br>
                Email: ${email}<br>
                Phone: ${phone}<br>
                <button onclick="editContact(${currentEditIndex})">Edit</button>
                <button onclick="deleteContact(${currentEditIndex})">Delete</button>
            `;
            editMode = false;
        } else {
            // Add new contact
            const contactList = document.getElementById('contactList');
            const li = document.createElement('li');
            li.innerHTML = `
                Name: ${name}<br>
                Email: ${email}<br>
                Phone: ${phone}<br>
                <button onclick="editContact(${contactList.children.length})">Edit</button>
                <button onclick="deleteContact(${contactList.children.length})">Delete</button>
            `;
            contactList.appendChild(li);
        }
        clearFields();
    } else {
        alert('Please fill in all fields.');
    }
}

function clearFields() {
    document.getElementById('name').value = '';
    document.getElementById('email').value = '';
    document.getElementById('phone').value = '';
}

function editContact(index) {
    const contact = document.getElementById('contactList').children[index];
    const contactInfo = contact.innerHTML.split('<br>');
    const name = contactInfo[0].split(': ')[1];
    const email = contactInfo[1].split(': ')[1];
    const phone = contactInfo[2].split(': ')[1];
    document.getElementById('name').value = name;
    document.getElementById('email').value = email;
    document.getElementById('phone').value = phone;
    editMode = true;
    currentEditIndex = index;
}

function deleteContact(index) {
    document.getElementById('contactList').children[index].remove();
}
