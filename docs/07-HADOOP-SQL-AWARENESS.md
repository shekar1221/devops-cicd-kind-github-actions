# Hadoop and SQL Awareness for JD

## SQL / RDBMS basics

The JD mentions Postgres and Oracle. For this role, explain operational awareness.

Checks:

```sql
select count(*) from table_name;
select * from table_name where id = 100;
select count(*) from pg_stat_activity;
select * from pg_stat_activity where state='active';
```

Troubleshooting areas:

- Connectivity
- Authentication
- Slow query
- High sessions
- Locks
- Tablespace or disk full
- Backup/restore awareness

Interview answer:

> I check whether the issue is connectivity, credentials, active sessions, locks, slow queries, or storage. For application issues, I also check connection pool errors in logs.

## Hadoop basics

Components:

| Component | Role |
|---|---|
| HDFS | Distributed file system |
| NameNode | Metadata server |
| DataNode | Stores actual blocks |
| YARN | Resource management |
| ResourceManager | YARN master |
| NodeManager | Worker agent |
| MapReduce | Batch processing |
| Hive | SQL-like layer |
| Spark | Fast processing engine |

Commands:

```bash
hdfs dfs -ls /
hdfs dfs -du -h /path
hdfs dfsadmin -report
yarn application -list
yarn logs -applicationId <id>
```

Interview answer:

> I have basic Hadoop operational awareness. I understand HDFS, NameNode, DataNode, YARN, ResourceManager, NodeManager, and how to check HDFS health and YARN application logs.

