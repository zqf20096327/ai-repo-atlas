# ubunye-ai-ecosystems/ubunye_engine

⭐ 16 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ubunye-ai-ecosystems/ubunye_engine) · [官网](https://ubunye-ai-ecosystems.github.io/ubunye_engine/) · 组织维护

**配置驱动的 Spark 数据/ML 流水线框架，同一任务多环境运行**

用 YAML 配置加普通 Python 类描述数据流水线，框架负责连接、计算引擎（Apache Spark 或无 Java 的 pandas）与读写循环；同一任务文件夹不改代码即可在笔记本、Docker、Kubernetes、AWS Glue、GCP Dataproc、Azure Container Apps 和 Databricks 上运行，`ubunye prove` 比对各环境输出行哈希验证一致性。连接器（hive/jdbc/delta/s3/unity/binary/rest_api）、存储后端与执行后端均以插件方式从外部注册。支持 ETL、ML 训练与推理（模型注册到本地/S3/GCS/Databricks 卷）、RAG 文档流水线与特征工程。以 pip 包提供，附 CLI 与 Python API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一任务在 7 类环境运行并通过输出哈希比对验证
- 连接器/存储/执行后端均为外部插件，无需改引擎代码
- pandas 后端无需 Java 即可在笔记本运行
- 模型注册写入本地文件夹、Databricks 卷、S3 或 GCS

## 适用场景

- 在笔记本开发、在生产集群运行同一 ETL/ML 流水线
- 统一团队流水线的目录结构与配置格式
- 搭建 RAG 文档摄取与嵌入流水线
- 管理 ML 模型版本并按漂移检查决定晋升

## 场景标签

`RAG` `MLOps` · 领域:知识与检索

## 证据(README 行号)

> L17: **Ubunye Engine writes that plumbing for you.** You describe the pipeline in a short YAML file and put your transfo
> L23: - **Proven portability.** One task, unchanged, gives the same rows on pandas (no Java), local Spark, Kubernetes, AW

## 星数曲线

```mermaid
xychart-beta
    title "ubunye-ai-ecosystems/ubunye_engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ceef729c496d` · [字段定义](../../DATASET.md)*
