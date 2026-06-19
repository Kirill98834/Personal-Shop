def generate_cart_text(cart_items):
    '''Генерация текста о содержимом корзины'''
    if not cart_items:
        return "Корзина пуста🗑️"

    text = "Содержимое корзины:🧺\n"
    total = 0.0

    for item in cart_items:
        name = item.get("product_name", "Названия нет")
        quantity = item.get("quantity", 0)
        final_price = item.get("final_price", 0)

        total = float(final_price)
        text += f"{name}-{quantity}-{final_price}руб.\n"

    text += f"Итого: {total}руб."
    return text


