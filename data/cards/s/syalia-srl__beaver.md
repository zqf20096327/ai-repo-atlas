# syalia-srl/beaver

⭐ 37 · Python · MIT · 推送 2026-08-10 · [GitHub](https://github.com/syalia-srl/beaver) · [官网](https://syalia.com/beaver/) · 组织维护

**给开发者的纯 Python 嵌入式多模型数据库：关系/文档/向量/图/事件**

基于 SQLite 的本地嵌入式数据库，以单个可移植文件提供键值字典、持久化列表与优先队列、文档集合（向量嵌入+Pydantic 元数据）、向量线性检索、FTS5 全文与模糊搜索、知识图遍历、Pub/Sub、时间序列日志与跨进程锁等数据结构。面向小型本地场景，无需数据库服务器，线程与多进程安全，核心依赖仅 numpy/pydantic/rich/typer。以 pip 安装的 Python API 提供；CLI、REST 服务器与 Docker 镜像标注将在 2.0 正式版落地（目标 2026 年 6 月），当前处于 release-candidate 周期。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单文件 SQLite 存储，100% 兼容标准 SQLite 工具
- 文档集合支持向量嵌入存储与基于 numpy 的内存向量检索
- 知识图、Pub/Sub、HyperLogLog/Bloom Filter、时间序列日志等多种数据结构
- 线程与多进程安全，跨进程死锁防护锁

## 适用场景

- 本地小项目中替代独立数据库服务器，存储结构化数据与向量嵌入
- 在单脚本内同时使用字典、队列、全文搜索与知识图遍历
- 多进程脚本间通过持久化队列与锁进行任务协调

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L53:  * **Document Collections**: Store rich documents combining a vector embedding and Pydantic-based metadata.
> L54:  * **Vector Search**: Fast, multi-process-safe linear vector search using an in-memory `numpy`-based index.

## 星数曲线

```mermaid
xychart-beta
    title "syalia-srl/beaver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `411906c2e20b` · [字段定义](../../DATASET.md)*
