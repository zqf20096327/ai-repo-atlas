# Anionex/treeAI

⭐ 49 · TypeScript · MIT · 推送 2026-08-10 · [GitHub](https://github.com/Anionex/treeAI) · 个人维护 · 中文 README

**本地优先的树状 LLM 对话可视化工作区，支持分支探索与导出**

纯浏览器端的 React + React Flow 画布应用：将 LLM 对话组织为节点树，可从任意节点分叉、并行探索不同分支，各分支可独立设置模型、温度与 token 预算。兼容 OpenAI 风格流式 Chat Completions API 的任意提供商，请求直接由浏览器发往用户配置的端点，无应用后端。会话与模型配置存于浏览器 IndexedDB（API key 明文存储）。支持导入 .txt/.md 文本、导出 FreeMind 格式 .mm 文件。项目处早期阶段（0.1.0），不支持 reasoning 模型思考流，无账号同步与协作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 对话以树状画布组织，任意节点可分叉、并行保留所有路径
- 节点级独立配置模型、温度与 token 预算
- 客户端直连 OpenAI 兼容 API，数据存于浏览器 IndexedDB，无中间服务器
- 导出 FreeMind 兼容 .mm 文件，导入 .txt/.md 作为对话节点

## 适用场景

- 对同一提示并行探索多条回答路径并事后对比
- 在不同分支上切换模型或参数进行实验
- 本地保存对话树并导出为思维导图归档

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L15: A local-first visual workspace for exploring, comparing, and exporting LLM conversation trees across OpenAI-compati
> L21: All sessions and model configurations stay in the browser's IndexedDB. Requests go directly from the browser to the
> L79: - **Streaming:** responses are consumed from Server-Sent Events and rendered incrementally in the active node.

## 星数曲线

```mermaid
xychart-beta
    title "Anionex/treeAI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-25 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `372f5b932a75` · [字段定义](../../DATASET.md)*
