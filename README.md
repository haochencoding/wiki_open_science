# Dictionaries for Processed Data

## Blocking metrics

### block_monthly_editor_metrics.csv
| Metric | Description |
|--------|-------------|
| **Block & Reblock & Unblock** | |
| `n_editor_all` | Number of all editors |
| `n_editor_ip` | Number of anonymous editors (i.e., IP addresses) |
| `n_editor_bot` | Number of bots |
| `n_editor_user` | Number of users (with wiki account) |
| **Block & Reblock** | |
| `n_editor_all_block` | Number of all editors |
| `n_editor_ip_block` | Number of anonymous editors (i.e., IP addresses) |
| `n_editor_bot_block` | Number of bots |
| `n_editor_user_block` | Number of users (with wiki account) |
|  **Unblock Only** | |
| `n_editor_all_unblock` | Number of all editors |
| `n_editor_ip_unblock` | Number of anonymous editors (i.e., IP addresses) |
| `n_editor_bot_unblock` | Number of bots |
| `n_editor_user_unblock` | Number of users (with wiki account) |


### block_monthly_administrator_metrics.csv
| Metric | Description |
|--------|-------------|
| **Block & Reblock & Unblock** | |
| `n_admin_all` | Number of administrators that have blocked or unblocked a user per month |
| `n_admin_ip` | Number of administrators who log the request using IP addresses |
| `n_admin_bot` | Number of administrators who are bots |
| `n_admin_user` | Number of administrators who log the request using wiki account |
| **Block & Reblock** | |
| `n_admin_all_block` | Number of administrators that have blocked a user per month |
| `n_admin_ip_block` | Number of administrators who log the request using IP addresses |
| `n_admin_bot_block` | Number of administrators who are bots |
| `n_admin_user_block` | Number of administrators who log the request using wiki account |
| **Unblock Only** | |
| `n_admin_all_unblock` | Number of administrators that have unblocked a user per month |
| `n_admin_ip_unblock` | Number of administrators who log the request using IP addresses |
| `n_admin_bot_unblock` | Number of administrators who are bots |
| `n_admin_user_unblock` | Number of administrators who log the request using wiki account |

### block_monthly_log_metrics.csv
These metrics count the number of blocking logs per month.
| Category | Metric | Description |
|----------|--------|-------------|
| **Block & Reblock & Unblock** | | |
| Total Number of Logs | `n_log_all` | Total number of logs |
| Number of Logs by Editor Type | `n_log_editor_ip` | Logs done to IP editors |
| | `n_log_editor_bot` | Logs done to bots |
| | `n_log_editor_user` | Logs done to users (with wiki account) |
| Number of Logs by Admin Type | `n_log_admin_ip` | Logs requested by IP administrators |
| | `n_log_admin_bot` | Logs requested by bot administrators |
| | `n_log_admin_user` | Logs requested by user administrators |
| **Block & Reblock** | | |
| Total Number of Logs | `n_log_all_block` | Total number of (re-)block logs |
| Number of Logs by Editor Type | `n_log_editor_ip_block` | (Re-)block logs done to IP editors |
| | `n_log_editor_bot_block` | (Re-)block logs done to bots |
| | `n_log_editor_user_block` | (Re-)block logs done to users (with wiki account) |
| Number of Logs by Admin Type | `n_log_admin_ip_block` | (Re-)block logs requested by IP administrators |
| | `n_log_admin_bot_block` | (Re-)block logs requested by bot administrators |
| | `n_log_admin_user_block` | (Re-)block logs requested by user administrators |
| **Unblock Only** | | |
| Total Number of Logs | `n_log_all_unblock` | Total number of unblock logs |
| Number of Logs by Editor Type | `n_log_editor_ip_unblock` | Unblock logs done to IP editors |
| | `n_log_editor_bot_unblock` | Unblock logs done to bots |
| | `n_log_editor_user_unblock` | Unblock logs done to users (with wiki account) |
| Number of Logs by Admin Type | `n_log_admin_ip_unblock` | Unblock logs requested by IP administrators |
| | `n_log_admin_bot_unblock` | Unblock logs requested by bot administrators |
| | `n_log_admin_user_unblock` | Unblock logs requested by user administrators |


## Page abuse metrics

### abusefilter_monthly_metrics.csv
The abusefilter is the filter on Wikipedia that automatically detect abnormal editing behaviours. It helps to monitor and intervene vandalism/abuse on the pages.
- n_af_all: number of all abusefilter-related logs
- n_af_create: number of abusefilter creation logs
- n_af_modify: number of abusefilter modify logs
- n_af_hit: number abusefilter hit logs (**warning**: the value of this variable is all 0)
- note: n_af_all = n_af_create + n_af_modify