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
    <html>
    <head>
        <title>Farm to Fork Meats</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            html, body {
                height: 100%;
                background-color: #000000;
                font-family: Arial, sans-serif;
            }
            body {
                display: flex;
                flex-direction: column;
            }
            .container {
                background-color: #1C2526;
                color: #FFFFFF;
                padding: 20px;
                flex: 1;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
            }
            h1 {
                font-size: 36px;
                margin-bottom: 10px;
                text-align: center;
                color: #FFD700;
            }
            h2 {
                font-size: 24px;
                margin-top: 20px;
                text-align: center;
                color: #FFFFFF;
            }
            p.subtitle {
                text-align: center;
                font-size: 18px;
                margin-bottom: 20px;
                color: #D3D3D3;
            }
            ul {
                list-style-type: none;
                padding: 0;
                margin: 0 auto 20px auto;
                max-width: 600px;
                width: 100%;
            }
            li {
                font-size: 18px;
                margin: 10px 0;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .item-container {
                display: flex;
                align-items: center;
                flex: 1;
            }
            .item-name {
                flex: 1;
            }
            .item-price {
                width: 100px;
                text-align: right;
            }
            li i {
                margin-right: 10px;
                color: #FFD700;
                font-size: 20px;
            }
            .contact {
                font-size: 20px;
                margin-top: 20px;
                text-align: center;
            }
            .contact a {
                color: #FFD700;
                text-decoration: none;
                margin: 0 10px;
            }
            .contact a:hover {
                text-decoration: underline;
            }
            .contact i {
                margin-left: 5px;
                color: #FFD700;
                font-size: 20px;
            }
            .note {
                font-size: 14px;
                font-style: italic;
                text-align: center;
                margin-top: 10px;
                margin-bottom: 0;
                color: #D3D3D3;
            }
            .meat-image {
                display: block;
                max-width: 80%;
                height: auto;
                margin: 20px auto;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(255,255,255,0.2);
            }
            @media (max-width: 600px) {
                h1 {
                    font-size: 26px;
                }
                h2 {
                    font-size: 20px;
                }
                p.subtitle {
                    font-size: 16px;
                }
                li {
                    font-size: 16px;
                    flex-wrap: wrap;
                }
                .item-price {
                    width: 80px;
                }
                .meat-image {
                    max-width: 90%;
                }
                .contact {
                    font-size: 18px;
                }
                .note {
                    font-size: 13px;
                }
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
            <p class="contact">
                Call or Text <a href="tel:+14129908956"><i class="fa-solid fa-phone"></i></a> | 
                <a href="https://wa.me/14129908956"><i class="fa-brands fa-whatsapp"></i></a>
            </p>
            <p class="note">Minimum 5 lbs to order - Delivery charges apply</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
