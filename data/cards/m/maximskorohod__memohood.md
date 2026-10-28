# maximskorohod/memohood

⭐ 25 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/maximskorohod/memohood) · 个人维护

**hermes-agent 的对话记忆插件：跨会话事实存取与版本化**

MemoHood 是面向 hermes-agent 的记忆提供方插件（memory.provider），将事实、决定、更正与偏好存入本地 SQLite，跨会话自动回取。机制包括：FTS5/BM25+俄语词干与向量（BGE-M3，经 Cloudflare 或本地 fastembed）混合检索、RRF 融合、可选 Cohere 重排；SUPERSEDE 版本化替换旧事实；Ebbinghaus 遗忘曲线的夜间整理；Model2Vec 离线门控降低 LLM 调用（争议事实由 Gemini flash-lite 提取）。一键脚本安装，可选 API 密钥；无密钥时仅关键词精确匹配。要求 Python 3.11+ 与 hermes-agent>=0.18。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SUPERSEDE 事实版本化：新事实替换旧事实，旧版进入带日期历史
- 混合检索：FTS5/BM25 + 向量 + RRF 融合 + 可选 Cohere 重排
- Model2Vec 离线门控与 Gemini flash-lite 争议事实提取，降低调用成本
- 按 Ebbinghaus 曲线衰减 confidence 的夜间整理与 pinned 事实保护

## 适用场景

- 让个人 agent 在新会话中自动记住偏好、决定与更正
- 长期陪伴型对话中避免旧事实与新事实混存冲突
- 本地优先存储对话记忆，模型更换后记忆不丢失

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L2:  MemoHood — это плагин памяти диалогов для hermes-agent: агент сам замечает важное в разговоре, сам вспоминает его к
> L31: Без памяти агент помнит только то, что помещается в текущий контекст: начали новую сессию — и всё, что было вчера, 
> L78: **1. Один командой.** Установщик сам находит venv `hermes-agent`, ставит зависимости (`sqlite-vec`, `PyStemmer`, `f

## 星数曲线

```mermaid
xychart-beta
    title "maximskorohod/memohood 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ac5cdba3d52a` · [字段定义](../../DATASET.md)*
