# dharunram-lgtm/Echo_Knowledge

⭐ 4 · Rust · MIT · 推送 2026-11-14 · [GitHub](https://github.com/dharunram-lgtm/Echo_Knowledge) · 个人维护

**本地优先的个人知识管理桌面应用：语义检索与带出处的 AI 问答**

面向 Windows 的 Tauri 2 桌面应用，将 PDF/Markdown/TXT 导入本地 SQLite 文档库，做关键词与基于余弦相似度的语义检索，并通过 RAG 流程生成带来源引用的 AI 问答（Ask ECHO），另提供交互式知识图谱浏览。AI 能力依赖 BYOK：用户自备 Gemini（嵌入与生成）或 Groq（生成）API key，密钥经 DPAPI 存入 Windows Credential Manager。数据、嵌入与聊天记录均存本地，无遥测与账号；不支持扫描件 OCR 与跨设备云同步。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 SQLite 存储，关键词与语义（余弦相似度）双检索路径
- RAG 问答带可验证来源引用，直连 Gemini/Groq HTTPS 端点
- 交互式知识图谱（@xyflow/react）展示概念关系与聚类
- SHA-256 去重与 DPAPI 加密的凭据隔离

## 适用场景

- 把个人 PDF/Markdown 文档导入本地库做语义检索
- 对自有文档提问并获得带引用的回答
- 用知识图谱可视化探索文档间的概念关联

## 场景标签

`知识库管理` `语义搜索` `知识图谱` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: ECHO Knowledge is a local-first, AI-powered knowledge management system and personal document intelligence desktop a
> L25: - **Ask ECHO — Grounded AI Answers:** Interactive dialogue interface that constructs augmented prompts from retriev

## 星数曲线

```mermaid
xychart-beta
    title "dharunram-lgtm/Echo_Knowledge 星数(近 2 点)"
    x-axis ["2026-11-12", "2026-11-24"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-12 4 → 2026-11-24 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `2a4c13f44bd1` · [字段定义](../../DATASET.md)*
