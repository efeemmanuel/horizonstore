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
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let btns = document.querySelectorAll(".product__item button")

btns.forEach(btn=>{
    btn.addEventListener("click", addToCart)
})

function addToCart(e){
    let details_id = e.target.value
    let url = "/add_to_cart"

    let data = {id:details_id}

    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        document.getElementById("num_of_items").innerHTML = data
        console.log(data)
    })
    .catch(error=>{
        console.log(error)
    })
}



let removeButtons = document.querySelectorAll(".remove-from-cart");

removeButtons.forEach(button => {
    button.addEventListener("click", removeFromCart);
});

function removeFromCart(e) {
    let itemId = e.target.value;
    let url = "/remove_from_cart";
    
    let data = { id: itemId };
    
    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        if (data.hasOwnProperty("num_of_items")) {
            document.getElementById("num_of_items").innerHTML = data.num_of_items;
            e.target.closest("tr").remove(); // Remove the table row from the DOM
        }
    })
    .catch(error => {
        console.log(error);
    });
}









// Increase quantity
function increaseQuantity(e) {
    let cartItemId = e.target.dataset.itemId;
    let url = "/increase_quantity";
    let data = { id: cartItemId };

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                // Update the displayed quantity
                let quantityElement = document.querySelector(`[data-quantity="${cartItemId}"]`);
                quantityElement.textContent = data.quantity;
            }
        })
        .catch(error => {
            console.log(error);
        });
}

// Reduce quantity
function reduceQuantity(e) {
    let cartItemId = e.target.dataset.itemId;
    let url = "/reduce_quantity";
    let data = { id: cartItemId };

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
        body: JSON.stringify(data)
    })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                // Update the displayed quantity
                let quantityElement = document.querySelector(`[data-quantity="${cartItemId}"]`);
                quantityElement.textContent = data.quantity;
            }
        })
        .catch(error => {
            console.log(error);
        });
}

// Attach event listeners to the buttons
let increaseBtns = document.querySelectorAll(".increase-quantity");
let reduceBtns = document.querySelectorAll(".reduce-quantity");

increaseBtns.forEach(btn => {
    btn.addEventListener("click", increaseQuantity);
});

reduceBtns.forEach(btn => {
    btn.addEventListener("click", reduceQuantity);
});
