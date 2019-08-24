let links = document.querySelectorAll(".ripple");

for (link of links) {
    link.addEventListener('click', (e) => {
        console.log('ripple!');
        e.currentTarget.classList.add('ripple-clicked');
    });
}
