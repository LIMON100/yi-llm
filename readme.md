# Yoga Instruction 

Generated yoga-instruction based on queries and expected duration from users.


### Folder Structure

    yi-llm/
    │   .gitignore
    │   app.py
    │   requirements.txt
    │   readme.md
    │
    ├───backend/
    │   │   readme.md
    │   │
    │   ├───app/
    │   │       __init__.py
    │   │       yllm.py
    │   │
    │   └───tests/
    │           __init__.py
    │           test_meditation.py
    │
    └───templates/
            index.html

### 
    app.py : run the app
    backend(folder)
        app(folder): yllm.py ( perform all necessary tasks for query and generated output)
        tests(folder): test_meditation.py (perform unit testing)

    templates(folder)
        index.html (Ui for take queries and show output)

#### Install necessary libraries
    pip install -r requirements.txt
#### For run the project
    update your openai key line 55 in app.py
    python app.py

![](https://github.com/LIMON100/yi-llm/blob/master/images/output_med.PNG?raw=true)

#### Unit-testing, go to backend folder and run below command
    python -m unittest discover -s tests -p "*.py"
