def popUpGen(product):
    title = str(product['title'])
    title = title.lower()
    title = title.replace(" - ", "-")
    title = title.replace("  ", "-")
    title = title.replace(" ", "-")
    title = title.replace(",", "-")
    title = title.replace("/", "-")
    title = title.replace(". ", "")
    title = title.replace(".", "-")
    title = title.replace('-"', "-quot-")
    title = title.replace('"', "-quot")
    title = title.replace("'", "-39-")

    popUp = '// *[ @ id = "' + title + '"] / div[7] / div / div / div / button / img'

    return popUp



def UrlGen(product, size):
    baseUrl = 'https://packershoes.com/collections/'
    brand = product['vendor'].lower()
    productName = product['handle']
    sizeVariant = product['id']
    for variant in product['variants']:
        if(size == variant['option1']):
            sizeVariant = variant['id']
    finalUrl = baseUrl + brand + '/products/' + productName + '?variant=' + str(sizeVariant)
    return finalUrl