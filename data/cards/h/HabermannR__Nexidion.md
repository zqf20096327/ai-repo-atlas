# HabermannR/Nexidion

⭐ 22 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/HabermannR/Nexidion) · 个人维护

**可自托管的多用户私有知识库，带可选 AI 代理**

基于 Flask + React + PostgreSQL 的自托管知识库应用，面向需要管理敏感信息的用户：多用户隔离的 Vault、层级笔记、Markdown 编辑、完整版本历史、UUID 内部链接与 PDF 导入管道。默认零外部网络调用、无遥测；可选启用后台 Task Runner（需 OpenAI 兼容 API），自动重组笔记、汇总子树、执行批量修改，也可指向本地 Ollama/llama.cpp/LM Studio 保持数据不出本机。通过 Docker Compose 一键部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多用户 Vault 隔离与 JWT 认证、管理面板
- UUID 内部链接，重命名节点不断链
- 可选 AI Task Runner：重组笔记、汇总子树、批量修改
- 默认零外部网络调用，LLM 连接为显式 opt-in

## 适用场景

- 在家用 NAS 或 VPS 上自托管私有知识库，管理敏感资料
- 多用户团队隔离管理各自的知识库
- 导入 PDF 后让 AI 代理自动整理与汇总笔记

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L41: * **Optional AI Agent Runner:** An autonomous background worker that can reorganize notes, summarize subtrees, or e
> L107: *(Note: If you do not want to use the AI features, simply run the standard command in Step 3. The worker will rema

## 星数曲线

```mermaid
xychart-beta
    title "HabermannR/Nexidion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `049b2aecf99a` · [字段定义](../../DATASET.md)*
