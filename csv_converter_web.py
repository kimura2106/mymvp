#!/usr/bin/env python
# coding: utf-8

# In[23]:


import streamlit as st
import pandas as pd
import io
import os

def convert_csv(file, original_filename):
    """
    CSVファイルを変換する関数
    """
    df = pd.read_csv(file, encoding="utf-8-sig")
    
    # カラム名の変換
    df = df.rename(columns={
        'Marker': 'NowTask',
        '[1]Signal Quality': 'SQ',
        '[1]delta': 'Delta',
        '[1]theta': 'Theta',
        '[1]alpha1': 'Alpha1',
        '[1]alpha2': 'Alpha2',
        '[1]beta1': 'Beta1',
        '[1]beta2': 'Beta2',
        '[1]gamma': 'Gamma1'
    })
    df['Gamma2'] = 0
    
    # 必要なカラムリストを明示的に定義
    columns_to_keep = ['Time', 'SQ', 'NowTask', 'Delta', 'Theta', 'Alpha1', 'Alpha2', 'Beta1', 'Beta2', 'Gamma1', 'Gamma2']

    # データフレームに存在するカラムのみ抽出
    existing_columns = [col for col in columns_to_keep if col in df.columns]

    # 指定された順序でカラムを並び替え
    df = df[existing_columns]

    return df, original_filename

# Streamlit アプリの設定
st.title("変換くん - CSV変換ツール")

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    original_filename = os.path.splitext(uploaded_file.name)[0]  # 拡張子を除いたファイル名を取得
    df_converted, filename = convert_csv(uploaded_file, original_filename)
    
    st.write("変換後のデータ:")
    st.dataframe(df_converted)
    
    # 変換後のCSVをダウンロードできるようにする
    csv = df_converted.to_csv(index=False, encoding="utf-8-sig")
    new_filename = f"{filename}_ios2w.csv"
    st.download_button(
        label="変換後のCSVをダウンロード",
        data=csv,
        file_name=new_filename,
        mime="text/csv"
    )


# In[ ]:




