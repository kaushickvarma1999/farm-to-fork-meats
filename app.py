from flask import Flask
app = Flask(__name__)

@app.route('/')
def show_items():
    items = [
        ("Chicken (1lb)", 3.99, "fa-solid fa-drumstick-bite"),
        ("Goat (1lb)", 7.99, "fa-solid fa-deer"),
        ("Live Goat (1lb)", 9.99, "fa-solid fa-deer"),
        ("Eggs (1 Dozen)", 5.99, "fa-solid fa-egg"),
        ("Milk (1 Gallon)", 5.99, "fa-solid fa-mug-saucer"),
        ("Honey (Half kg)", 17.99, "fa-solid fa-jar"),
        ("Beef (1lb)", 7.99, "fa-solid fa-cow")
    ]

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="Farm-fresh meat delivered to your door. Chicken, goat, eggs, milk & more in Pittsburgh. Order via phone or WhatsApp." />
        <title>Farm to Fork Meats</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" />
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            html, body { height: 100%; background-color: #000; font-family: Arial, sans-serif; }
            body { display: flex; flex-direction: column; min-height: 100vh; }
            .container {
                background-color: #1C2526;
                color: #FFF;
                padding: 20px;
                flex: 1;
                display: flex;
                flex-direction: column;
            }
            h1 { font-size: 36px; text-align: center; color: #FFD700; }
            h2 { font-size: 24px; margin-top: 20px; text-align: center; }
            p.subtitle { text-align: center; font-size: 18px; margin-bottom: 20px; color: #D3D3D3; }
            ul {
                list-style: none;
                padding: 0;
                margin: 0 auto 20px;
                max-width: 600px;
                width: 100%;
            }
            li {
                font-size: 18px;
                margin: 10px 0;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .item-container { display: flex; align-items: center; flex: 1; }
            .item-name { flex: 1; }
            .item-price { width: 100px; text-align: right; }
            li i { margin-right: 10px; color: #FFD700; font-size: 22px; }

            .meat-image {
                display: block;
                max-width: 80%;
                margin: 20px auto;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(255,255,255,0.2);
            }

            .bottom-section { margin-top: auto; text-align: center; }
            .contact {
                font-size: 20px;
                margin-top: 20px;
            }
            .contact a {
                color: #FFD700;
                text-decoration: none;
                margin: 0 10px;
            }
            .contact i {
                margin-left: 5px;
                font-size: 28px;
                color: #FFD700;
                animation: giggle 1s infinite ease-in-out;
                display: inline-block;
            }

            .note {
                font-size: 14px;
                font-style: italic;
                margin: 10px 0;
                color: #D3D3D3;
            }

            .cta-btn {
                display: inline-block;
                margin-top: 10px;
                background-color: #FFD700;
                color: #1C2526;
                padding: 10px 20px;
                border-radius: 8px;
                font-weight: bold;
                text-decoration: none;
                transition: all 0.3s ease;
            }

            .cta-btn:hover {
                background-color: #ffcc00;
            }

            .float-whatsapp {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background: #25D366;
                color: white;
                padding: 12px;
                border-radius: 50%;
                font-size: 28px;
                z-index: 1000;
                animation: pulse 2s infinite;
            }

            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.15); }
                100% { transform: scale(1); }
            }

            @keyframes giggle {
                0%, 100% { transform: rotate(0deg); }
                25% { transform: rotate(15deg); }
                50% { transform: rotate(-15deg); }
                75% { transform: rotate(10deg); }
            }

            @media (max-width: 600px) {
                h1 { font-size: 26px; }
                h2 { font-size: 20px; }
                li { font-size: 16px; flex-wrap: wrap; }
                .item-price { width: 80px; }
                .meat-image { max-width: 90%; }
                .contact { font-size: 18px; }
                .note { font-size: 13px; }
                .contact i { font-size: 32px; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Farm to Fork Meats</h1>
            <p class="subtitle">Fresh, Farm-Sourced Meat Delivered to Your Doorstep</p>
            <h2>Our Fresh Meat & Products</h2>
            <ul>
    """

    for item, price, icon in items:
        html += f'<li><div class="item-container"><i class="{icon}"></i><span class="item-name">{item}</span></div><span class="item-price">${price:.2f}</span></li>'

    html += """
            </ul>
            <img src="/static/images/meat_products.jpg" alt="Meat Products" class="meat-image">
            <div class="bottom-section">
                <p class="contact">
                    Call or Text 
                    <a href="tel:+14129908956"><i class="fa-solid fa-phone"></i></a> | 
                    <a href="https://wa.me/14129908956"><i class="fa-brands fa-whatsapp"></i></a>
                </p>
                <a href="https://wa.me/14129908956" class="cta-btn">Order Now on WhatsApp</a>
                <p class="note">We deliver across Pittsburgh & surrounding areas.<br>Minimum 5 lbs to order – Delivery charges apply</p>
            </div>
        </div>

        <!-- Floating WhatsApp Button -->
        <a href="https://wa.me/14129908956" class="float-whatsapp" target="_blank">
            <i class="fa-brands fa-whatsapp"></i>
        </a>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
