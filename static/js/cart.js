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
const csrftoken = getCookie('csrftoken');

document.querySelectorAll(".product__item button").forEach(btn => {
    btn.addEventListener("click", addToCart);
});

function addToCart(e) {
    let details_id = e.target.value;
    let url = "/add_to_cart";
    let data = { id: details_id };

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("num_of_items").textContent = data.num_of_items;
        updateCartSummary(data.total_price);
    })
    .catch(error => {
        console.log(error);
    });
}

document.querySelectorAll(".remove-from-cart").forEach(button => {
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
        if (data.num_of_items !== undefined) {
            document.getElementById("num_of_items").textContent = data.num_of_items;
            e.target.closest("tr").remove();
            updateCartTotal();
            updateCartSummary(data.total_price);
        }
    })
    .catch(error => {
        console.log(error);
    });
}

document.querySelectorAll(".increase-quantity").forEach(btn => {
    btn.addEventListener("click", increaseQuantity);
});

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
            let quantityElement = document.querySelector(`[data-quantity="${cartItemId}"]`);
            quantityElement.value = data.quantity;
            updateItemTotal(cartItemId, data.quantity);
            updateCartTotal();
            updateCartSummary(data.total_price);
        }
    })
    .catch(error => {
        console.log(error);
    });
}

document.querySelectorAll(".reduce-quantity").forEach(btn => {
    btn.addEventListener("click", reduceQuantity);
});

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
            let quantityElement = document.querySelector(`[data-quantity="${cartItemId}"]`);
            quantityElement.value = data.quantity;
            updateItemTotal(cartItemId, data.quantity);
            updateCartTotal();
            updateCartSummary(data.total_price);
        }
    })
    .catch(error => {
        console.log(error);
    });
}

function updateItemTotal(cartItemId, quantity) {
    let priceElement = document.querySelector(`[data-price="${cartItemId}"]`);
    let price = parseFloat(priceElement.textContent.replace('$', ''));
    let totalElement = document.querySelector(`[data-total="${cartItemId}"]`);
    totalElement.textContent = `$${(price * quantity).toFixed(2)}`;
}

function updateCartTotal() {
    let total = 0;
    document.querySelectorAll(".shoping__cart__total").forEach(totalElement => {
        total += parseFloat(totalElement.textContent.replace('$', ''));
    });
    document.querySelector(".shoping__checkout ul li span").textContent = `$${total.toFixed(2)}`;
}

function updateCartSummary(total_price) {
    document.querySelector("li.total span").textContent = `$${total_price.toFixed(2)}`;
    document.getElementById("num_of_items").textContent = total_price.num_of_items;
}











