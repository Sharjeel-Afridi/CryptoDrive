const navBtns = document.querySelectorAll('.nav-btn');

navBtns.forEach(navBtn => {
    navBtn.addEventListener('click', () => {
        navBtns.forEach(btn => {
            btn.classList.remove("text-black", "border-white", "rounded-full", "bg-blue-100");
        });
        navBtn.classList.add("text-black", "border-white", "rounded-full", "bg-blue-100");
    });
});
