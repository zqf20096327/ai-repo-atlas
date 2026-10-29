# LevelUpBM/frank-bot

⭐ 19 · Python · 推送 2026-03-30 · [GitHub](https://github.com/LevelUpBM/frank-bot) · [官网](https://frankbot.lvlup.au/) · 组织维护

**面向企业文档问答的自托管 RAG 聊天机器人平台**

基于 Flask 的自托管 AI 聊天机器人平台：客户端上传 PDF/DOCX/TXT 文档，系统分块（400 词、80 词重叠）后用 Sentence Transformers（all-MiniLM-L6-v2）本地嵌入 ChromaDB，以 Claude 为 LLM 后端回答提问，文档不离开客户服务器。提供 12 个行业垂直人格提示词与三层提示架构，支持查询扩展（Claude Haiku 生成 4 个改写）、来源加权与原子重建索引。通过 pip 安装依赖并运行 run_bot.py，设计为 Linux VM 上 systemd 服务或 Docker 部署，每个客户独立 droplet 隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地嵌入（sentence-transformers）+ ChromaDB 本地向量库，无需外部嵌入 API
- 12 个行业垂直人格 + 三层提示架构（安全层始终注入且优先）
- 查询扩展（Claude Haiku 生成 4 个改写合并检索）与指定文档保证检索
- systemd/Docker 部署，每客户独立隔离实例

## 适用场景

- 企业上传内部政策/合规文档，让员工自助问答
- HR、建筑、矿业等行业定制垂直问答机器人
- 数据不出本地服务器的自托管文档问答

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: **RAG-powered AI assistant for any business. Drop in your documents. Ask Frank anything.**
> L5: Frank is a production-ready AI chatbot platform built on:
> L11: The client supplies their own Anthropic API key. Their documents never leave their server.

## 星数曲线

```mermaid
xychart-beta
    title "LevelUpBM/frank-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e5dfd2fb9468` · [字段定义](../../DATASET.md)*
