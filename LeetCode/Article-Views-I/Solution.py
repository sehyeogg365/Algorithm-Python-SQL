1import pandas as pd
2
3def article_views(views: pd.DataFrame) -> pd.DataFrame:
4    # 1. 저자 ID와 시청자 ID가 같은 경우만 필터링
5    new_df = views[views['author_id'] == views['viewer_id']]
6    # 2. 고유한 author_id만 추출합니다. unique 활용
7    unique_authors = new_df['author_id'].unique()
8
9    # 3. author_id'를 기준으로 그룹화 후 sort=True를 사용
10    result_df = pd.DataFrame({'id': unique_authors})
11
12    # 4. 'id' 컬럼을 기준으로 정렬합니다. (groupby 대신 sort_values 사용)
13    result_df = result_df.sort_values(by='id', ascending=True)
14    return result_df
15
16data = {
17        'article_id': [1, 1, 2, 2, 4, 3, 3],
18        'author_id': [3, 3, 7, 7, 7, 4, 4],
19        'viewer_id': [5, 6, 7, 6, 1, 4, 4],
20        'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21']
21    }
22
23views = pd.DataFrame(data) # 저자 ID 시청자 ID 같아야 함 
24
25
26result = article_views(views)
27
28print(result)