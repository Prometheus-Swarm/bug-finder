"""Prompts for the repository summarization workflow."""

PROMPTS = {
    "system_prompt": (
        "You are an expert software engineer and technical lead specializing in identifying bugs in software repositories. "
        "You possess deep knowledge of common programming bugs and anti-patterns across various languages and frameworks. "
        "You excel at analyzing codebases to pinpoint potential issues, explain their root causes, and document them clearly for developers to resolve."
    ),
    "create_branch": (
        "You need to create a feature branch for the README that highlights the potential bugs and antipattern in the repository.\n"
        "Create a new branch with a descriptive name related to creating a README file.\n"
    ),
    "classify_repository": (
        "A repository has been cloned locally for you. All files can be accessed relative to the current directory.\n"
        "Analyze the structure and identify the type of repository this is.\n"
        "Use the `classify_repository` tool to report your choice.\n"
        "You must choose one of the following repository types:\n"
        "- Library/SDK: Code meant to be imported and used by other developers\n"
        "- Web App: Frontend or full-stack web application\n"
        "- API Service: Server-side application providing APIs\n"
        "- Mobile App: Native or cross-platform mobile app\n"
        "- Tutorial: Educational repository demonstrating techniques\n"
        "- Template: Starter code for new projects\n"
        "- CLI Tool: Command-line interface application\n"
        "- Framework: Foundational structure for building applications\n"
        "- Data Science: Machine learning or data analysis project\n"
        "- Plugin: Extension or module for a larger system (e.g., CMS, IDE, platform)\n"
        "- Chrome Extension: Browser extension targeting the Chrome platform\n"
        "- Jupyter Notebook: Interactive code notebooks, often for demos or research\n"
        "- Infrastructure: Configuration or automation code (e.g., Docker, Terraform)\n"
        "- Smart Contract: Blockchain smart contracts, typically written in Solidity, Rust, etc.\n"
        "- DApp: Decentralized application with both smart contract and frontend components\n"
        "- Game: Codebase for a game or game engine (2D, 3D, or browser-based)\n"
        "- Desktop App: GUI application for desktop environments (e.g., Electron, Qt, Tauri)\n"
        "- Dataset: Repository containing structured data for analysis or training\n"
        "- Other: If it doesn't fit into any of the above categories\n"
        "IMPORTANT: Do not assume that the README is correct. "
        "Classify the repository based on the codebase.\n"
        "If files are mentioned in the README but are not present in the codebase, "
        "do NOT use them as a source of information.\n"
    ),
    "generate_readme_section": (
        "You are writing the {section_name} section of a README file for a repository.\n"
        "The repository has been cloned to the current directory and the files are available for inspection.\n"
        "The readme will contain the following sections:\n"
        "{all_sections}\n"
        "Restrict your documentation to the section you are writing.\n"
        "Read all files relevant to your task and generate comprehensive, clear documentation.\n"
        "The section should include the following information:\n"
        "{section_description}\n"
        "Write the section in markdown format.\n"
        "The section name will be automatically added as a second level heading. "
        "DO NOT include it in your documentation. DO NOT include any second level headings.\n"
        "Any sub-sections you would like to add should be THIRD level headings or LOWER. "
        "Follow the proper hierarchy when choosing a heading level.\n"
        "IMPORTANT: DO NOT assume that any existing documentation is correct. It may be inaccurate or outdated.\n"
        "Create the documentation based SOLELY on the files actually present in the codebase.\n"
        "EXTREMELY IMPORTANT: If files are mentioned in the README but are not present in the codebase, "
        "do NOT mention them in your documentation. They do not exist and are not relevant.\n"
        "This is a public facing document, so DO NOTinclude any instructions or suggestions to the developer.\n"
    ),
    "generate_issues_readme": (
        "Create a descriptive title for the following README contents and create the README file:\n"
        "{readme_content}\n"
        "The content will be added automatically, your job is just to create a good title."
    ),
    "create_pr": (
        "You are creating a pull request for the file README_Prometheus.md you have generated. "
        "The repository has been cloned to the current directory.\n"
        "Use the `create_pull_request_legacy` tool to create the pull request.\n"
        "IMPORTANT: Always use relative paths (e.g., 'src/file.py' not '/src/file.py')\n\n"
        "Steps to create the pull request:\n"
        "1. First examine the available files to understand the implementation\n"
        "2. Create a clear and descriptive PR title\n"
        "3. Write a comprehensive PR description that includes:\n"
        "   - Description of all changes made\n"
        "   - The main features and value of the documentation\n"
    ),
    "review_readme_file": (
        "Review the README_Prometheus.md in the repository and evaluate its quality and "
        "relevance to the repository.\n\n"
        "Please analyze:\n"
        "1. Is the README_Prometheus.md file related to this specific repository? (Does it describe the actual code "
        "and purpose of this repo?)\n"
        "2. Does it correctly explain the repository's purpose, features, and functionality?\n"
        "3. Is it comprehensive enough to help users understand and use the repository?\n"
        "4. Does it follow best practices for README documentation?\n\n"
        "Use the `review_readme_file` tool to submit your findings.\n"
        "IMPORTANT: Do not assume that an existing README is correct. "
        "Evaluate README_Prometheus.md against the codebase.\n"
        "DO NOT consider the filename in your analysis, only the content.\n"
        "STOP after submitting the review report."
    ),
    "previous_review_comments": (
        "Here are the comments from the previous review:\n"
    ),
    "identity_repo_type": (
        """
        You are analyzing a software repository to identify its type and characteristics.
        Explore the directory structure and relevant files (e.g., `package.json`, `requirements.txt`, `Dockerfile`, `setup.py`, `pyproject.toml`, etc.). Your goal is to extract the following information:
        - Primary programming language(s)
        - Frameworks/libraries used
        - Type of project (e.g., CLI tool, REST API backend, web frontend, data pipeline, etc.)
        - Any patterns or architectural styles (e.g., microservices, monolith, layered architecture)

        Output a structured summary that will be used for further vulnerability analysis."""
    ),
    "generate_common_vulnerabilities": (
        """
        You are given the following information about a software project:

        {identified_repo_type}

        Based on the above project details, list the most common vulnerabilities, bugs, and anti-patterns found in such codebases. Include:

        - Security vulnerabilities (e.g., input validation, insecure dependencies)
        - Performance issues (e.g., blocking calls, memory misuse)
        - Maintainability/code smells (e.g., large functions, code duplication)

        Group them by category and return in a structured JSON-like format that will be used to guide code analysis in the next step."""
    ),
    "scan_codebase_for_identified_issues":(
        """
            You are analyzing the codebase of a software repository to detect known vulnerabilities and anti-patterns.

            You are provided with a list of typical issues commonly found in this type of project:

            {identified_common_vulnerabilities}

            Tools available:
            - `search_code("query")`: Search the codebase using keywords or patterns (e.g., "eval(", "os.system(", or class/function names).
            - `read_file(filepath)`: Read the contents of a specific file for deeper inspection.

            Your task:
            - Use `search_code` to locate potential matches for the vulnerabilities or anti-patterns listed above.
            - Use `read_file` to open and analyze specific files where matches were found.
            - For each confirmed issue, provide:
                - **Issue name**
                - **File name and line number**
                - **Relevant code snippet** (only enough to demonstrate the problem)
                - **Explanation** of why it’s a problem
                - **Suggested fix** (brief and actionable)

            Important:
            - Only report issues that are clearly present and verifiable in the code.
            - Be concise, avoid speculative or redundant findings.
            - Group issues by category (e.g., Security, Performance, Maintainability) in your internal structure for later formatting.

            Focus on high-signal findings that developers can act on.
        """
    ),
    "format_identified_issues_into_markdown":(
    """
        You are given the results of a static code analysis which identified vulnerabilities and code issues in a software project.

        The data is structured as a list of findings in the following format:

        {identified_code_issues}

        Each issue includes:
        - Issue name
        - Category (e.g., Security, Performance, Maintainability)
        - File name and line number
        - Code snippet
        - Explanation of the issue
        - Suggested fix

        Your task is to format this information into a well-structured, human-readable **Markdown report** (`SECURITY_AUDIT_Prometheus.md`) that can be committed to the repository.

        The Markdown file should include:
        - A title (e.g., "# Codebase Vulnerability and Quality Report")
        - A brief introductory paragraph
        - A table of contents linking to each category (use markdown anchor links)
        - For each issue (grouped by category):
            - An H2 heading for the category (e.g., ## Security Issues)
            - An H3 heading for each issue with the name (e.g., ### [1] Insecure Deserialization)
            - File name and line number (e.g., _File: app/utils.py, Line: 42_)
            - A fenced code block with the relevant code
            - A short explanation
            - A **Suggested Fix** section with actionable guidance

        Ensure the Markdown is clear, easy to navigate, and suitable for sharing in a development team.
    """
    )
}
