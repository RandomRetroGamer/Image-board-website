document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('uploadForm');
    if (!form) return;

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const file = document.getElementById('image').files[0];

        if (!file) return;

        const reader = new FileReader();

        reader.onload = () => {
            const imageURL = reader.result;
            addPost(title, description, imageURL);

            // Reset the form after the post is added
            document.getElementById('uploadForm').reset();
        };

        reader.readAsDataURL(file);
    });

    function addPost(title, description, imageURL) {
        const container = document.getElementById('postContainer');
        const post = document.createElement('div');
        post.className = 'post';

        post.innerHTML = `
            <h2>${title}</h2>
            <img src="${imageURL}" alt="${title}" style="max-width: 200px;" />
            <p>${description}</p>
        `;

        container.prepend(post); // Adds new post at the top
    }
});

function toggleComments(button) {
    const post = button.closest('.post');
    const commentsSection = post.querySelector('.comments-section');

    if (commentsSection.style.display === 'none' || commentsSection.style.display === '') {
        commentsSection.style.display = 'block';
    } else {
        commentsSection.style.display = 'none';
    }
}
