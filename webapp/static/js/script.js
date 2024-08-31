async function makeRequest(url, method = "GET") {
    let csrfToken = await getCookie('csrftoken');
    let headers = {
        'Content-Type': 'application/json'
    };
    if (method !== "GET") {
        headers['X-CSRFToken'] = csrfToken;
    }

    let response = await fetch(url, {
        method: method,
        headers: headers,
    });

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(await response.text());
        console.log(error);
        throw error;
    }
}

async function onClick(event) {
    event.preventDefault();
    let button = event.currentTarget;
    let url = button.dataset.url;
    let isFavorite = button.classList.contains('favorite');

    let method = isFavorite ? "DELETE" : "POST";

    try {
        let response = await makeRequest(url, method);

        if (isFavorite) {
            button.classList.remove('favorite');
            button.innerText = 'Add to favorites';
        } else {
            button.classList.add('favorite');
            button.innerText = 'Remove from favorites';
        }


    } catch (error) {
        console.error("Error updating favorites:", error);
    }
}

function onLoad() {
    let buttons = document.querySelectorAll('[data-like="favorite"]');
    for (let button of buttons) {
        button.addEventListener("click", onClick);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

window.addEventListener("load", onLoad);
