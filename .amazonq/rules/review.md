AWS Q Must Follow Rules Bellow.

1. Review code only in main folder [location: ../main]
2. When reviewing code written in Python, follow the coding convention specified in ../codeConvention/pep-00008.rst. 
2. Define project-specific coding standards and best practices in Markdown rule files located in the project-root/.amazonq/rules directory. 
3. Amazon Q Developer performs both rule-based and generative AI-powered analysis to detect security vulnerabilities and code quality issues. 
4. Filtering is applied to exclude unsupported languages, test code, and third-party open source libraries, focusing reviews on relevant code. 
5. Code issues detected will include detailed descriptions and recommended fixes, some of which can be applied directly to the codebase. 
6. Rules should specify issue severity levels (Critical, High, Medium, Low) and handling procedures. 
7. Commit message format and naming conventions must be standardized to maintain consistency and traceability. 
8. Include guidelines on coding style, documentation, security best practices, and performance as relevant. 
9. Keep rules updated to incorporate the latest AWS and Amazon security policies and best practices. 
10. Use the /q review slash command in GitHub pull requests to initiate or rerun automated code reviews including all comments and commits. 
11. Review and accept suggested code changes from Amazon Q Developer to ensure code quality and policy compliance. 
12. Treat critical issues with high priority to prevent security risks or control loss.