# Riscue/ha-ai-memory

⭐ 13 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Riscue/ha-ai-memory) · 个人维护

**Home Assistant Assist 代理的长期语义记忆组件**

Home Assistant 自定义集成，为 Assist LLM 代理提供跨对话持久记忆：自动向每个代理暴露 add_memory / search_memory / delete_memory 三个原生 LLM 工具，另提供四个 HA 服务供自动化脚本调用。记忆按 Wing→Room 组织，分层 L0–L3（层间晋升后台任务与 L0/L1 接线尚未完成），支持 private/common 隐私作用域，数据本地存储于 SQLite（WAL 模式）。嵌入可选 Ollama、OpenAI 兼容端点（llama.cpp/LM Studio/vLLM 等）或内置 TF-IDF，检索为 SQL 预过滤 + 余弦相似度 + 文本回退。经 HACS 或手动复制安装，要求 HA ≥ 2025.11.3 与 Python 3.14。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- add/search/delete_memory 原生 LLM 工具自动暴露给所有 Assist 代理
- Wing→Room 记忆宫殿结构与 private/common 隐私作用域
- 三种嵌入引擎：Ollama、OpenAI 兼容端点、零依赖 TF-IDF
- 数据全部本地（SQLite + WAL，嵌入向量磁盘缓存）

## 适用场景

- 让家庭助理代理记住我的偏好、健康状况与设备信息并在后续对话中召回
- 通过自动化脚本读写记忆（如存储门锁密码、按条件检索）
- 多代理共享 common 记忆或隔离 private 记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: A long-term, semantic memory system for Home Assistant's Assist LLM agents. Store facts, preferences,
> L21: - **Native LLM tools**: `add_memory`, `search_memory`, and `delete_memory` are automatically exposed
> L114: Once installed, three tools are exposed to every Assist agent. The agent decides when to call them

## 星数曲线

```mermaid
xychart-beta
    title "Riscue/ha-ai-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `cc6afe306a1b` · [字段定义](../../DATASET.md)*
