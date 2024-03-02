const navBtns = document.querySelectorAll('.nav-btn');
const contentDiv = document.querySelector('#content');

const homeComponent = `<h1 class="font-bold text-2xl mt-[80px] ml-[50px]">HOME</h1>`;
const mydriveComponent = `<h1 class="font-bold text-2xl mt-[80px] ml-[50px]">My Drive</h1>`;
const recentComponent = `<h1 class="font-bold text-2xl mt-[80px] ml-[50px]">Recent</h1>`;

const components = {
    "HOME": `
        <h1 class="font-bold text-2xl mt-[80px] ml-[50px]">
            HOME
        </h1>`,
    "My Drive": `
        <h1 class="font-bold text-2xl mt-[80px] ml-[50px]">
            My Drive
        </h1>`,
    "Recent": `
        <h1 class="font-bold text-2xl mt-[80px] ml-[50px]">
            Recent
        </h1>`
};

function renderComponent(component){
    contentDiv.innerHTML = component;
}

navBtns.forEach(navBtn => {
    navBtn.addEventListener('click', (event) => {
        let buttonText = event.target.textContent.trim();
        let buttonComponent = components[buttonText];

        if (buttonComponent) {
            renderComponent(buttonComponent);
        }
        navBtns.forEach(btn => {
            btn.classList.remove("text-black", "border-white", "rounded-full", "bg-blue-100");

        });
        navBtn.classList.add("text-black", "border-white", "rounded-full", "bg-blue-100");
    });
});

navBtns[0].click();