"""
12 ToDo アプリ
================

このアプリは、タスクを追加・完了チェック・完了済みタスクを削除できる簡単な ToDo アプリです。
セッション状態 (`st.session_state`) とコールバック関数を使ってタスクの追加や削除を管理し、
削除ボタンを押すと即座に完了済みタスクが消えるように `st.rerun()` を併用しています。
"""

import streamlit as st

# 初期化: セッション状態にタスク一覧がなければ空リストで作成
if "tasks" not in st.session_state:
    st.session_state.tasks = []


def add_task() -> None:
    """テキスト入力欄の内容をタスクとして追加し、その後入力をクリアします。"""
    task_title = st.session_state.new_task.strip()
    if task_title:
        st.session_state.tasks.append({"title": task_title, "done": False})
    # 入力欄をリセット
    st.session_state.new_task = ""


def toggle_task(idx: int) -> None:
    """指定したインデックスのタスクの完了状態を反転させます。"""
    st.session_state.tasks[idx]["done"] = not st.session_state.tasks[idx]["done"]


def remove_completed() -> None:
    """完了済みタスクを削除し、可能であれば即時再実行します。"""
    st.session_state.tasks = [task for task in st.session_state.tasks if not task["done"]]
    # 画面を即座に更新するために st.rerun() を試行
    try:
        st.rerun()
    except Exception:
        try:
            st.experimental_rerun()  # 古いバージョンの Streamlit 向け
        except Exception:
            pass


def main() -> None:
    st.title("ToDo アプリ")
    st.write("やるべきタスクを追加・完了チェックできるミニアプリです。")

    # タスク追加用入力欄: Enter キーで add_task を実行
    st.text_input(
        "新しいタスクを入力してください",
        key="new_task",
        on_change=add_task,
    )

    # 登録済みタスクの表示
    if st.session_state.tasks:
        st.subheader("タスクリスト")
        for idx, task in enumerate(st.session_state.tasks):
            # チェックボックスで完了状態を切り替え
            st.checkbox(
                task["title"],
                value=task["done"],
                key=f"task_{idx}",
                on_change=toggle_task,
                args=(idx,),
            )
        # 完了済みタスクの削除ボタン
        st.button("完了済みタスクを削除", on_click=remove_completed)
    else:
        st.info("現在登録されているタスクはありません。新しいタスクを追加してください。")


if __name__ == "__main__":
    main()
