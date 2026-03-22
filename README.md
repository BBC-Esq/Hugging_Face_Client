# 🤗 Hugging Face Client

A PySide6 desktop application for managing your Hugging Face Hub account — repos, files, model cards, and collections — all from a single GUI.

---

<img width="1405" height="758" alt="image" src="https://github.com/user-attachments/assets/0552ba3f-77be-44cb-87f7-a505adffb412" />

## ✨ Features

| | Feature | Description |
|---|---|---|
| 🔐 | **Authentication** | Login with your HF access token; auto-detects cached tokens from `huggingface-cli login` |
| 📦 | **Repo Management** | Create, browse, delete, and toggle visibility of models, datasets, and spaces |
| ⭐ | **Favorites** | Mark repos as favorites and filter to show only your starred picks |
| 🔍 | **Live Search** | Filter repos instantly as you type with debounced live filtering; switch between Models, Datasets, and Spaces |
| 📂 | **File Browser** | Browse file trees, upload files/folders, download, edit text files, and delete — with commit messages and branch selection |
| 📁 | **Drag & Drop Upload** | Drag files from your file manager onto the file tree to upload — target folder is detected automatically |
| 📝 | **README / Model Card Editor** | View, edit, or generate model cards from a structured template with YAML frontmatter |
| 📚 | **Collections** | Create, browse, add/remove items, and delete Hugging Face collections |
| 🌿 | **Branch Support** | Switch branches when browsing; default branch detected automatically from repo refs |
| 🔄 | **Retry with Backoff** | API calls auto-retry on network errors and HTTP 5xx responses |
| 🪵 | **Logging** | Timestamped log files in `logs/` for diagnostics |
| 💾 | **Session Persistence** | Window size, position, splitter state, last repo type, favorites filter, and sort preferences remembered across sessions |

> [!NOTE]
> Text files over 10 MB are blocked from the built-in editor. You'll get guidance to download, edit locally, and re-upload instead.

---

## 🚀 Installation

```bash
pip install PySide6 huggingface_hub
```

Or using the requirements file:

```bash
pip install -r requirements.txt
```

---

## 🖥️ Usage

```bash
python main.py
```

1. Click **Login** and paste your Hugging Face access token (get one at https://huggingface.co/settings/tokens — you need a token with `write` scope).
2. Your repositories load automatically. Use the dropdown to switch between Models, Datasets, and Spaces.
3. Select a repo from the left panel to browse its files, view/edit its README, or manage collections.

---

## ⌨️ Keyboard Shortcuts & Interactions

| Action | What it does |
|---|---|
| **Double-click** a repo | Open it on Hugging Face Hub in your browser |
| **Double-click** a text file | Open it in the built-in editor |
| **Drag files** onto file tree | Upload files to the targeted folder with confirmation |
| **Right-click** a file | Context menu: edit, download, delete (multi-select for batch delete) |
| **Right-click** a repo | Add/remove from favorites |
| **Right-click** a collection | Add item, open in browser, or delete |
| **Right-click** a collection item | Remove it from the collection |
| **Click a column header** | Sort repos by name, visibility, downloads, likes, or modified date |
| **Type** in the search box | Live-filter repos as you type |

> [!IMPORTANT]
> All destructive actions (delete repo, delete files, delete collection) require confirmation.

---

## 📌 Notes

- Built on the [`huggingface_hub`](https://github.com/huggingface/huggingface_hub) Python library — all operations go through the official HF API
- Large file uploads use HF's built-in LFS support automatically
- Your token is stored via `QSettings` (OS-level settings storage)
- Log files are saved to `logs/` with automatic cleanup keeping the 10 most recent files
