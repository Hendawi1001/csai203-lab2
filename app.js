document.querySelector('form').addEventListener('submit', function(event) {
  const name = document.getElementById('name').value;
  const age = document.getElementById('age').value;
  const major = document.getElementById('major').value;
  const password = document.getElementById('password').value;
  if (!name || !age || !major|| !password) {
      alert('Please fill in all fields.');
      event.preventDefault();
  }
});
