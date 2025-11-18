import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # 저지방이면서 재활용이 가능한 제품의 ID를 찾는 솔루션을 작성하세요.
    filtered_products = products.loc[
        (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    ]

    return filtered_products[['product_id']]

data = {
    'product_id' : [0, 1, 2, 3, 4],
    'low_fats' : ['Y', 'Y', 'N', 'Y', 'N'],
    'recyclable' : ['N', 'Y', 'Y', 'N', 'N']
}

df = pd.DataFrame(data)

result = find_products(df)
print(result)