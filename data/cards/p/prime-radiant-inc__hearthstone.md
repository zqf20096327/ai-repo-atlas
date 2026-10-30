# prime-radiant-inc/hearthstone

⭐ 23 · TypeScript · Apache-2.0 · 推送 2026-06-06 · [GitHub](https://github.com/prime-radiant-inc/hearthstone) · 组织维护

**家庭知识问答应用：用 Google Docs 作 RAG 答案来源**

面向家庭场景的问答应用：主人连接自己的 Google Drive 文档并建立索引，访客（保姆、代管房屋者、家人）凭六位 PIN 登录 iOS 应用，用自然语言提问 WiFi 密码、作息、紧急联系人等家庭事务；答案基于文档内容生成并附引用来源。技术栈为 Bun/TypeScript 后端 + SQLite/sqlite-vec 向量检索 + OpenAI 嵌入与对话模型，iOS 端需 Xcode 16+ 编译，后端可部署到 Fly.io。限制：需 OpenAI API key 与 Google Cloud OAuth 凭据，仅提供 PIN 一种认证方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Google Docs 索引化，答案带引用且可点击查看原文
- 六位 PIN + QR 码的访客访问机制，可随时吊销
- SQLite + sqlite-vec 单文件向量检索
- 后端可单机部署到 Fly.io（含持久卷与休眠唤醒）

## 适用场景

- 保姆或房屋代管人临时照看时快速查到家庭事务信息
- 家庭成员集中维护一份文档，全员随时问答查询
- 度假屋/出租屋的设备操作说明远程问答

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: Hearthstone gives babysitters, house-sitters, and family members instant answers to household questions — WiFi passw
> L15: Answers are grounded in your documents. The AI cites its sources, and guests can tap through to read the original.
> L260: - **SQLite + sqlite-vec** for vector search. Embeddings are stored alongside the data in a single file. On macOS, 

## 星数曲线

```mermaid
xychart-beta
    title "prime-radiant-inc/hearthstone 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f43b9993f58d` · [字段定义](../../DATASET.md)*
