# codewithbro95/openmind

⭐ 21 · Python · MIT · 推送 2026-07-22 · [GitHub](https://github.com/codewithbro95/openmind) · [官网](https://openmind.fotiecodes.com) · 个人维护

**本地 AI 记忆引擎：索引你的文件夹，本地搜索与带出处的问答**

OpenMind Core 是本地优先的记忆引擎，提供 CLI 与带鉴权的本地 API。它索引用户明确授权的文件夹（支持文本/PDF/DOCX/CSV/Markdown/HTML/图片），用 LanceDB 存向量、SQLite 存元数据，后台索引并支持 Watch 模式同步；可搜索本地记忆并向 LM Studio 本地模型提问，回答附带来源。通过 openmind serve 暴露 127.0.0.1 版本化 API 供第三方客户端构建；明确不做桌面 UI、云同步或文件自动化，当前仅支持 LM Studio 作为用户侧提供者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 索引→搜索→带来源问答的本地流程，数据全部存于 ~/.openmind
- LanceDB 向量存储 + SQLite 元数据，文件哈希去重避免重复索引
- 带 bearer token 鉴权的本地 API（127.0.0.1:8765/api/v1）供客户端构建
- LM Studio 原生 REST 与 OpenAI 兼容端点用于对话、嵌入与图像描述

## 适用场景

- 在我自己的电脑文件里搜索和提问，如找回旧收据里的订单号
- 为桌面或编辑器扩展类客户端提供统一的本地记忆引擎
- 不把文件上传云端的前提下做带来源的文件问答

## 场景标签

`文档问答` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L11: OpenMind is a local AI memory engine for your computer.
> L23: Index local files -> Search local memory -> Ask source-grounded questions
> L39: - LM Studio as the user-facing local AI provider.

## 星数曲线

```mermaid
xychart-beta
    title "codewithbro95/openmind 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `637d2b37b714` · [字段定义](../../DATASET.md)*
