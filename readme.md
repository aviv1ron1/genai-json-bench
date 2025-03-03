<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">IBM-JSON</h1></p>
<p align="center">
	<em>Unleash JSON magic, simplify data handling!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/urilevy77/IBM-JSON?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/urilevy77/IBM-JSON?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/urilevy77/IBM-JSON?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/urilevy77/IBM-JSON?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

IBM-JSON simplifies JSON data management by offering a streamlined solution to organize, validate, and generate JSON structures effortlessly. With features like schema validation, error handling, and user-friendly prompts, it caters to developers seeking efficient JSON handling for diverse projects. Ideal for ensuring data integrity and enhancing workflow efficiency.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Centralizes data management using `data_store.py` to organize JSON data for processing and analysis.</li><li>Defines project constants and paths in `config.py` for essential functionality and data management.</li><li>Generates JSON structures, instances, and errors based on predefined prompts and themes in `generators.py`.</li><li>Implements a configurable schema for organizing data with various structures in `story_structures.txt`.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Validates JSON schemas and instances against the Draft 7 standard in `validation.py`.</li><li>Facilitates language model integration and community contributions through `requirements.txt`.</li><li>Utilizes a Hugging Face chat model for structured JSON generation in `generators.py`.</li><li>Detects and reports data validation errors in `errors.txt` for maintaining content integrity.</li></ul> |
| 📄 | **Documentation** | <ul><li>Provides prompts for JSON schema generation, error handling, and user queries in `prompts.py`.</li><li>Generates JSON schemas, instances, and errors based on defined rules in `prompts.yaml`.</li><li>Facilitates testing and debugging of JSON functionalities in `main.py`.</li><li>Manages dependencies for the project in `requirements.txt`.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with Hugging Face API model and data files through `config.py`.</li><li>Utilizes `langchain-huggingface` for language model integration.</li><li>Supports `python-dotenv` for environment variable management.</li><li>Facilitates testing with `pytest`.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Modularizes data storage and organization in `data_store.py`.</li><li>Separates project constants and paths in `config.py` for easy management.</li><li>Encapsulates prompts and themes for JSON generation in `prompts.py` and `prompts.yaml`.</li><li>Provides modular content categorization in `themes.txt`.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Supports testing with `pytest` for validating JSON functionalities.</li><li>Validates JSON schemas and instances against the Draft 7 standard in `validation.py`.</li><li>Facilitates error detection and reporting in `errors.txt` for maintaining data integrity.</li><li>Generates structured JSON outputs for testing in `generators.py`.</li></ul> |

---

##  Project Structure

```sh
└── IBM-JSON/
    ├── config.py
    ├── content_idea_files
    │   ├── errors.txt
    │   ├── story_structures.txt
    │   └── themes.txt
    ├── data_store.py
    ├── generators.py
    ├── main.py
    ├── prompts.py
    ├── prompts.yaml
    ├── requirements.txt
    └── validation.py
```


###  Project Index
<details open>
	<summary><b><code>IBM-JSON/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/data_store.py'>data_store.py</a></b></td>
				<td>- The `data_store.py` file provides a function to save JSON details into global arrays<br>- It stores dictionaries containing schema, JSON instances, erroneous JSON, and error descriptions<br>- This functionality supports the project's architecture by managing and organizing JSON data for further processing and analysis.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/config.py'>config.py</a></b></td>
				<td>- Define project constants and paths for the Hugging Face API model and data files<br>- The config file centralizes key identifiers and file paths essential for the project's functionality and data management.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>Facilitates language model integration and community contributions by managing dependencies for the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/prompts.py'>prompts.py</a></b></td>
				<td>- The prompts.py file defines various prompts used by the system for generating JSON schemas, instances, errors, and user queries<br>- It encapsulates human and system prompts for tasks like schema generation, error introduction, and user query simulation<br>- These prompts guide users in creating valid JSON structures and instances while handling errors effectively within the system.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/generators.py'>generators.py</a></b></td>
				<td>- Generates JSON schemas, instances, and error scenarios based on predefined prompts and themes<br>- Utilizes a Hugging Face chat model to create structured outputs for JSON generation and error handling<br>- Provides a comprehensive approach for fixing JSON errors and generating descriptive outputs.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/prompts.yaml'>prompts.yaml</a></b></td>
				<td>- Generates JSON schemas, instances, and errors based on defined rules and structures<br>- Ensures strict adherence to schema specifications, including types, constraints, and formats<br>- Facilitates error introduction in JSON instances while maintaining overall structure integrity<br>- Simulates user queries for JSON file assistance and provides corrections with concise descriptions.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/main.py'>main.py</a></b></td>
				<td>- Generates JSON schemas, instances, errors, user inputs, and model outputs based on predefined structures, themes, and validations<br>- Handles schema and JSON validation, error generation, and logging user interactions<br>- Facilitates testing and debugging of JSON-related functionalities within the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/validation.py'>validation.py</a></b></td>
				<td>- Validates JSON schemas and instances against the Draft 7 standard<br>- Parses JSON strings into dictionaries and checks for schema conformity<br>- Returns true if valid, false otherwise.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- content_idea_files Submodule -->
		<summary><b>content_idea_files</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/content_idea_files/errors.txt'>errors.txt</a></b></td>
				<td>- Detects and reports various data validation errors within the project's content files<br>- Handles issues such as missing fields, incorrect data types, and formatting errors<br>- Ensures data integrity and consistency by identifying and flagging discrepancies in the content structure.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/content_idea_files/themes.txt'>themes.txt</a></b></td>
				<td>Identifies themes for content categorization across diverse topics in the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/urilevy77/IBM-JSON/blob/master/content_idea_files/story_structures.txt'>story_structures.txt</a></b></td>
				<td>- Implements a configurable schema for organizing data with various structures like flat lists, nested objects, and key-value pairs<br>- Enables dynamic definition of fields and constraints at runtime, enhancing flexibility and adaptability in data management within the codebase architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with IBM-JSON, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install IBM-JSON using one of the following methods:

**Build from source:**

1. Clone the IBM-JSON repository:
```sh
❯ git clone https://github.com/urilevy77/IBM-JSON
```

2. Navigate to the project directory:
```sh
❯ cd IBM-JSON
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run IBM-JSON using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/urilevy77/IBM-JSON/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/urilevy77/IBM-JSON/issues)**: Submit bugs found or log feature requests for the `IBM-JSON` project.
- **💡 [Submit Pull Requests](https://github.com/urilevy77/IBM-JSON/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/urilevy77/IBM-JSON
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/urilevy77/IBM-JSON/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=urilevy77/IBM-JSON">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
