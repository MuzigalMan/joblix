import { csrf_token } from "{{ url_for('static', filename='js/events.js') }}";

document.getElementById('myForm').addEventListener('submit', (event) => {
  event.preventDefault(); // prevent the default form submission behavior

  var arg1 = document.getElementById('#job-name').val();
  var arg2 = document.getElementById('#job-location').val();
  var arg3 = document.getElementById('#file').val();

  var data = {arg1, arg2, arg3}

  // Show loading screen
  const loadingScreen = document.getElementById('loading-screen');
  loadingScreen.style.display = 'flex';

  fetch('/result', {
    method: 'POST',
    body: data,
    headers: {
      'X-CSRFToken': csrf_token ,
    },
  })
  .then((res) => res.json())
  .then(error => console.error(error));
});
