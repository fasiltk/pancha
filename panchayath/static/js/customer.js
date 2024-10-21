
// document.addEventListener("DOMContentLoaded", function () {
//     document.querySelectorAll('.b').forEach(function(bElement) {
//         bElement.classList.add('hidden');
//     });

//     document.querySelectorAll('.toggle-icon').forEach(function(toggleIcon, index) {
//         toggleIcon.addEventListener('click', function() {
//             const card = toggleIcon.closest('.card');
//             card.querySelector('.a').classList.add('hidden');
//             card.querySelector('.b').classList.remove('hidden');
//         });
//     });

//     document.querySelectorAll('.arrow-icon').forEach(function(arrowIcon, index) {
//         arrowIcon.addEventListener('click', function() {
//             const card = arrowIcon.closest('.card');
//             card.querySelector('.b').classList.add('hidden');
//             card.querySelector('.a').classList.remove('hidden');
//         });
//     });

//     document.querySelectorAll('.book').forEach(function(book, index) {
//         book.addEventListener('click', function() {
//             card.querySelector('.c').classList.remove('hidden');
//         });
//     });

// });




document.addEventListener("DOMContentLoaded", function () {
    // Hide all the 'b' and 'c' sections initially
    document.querySelectorAll('.b, .c').forEach(function(element) {
        element.classList.add('hidden');
    });

    // Add event listeners to all the toggle icons
    document.querySelectorAll('.toggle-icon').forEach(function(toggleIcon, index) {
        toggleIcon.addEventListener('click', function() {
            const card = toggleIcon.closest('.card');
            card.querySelector('.a').classList.add('hidden');
            card.querySelector('.b').classList.remove('hidden');
        });
    });

    // Add event listeners to all the arrow icons
    document.querySelectorAll('.arrow-icon').forEach(function(arrowIcon, index) {
        arrowIcon.addEventListener('click', function() {
            const card = arrowIcon.closest('.card');
            card.querySelector('.b').classList.add('hidden');
            card.querySelector('.a').classList.remove('hidden');
        });
    });

    // Add event listeners to all the book buttons
    document.querySelectorAll('.book').forEach(function(book, index) {
        book.addEventListener('click', function() {
            const card = book.closest('.card'); // Get the closest card for the clicked button
            card.querySelector('.c').classList.remove('hidden'); // Show the 'c' section
            card.querySelector('.b').classList.add('hidden');
        });
    });

    document.querySelectorAll('.fa-house-user').forEach(function(user, index) {
        user.addEventListener('click', function() {
            const card = user.closest('.card'); 
            card.querySelector('.a').classList.remove('hidden'); 
            card.querySelector('.b').classList.add('hidden');
            card.querySelector('.c').classList.add('hidden');

        });
    });

});
