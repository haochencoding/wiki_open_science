# Dictionaries for Processed Data

`block_monthly_editor_metrics.csv`
- For the monthly number of editors **(re-)blocked and unblocked**
    - n_editor_all: number of all editors
    - n_editor_ip: number of anonymous editors (i.e., IP addresses) 
    - n_editor_bot: number of bots
    - n_editor_user: number of users (with wiki account)
- For the monthly number of editors **(re-)blocked** 
    - n_editor_all_block: number of all editors
    - n_editor_ip_block: number of anonymous editors (i.e., IP addresses) 
    - n_editor_bot_block: number of bots
    - n_editor_user_block: number of users (with wiki account)
- For the monthly number of editors **unblocked** 
    - n_editor_all_unblock: number of all editors
    - n_editor_ip_unblock: number of anonymous editors (i.e., IP addresses) 
    - n_editor_bot_unblock: number of bots
    - n_editor_user_unblock: number of users (with wiki account)

`block_monthly_administrator_metrics.csv`
- For the monthly number of all administrators that have **(re-)blocked and unblocked** at least 1 editor
    - n_admin_all: number of administrators that have blocked or unblocked a user per month
    - n_admin_ip: number of administrators who log the request using IP addresses
    - n_admin_bot: number of administrators who are bots
    - n_admin_user: number of administrators who log the request using wiki account
- For the monthly number of all administrators that have **(re-)blocked** at least 1 editor
    - n_admin_all_block: number of administrators that have blocked or unblocked a user per month
    - n_admin_ip_block: number of administrators who log the request using IP addresses
    - n_admin_bot_block: number of administrators who are bots
    - n_admin_user_block: number of administrators who log the request using wiki account
- For the monthly number of all administrators that have **unblocked** at least 1 editor
    - n_admin_all_unblock: number of administrators that have blocked or unblocked a user per month
    - n_admin_ip_unblock: number of administrators who log the request using IP addresses
    - n_admin_bot_block: number of administrators who are bots
    - n_admin_user_unblock: number of administrators who log the request using wiki account

`block_monthly_queries_metrics.csv`
- For the monthly number of **(re-)block and unblock** queries
    - Total number of queries:
        - n_queries_all
    - Queries done to different types of editors
        - n_queries_editor_ip
        - n_queries_editor_bot
        - n_queries_editor_user
    - Queries requested by different types of administrators
        - n_queries_admin_ip
        - n_queries_admin_bot
        - n_queries_admin_user
    - Queries that apply to the whole site and only specific pages **Warning: this metric might not be correct**
        - n_queries_global
        - n_queries_pagespecific
- For the monthly number of **(re-)block** queries
    - Total number of queries:
        - n_queries_all_block
    - Queries done to different types of editors
        - n_queries_editor_ip_block
        - n_queries_editor_bot_block
        - n_queries_editor_user_block
    - Queries requested by different types of administrators
        - n_queries_admin_ip_block
        - n_queries_admin_bot_block
        - n_queries_admin_user_block
    - Queries that apply to the whole site and only specific pages **Warning: this metric might not be correct**
        - n_queries_global_block
        - n_queries_pagespecific_block
- For the monthly number of **unblock** queries
    - Total number of queries:
        - n_queries_all_unblock
    - Queries done to different types of editors
        - n_queries_editor_ip_unblock
        - n_queries_editor_bot_unblock
        - n_queries_editor_user_unblock
    - Queries requested by different types of administrators
        - n_queries_admin_ip_unblock
        - n_queries_admin_bot_unblock
        - n_queries_admin_user_unblock
    - Queries that apply to the whole site and only specific pages **Warning: this metric might not be correct**
        - n_queries_global_unblock
        - n_queries_pagespecific_unblock
        