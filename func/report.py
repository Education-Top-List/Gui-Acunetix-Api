sql_injection_report_template = """
## Task ID：{task_id}
- Verify node server：{api_url}
- Vulnerable URL：{url}; Data parameters submitted：{data}
- Database type：{dbms}； Database version：{dbms_version}
- Injection type：
```
{injection_type}
```
- 注入Payload：
```
{payload}
```
---
"""


def save_to_md(tree_view, file_path):
    print(file_path)
    model = tree_view.get_model()
    with open(file=file_path,mode="w") as md:

        for row in model:
            api_url, task_id, status, url, data, dbms, dbms_version, injection_type, payload = row
            report_md = sql_injection_report_template.format(api_url=api_url, task_id=task_id, url=url, data=data,
                                                             dbms=dbms, dbms_version=dbms_version,
                                                             injection_type=injection_type, payload=payload)
            md.write(report_md)
