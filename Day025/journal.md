# Day 025

## Journal

### Imagine you are building an AI application with different types of users, such as Students, Developers, and AI Engineers.

### How could inheritance help you create these different user types without repeating the same code?

### Explain what information and behavior could belong in a parent User class and what could belong specifically to each child class.

Inheritance provides a perfect structural architecture for this application. Instead of writing identical code for login sequences, profile management, and account settings three separate times, you can bundle all shared human properties into a single parent class and let individual roles branch out as child classes.
Here is how you can cleanly divide the information and behaviors across your class hierarchy:
1. The Parent Class: User
This class houses the foundational code baseline that every human user requires to exist in your application ecosystem.
Shared Information (Attributes):
user_id: A unique database string identifier.
username: The account display name.
email: The verified digital contact address.
account_tier: Tracks access levels (e.g., Free, Pro, Enterprise).
Shared Behavior (Methods):
.login() / .logout(): Handles basic credential verification and session token authentication.
.update_profile_picture(): Modifies core user account metadata.
.reset_password(): Triggers a secure recovery link.
2. The Child Classes: Role-Specific Customization
Each child class inherits 100% of the functionality from User but introduces unique data and behaviors specific to their workflow.
Student(User)
Tailored for learning environments, prioritizing basic model interfaces and educational guardrails.
Unique Information:
enrolled_courses: A list of active curriculum pathways.
monthly_token_allowance: A strict token cap to prevent runaway usage on homework.
Unique Behavior:
.submit_assignment(): Packages code or prompts to an automated grading engine.
.query_tutor_bot(): Opens a conversation window with a highly structured, explanatory sandbox LLM.
Developer(User)
Built for engineers who need raw backend data access and control hooks to build simple applications.
Unique Information:
api_key_registry: A dynamic roster of secure authentication strings for external integrations.
rate_limits: Tracks concurrent requests permitted per minute.
Unique Behavior:
.generate_new_key(): Provisions a fresh endpoint authentication credential.
.view_usage_dashboard(): Displays a breakdown of API latency and payload error logs.
AIEngineer(User)
Designed for elite developers who require direct control over advanced orchestration layers, pipelines, and evaluation metrics.
Unique Information:
active_pipelines: Array mapping active vector databases or data indexing workflows.
eval_dataset_paths: Cloud storage strings pointing to benchmarking validation files.
Unique Behavior:
.trigger_finetuning_job(): Submits custom training weight configurations to compute clusters.
.evaluate_model_drift(): Compares current application output metrics against standard evaluation datasets.
