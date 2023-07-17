import streamlit as st
import pandas as pd
import altair as alt


#1「メニュー別データ.py」にdrinkの商品ごとの
# ラジオボタンと品別売上の棒グラフを表示する関数 drink_kindを定義し、
# チェックボックスが押されたら呼び出して表示できるようにしましょう。

#タイトル
st.markdown("#### ドリンクメニュー品別売上")
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
            key="test1")
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


#2「メニュー別データ.py」に、マルチセレクトを使って、
# 選択したドリンクメニューの売上数を折れ線グラフで表示するmultiselect_drinkを定義し、
# チェックボックスをチェックしたら呼び出して表示できるようにしてみましょう。



#タイトル
st.markdown("#### ドリンクメニュー売上数比較")
def select_drink_kind():
    #エクセルファイルの読み込み
    drink_data=pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                        engine="openpyxl", index_col=0)
    #行と列を入れ替える
    transposed_drinked_data=drink_data.transpose()
    #マルチセレクトの作成
    multiselect_drink_list=st.multiselect(
        "確認したいドリンクのメニューを選んでください（複数選択可）",
        transposed_drinked_data.columns.unique(),
        "生大"
        )
    st.write(transposed_drinked_data[multiselect_drink_list])
    if not multiselect_drink_list:
        st.error("表示するメニューが選択されていません")
    else:
        st.line_chart(transposed_drinked_data[multiselect_drink_list])

#ドリンクの月次売上
if st.checkbox("ドリンクの月次売上数比較"):
    select_drink_kind()
    
#タイトル
st.markdown("#### 肉類メニュー品別売上")
def meat_kind():
    #エクセルデータの読み込み
    meat_data = pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="meat", 
                                    engine="openpyxl", index_col=0)
    #行と列を入れ替える
    transposed_meat_data = meat_data.transpose()
    #3カラム作成
    col_1,col_2 = st.columns(2)
    with col_1:
        #ラジオボタンの作成
        selected_meat=st.radio("メニューを選んでください",
            transposed_meat_data.columns.unique(),
            key="test2")
    with col_2:
        #データフレームを作る
        data = pd.DataFrame({
            "営業月":transposed_meat_data.index.unique(),#月を取得
            "売上数":transposed_meat_data[selected_meat]
            })
        st.subheader(selected_meat)
        #棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('営業月',sort=None),
                    y='売上数',
                    ),
                    use_container_width=True)
#肉類の品別売上
if st.checkbox("肉類の品別売上"):
    meat_kind()


#タイトル
st.markdown("#### 肉類メニュー売上数比較")
def select_meat_kind():
    #エクセルファイルの読み込み
    meat_data=pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="meat", 
                                        engine="openpyxl", index_col=0)
    #行と列を入れ替える
    transposed_meat_data=meat_data.transpose()
    #マルチセレクトの作成
    multiselect_meat_list=st.multiselect(
        "確認したい肉類のメニューを選んでください（複数選択可）",
        transposed_meat_data.columns.unique(),
        "トモサンカク"
        )
    st.write(transposed_meat_data[multiselect_meat_list])
    if not multiselect_meat_list:
        st.error("表示するメニューが選択されていません")
    else:
        st.line_chart(transposed_meat_data[multiselect_meat_list])

#肉類の月次売上
if st.checkbox("肉類の月次売上数比較"):
    select_meat_kind()

#タイトル
st.markdown("#### サイドメニュー品別売上")
def sidemenu_kind():
    #エクセルデータの読み込み
    sidemenu_data = pd.read_excel(".//data/sales_data/2022sales_data.xlsx", sheet_name="sidemenu", 
                                    engine="openpyxl", index_col=0)
    #行と列を入れ替える
    transposed_sidemenu_data = sidemenu_data.transpose()
    #3カラム作成
    col_1,col_2 = st.columns(2)
    with col_1:
        #ラジオボタンの作成
        selected_sidemenu=st.radio("メニューを選んでください",
            transposed_sidemenu_data.columns.unique(),
            key="test3")
    with col_2:
        #データフレームを作る
        data = pd.DataFrame({
            "営業月":transposed_sidemenu_data.index.unique(),#月を取得
            "売上数":transposed_sidemenu_data[selected_sidemenu]
            })
        st.subheader(selected_sidemenu)
        #棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('営業月',sort=None),
                    y='売上数',
                    ),
                    use_container_width=True)
#ドリンクの品別売上
if st.checkbox("サイドメニューの品別売上"):
    sidemenu_kind()

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