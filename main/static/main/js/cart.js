function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log(cookieValue)
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

let buttons = document.querySelectorAll(".delete-button")

buttons.forEach(button => {
    button.addEventListener("click", removeFromCart)
})

function removeFromCart(e) {
    let product_id = buttons.value
    console.log(product_id)
    let url = "/remove_from_cart"
    let data = {id: product_id}

    fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.log(error)
        })
}