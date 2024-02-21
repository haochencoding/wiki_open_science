# Dictionaries for Processed Data

GitHub link for all data of these metrics: https://github.com/haochencoding/wiki_open_science/tree/main/data/processed_data

## Blocking metrics
The blocking metrics is calculated by processing block log events data, retrieved from English Wikipedia API. All metrics are calculated for a specific month of a specific year. Data available from December 2004 to June 2023 (will update to December 2023).


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


## Edit abuse metrics
The edit abuse metrics are calulated by processing abuse log data and abusefilter log data, retrieved from English Wikipedia API. Data available from March 2009 to June 2023 (will be updated to December 2023).

For more deteils, see: https://en.wikipedia.org/wiki/Wikipedia:Edit_filter

### Terminologies 
**Abusefilter** 
- The abusefilter is the filter on Wikipedia that automatically detect abnormal editing behaviours. It helps to monitor and intervene vandalism/abuse on the pages.
- Each modification and creation of abuse filters will be logged in the abusefilter log, stored in the back end.

**Abuse Logs**
- Once abnormal editing behaviours are detected, they will trigger certain automatical responses and be logged into the abuse log.

**Abusefilter Effects**
There are 4 types of effects of abusefilters.
- **Disallow**: The strongest setting is disallow. In this case, the edit is rejected, and the user will see a customizable message (this one by default). A link is provided for reporting false positives. It is also possible to have a user's autoconfirmed status revoked if a user trips the filter.
- **Warn:** The next lowest setting is to warn. In this case, the user will see a customisable message (this one by default) that the edit may be problematic. The user then has the option to either proceed with the save, or abandon the edit.
- **Tag:*** The next lowest setting is to add a tag. In this case, the edit is tagged for review by patrollers.
- **Log**: The lowest setting is to log the edit. In this case, the edit is merely added to the abuse log. When testing new filters, this is the suggested setting to use.

### abusefilter_monthly_metrics.csv
| Metric | Description |
|--------|-------------|
| `n_af_all` | Number of all abusefilter-related logs |
| `n_af_create` | Number of abusefilter creation logs |
| `n_af_modify` | Number of abusefilter modify logs |
| `n_af_hit` | Number of abusefilter hit logs |
**Notes**:
 - the values of 'n_af_hit' is all 0
 - `n_af_all` = `n_af_create` + `n_af_modify`

 ### abusefiltered_edits_monthly_metrics.csv
|  Metric | Description |
|----------|-------------|
| `n_afedit_result_all` | Total number of edits filtered by abusefilter|
| `n_afedit_result_disallow` | Number of edits labelled as disallow |
| `n_afedit_result_warn` | Number of edits labelled as warn |
| `n_afedit_result_tag` | Number of edits labelled as tag |
| `n_afedit_result_other` | Number of edits labelled as other actions by the abuse filter |
| `n_afedit_editor_all` | Total number of editors affected by the abuse filter |
| `n_afedit_editor_ip` | Number of anonymous editors (IP addresses) affected by the abuse filter edits |
| `n_afedit_editor_bot` | Number of bot editors affected by the abuse filter edits |
| `n_afedit_editor_account` | Number of registered editors affected by the abuse filter edits |