# Agriculture Information System

## Important: original code preserved

Your original 113-line program has been split into two logical modules.
The original crop data block (lines 1–58) is copied into `data/crop_data.py`.
The original functions and main program block (lines 59–113) are copied
verbatim into `app/application.py`.

The only additions are the imports at the top of `app/application.py` and
the small root `main.py` launcher. No crop names, descriptions, prompts,
loops, conditions, function bodies, or original logic have been rewritten.

## Folder structure

```text
Agriculture-Information-System-Original-Code/
├── main.py
├── app/
│   ├── __init__.py
│   └── application.py
├── data/
│   ├── __init__.py
│   └── crop_data.py
└── README.md
```

## Open and run in VS Code

1. Extract this ZIP file.
2. In VS Code choose **File → Open Folder** and select this project folder.
3. Open the integrated terminal (**Terminal → New Terminal**).
4. Run:

```bash
python main.py
```

Run from the project root (the folder containing `main.py`).

## Why this version is deliberately simple

You asked to keep the code exactly as you supplied it. Moving the data and
functions into separate files requires imports, but rewriting the loops,
prompts, conditions, or data structures would change your original program.
This version therefore uses a small two-layer arrangement while preserving
the original code. We can introduce models, services, repositories, and a
database gradually when you approve changes to the original logic.
