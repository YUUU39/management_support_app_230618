import streamlit as st
import pandas as pd
import altair as alt
"""
#### monthly_drink_sales()関数を作り、チェックボックスで呼び出す。
"""

def monthly_drink_sales():
    #エクセルデータの読み込み
    drink_data = pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                drink_data.columns.values.tolist(),
                                key="drink")
    #読み込んだエクセルデータを辞書型に変更
    drink_data_dict = drink_data.to_dict()
    #辞書に変換されたドリンクのデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": drink_data_dict[select_month].keys(),
                        "数量": drink_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}のドリンク販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:     
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)


#肉類の月別売上
def monthly_meat_sales():
    #エクセルデータの読み込み
    meat_data = pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="meat", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                meat_data.columns.values,
                                key=2)
    #読み込んだエクセルデータを辞書型に変更
    meat_data_dict = meat_data.to_dict()
    #辞書に変換された肉のデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": meat_data_dict[select_month].keys(),
                        "数量": meat_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}の肉類販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)

#サイドメニューの月別売上
def monthly_sidemenu_sales():
    #エクセルデータの読み込み
    sidemenu_data = pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="sidemenu", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                sidemenu_data.columns.values,
                                key=3)
    #読み込んだエクセルデータを辞書型に変更
    sidemenu_data_dict = sidemenu_data.to_dict()
    #辞書に変換された肉のデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": sidemenu_data_dict[select_month].keys(),
                        "数量": sidemenu_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}のサイドメニューの販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)

#タイトル
st.markdown("### 月次データ")

#ドリンクの月別売上チェックボックス
if st.checkbox("ドリンク"):
    monthly_drink_sales()
    
#肉類の月別売上チェックボックス
if st.checkbox("肉類"):
    monthly_meat_sales()
    
#サイドメニューの月別売上チェックボックス
if st.checkbox("サイドメニュー"):
    monthly_sidemenu_sales()

#コメント
with st.form(key='monthly_sales_comment'):
    #textbox
    comment = st.text_input("コメントを記入してください")
    submit_btn = st.form_submit_button("登録")
    if submit_btn: #ボタンをクリックしたらコメントを登録する。
        with open(".//data/sales_data/sales_kind_comment.txt","a",encoding='shift_jis') as f:
            f.write(f"{comment}")
    with open(".//data/sales_data/sales_kind_comment.txt","r",encoding='shift_jis') as f:
        sales_comment = f.read()
        sales_comment
st.markdown(":red[今回は練習用にデータベースの代わりにtxtファイルを使用しています]")
st.markdown(":red[また今回はコメント登録後の取り消し機能も実装していません]")
st.markdown(":red[monthly_sales_comment.txtを直接編集することは可能です。]")

"""
#### drinkの商品ごとのラジオボタンと品別売上の棒グラフを作成。
"""
#エクセルデータの読み込み
drink_data=pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                    engine="openpyxl", index_col=0)
#行と列を入れ替える
transposed_drinked_data=drink_data.transpose()
#2カラム作成
col_1,col_2=st.columns(2)
with col_1:
    #ラジオボタンの作成
    selected_drink=st.radio("メニューを選んでください",
                            transposed_drinked_data.columns.unique(),
                            key=4)
with col_2:
    #データフレームを作る
    data=pd.DataFrame({
        "営業月":transposed_drinked_data.index.unique(),
        "売上数":transposed_drinked_data[selected_drink]
    })
    st.subheader(selected_drink)
    #棒グラフの描画
    st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('営業月',sort=None),
            y='売上数',
            ),
            use_container_width=True)

"""
#### transposed_drink_dataの中身の確認
"""
transposed_drinked_data #マジックコマンド
"""
#### ドリンクメニューのラジオボタンの確認
"""
selected_drink=st.radio("メニューを選んでください",
                        transposed_drinked_data.columns.unique(),
                        key="test5")
selected_drink #マジックコマンド

"""
#### transposed_drink_data.columns.unique()の中身
"""
st.write(transposed_drinked_data.columns.unique())
"""
#### ラジオボタンで選択された商品の売上数が出力されるか確認
"""
col_1,col_2 = st.columns(2)
with col_1:
    #ラジオボタンの作成
    selected_drink=st.radio("メニューを選んでください",
                            transposed_drinked_data.columns.unique(),
                            key="test6")
with col_2:
    st.write(transposed_drinked_data[selected_drink])
"""
#### ラジオボタンで選択された商品の売上数が棒グラフで出力されるか確認
"""
col_1,col_2 = st.columns(2)
with col_1:
    #ラジオボタンの作成
    selected_drink=st.radio("メニューを選んでください",
                            transposed_drinked_data.columns.unique(),
                            key="test7")
with col_2:
    data=pd.DataFrame({
            "営業月":transposed_drinked_data.index.unique(),
            "売上数":transposed_drinked_data[selected_drink]
            })
    st.subheader(selected_drink)
    #棒グラフの描写
    st.altair_chart(alt.Chart(data).mark_bar().encode(
        x=alt.X('営業月',sort=None),
        y='売上数',
        ),
        use_container_width=True)
"""
↑ 問18冒頭と同じ
"""
#問１９　以下の説明と画像を見ながら、dev.pyにdrinkの商品ごとのラジオボタンと品別売上の棒グラフを表示する関数 drink_kindを定義し、
#チェックボックスが押されたら呼び出して表示できるようにしましょう。
"""
#### チェックボックスにチェックを入れると、ラジオボタンで選択された商品の売上数が棒グラフで出力されるか確認
"""
def drink_kind():
    #エクセルデータの読み込み
    drink_data = pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                    engine="openpyxl", index_col=0)
    #行と列を入れ替える
    transposed_drink_data = drink_data.transpose()
    #3カラム作成
    col_1,col_2 = st.columns(2)
    with col_1:
        #ラジオボタンの作成
        selected_drink=st.radio("メニューを選んでください",
            transposed_drink_data.columns.unique(),
            key="test8")
    with col_2:
        #データフレームを作る
        data = pd.DataFrame({
            "営業月":transposed_drink_data.index.unique(),#月を取得
            "売上数":transposed_drink_data[selected_drink]
            })
    st.subheader(selected_drink)
    #棒グラフの描画
    st.altair_chart(alt.Chart(data).mark_bar().encode(
                x=alt.X('営業月',sort=None),
                y='売上数',
                ),
                use_container_width=True)
#ドリンクの品別売上
if st.checkbox("ドリンクの品別売上"):
    drink_kind()

# 問２０　以下の説明と画像を見ながら、dev.pyにマルチセレクトを使って、
# 選択したドリンクメニューの売上数を折れ線グラフで表示してみましょう。

"""
#### マルチセレクトを使って、選択したドリンクメニューの売上数を折れ線グラフで確認
"""
#タイトル
st.markdown("#### ドリンクメニュー売上数比較")
#エクセルファイルの読み込み
drink_data=pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                    engine="openpyxl", index_col=0)
#行と列を入れ替える
transposed_drinked_data=drink_data.transpose()
#マルチセレクトの作成
multiselected_drink_list=st.multiselect(
    "確認したいドリンクのメニューを選んでください（複数選択可）",
    transposed_drinked_data.columns.unique(),
    "生大"
    )
st.write(transposed_drinked_data[multiselected_drink_list])
if not multiselected_drink_list:
    st.error("表示するメニューが選択されていません")
else:
    st.line_chart(transposed_drinked_data[multiselected_drink_list])

