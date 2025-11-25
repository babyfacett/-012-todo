import streamlit as st


def main() -> None:
    """A simple ToDo list application.

    Users can add tasks to a list, check tasks as completed, and clear completed
    tasks. The list of tasks is maintained in Streamlit's session state.
    """
    st.title("ToDo アプリ")
    st.write("やるべきタスクを追加・完了チェックできるミニアプリです。")

    # Initialize task list in session state
    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []  # Each task is a dict with 'title' and 'done'

    # Input for new task
    new_task = st.text_input("新しいタスクを入力してください")
    if st.button("タスクを追加", key="add_task"):
        task_title = new_task.strip()
        if task_title:
            st.session_state["tasks"].append({"title": task_title, "done": False})
            st.success(f"タスク '{task_title}' を追加しました。")
        else:
            st.warning("タスク内容を入力してください。")

    # Display tasks with checkboxes
    if st.session_state["tasks"]:
        st.subheader("タスクリスト")
        # Use a placeholder for dynamic content
        for idx, task in enumerate(st.session_state["tasks"]):
            # The checkbox toggles the 'done' status
            checked = st.checkbox(task["title"], value=task["done"], key=f"task_{idx}")
            st.session_state["tasks"][idx]["done"] = checked

        # Button to remove completed tasks
        if st.button("完了済みタスクを削除", key="remove_completed"):
            st.session_state["tasks"] = [task for task in st.session_state["tasks"] if not task["done"]]
            st.success("完了済みのタスクを削除しました。")
    else:
        st.info("現在登録されているタスクはありません。新しいタスクを追加してください。")


if __name__ == "__main__":
    main()