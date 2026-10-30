# srimallya/subgrapher

⭐ 25 · JavaScript · AGPL-3.0 · 推送 2026-05-05 · [GitHub](https://github.com/srimallya/subgrapher) · [官网](https://thetrustcommons.com/apps) · 个人维护

**本地优先的语义化知识浏览工作台，集成 AI 代理与混合 RAG**

面向个人研究者的 Electron 桌面应用：以“语义引用”为核心知识容器，可浏览网页、写笔记、附加文件夹与邮件线程、生成 HTML 可视化，并让 AI 代理在该上下文中推理。含环境感知 Notes（自动识别声明、抓取网页证据并打分）、Status 仪表盘、邮件客户端、基于 Hyperswarm 的私有/公开分享，以及通过 Telegram 远程调用本地模型。首次启动下载捆绑的本地 LLM 运行时与 GGUF 模型用于笔记路由与 feed 清理；支持 LM Studio 与 OpenAI/Google/Anthropic/Cerebras API 模型。AGPL-3.0 许可，作者声明项目仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 语义引用作为可 fork、可分享的知识容器
- 环境感知 Notes：后台识别事实声明、检索网页证据并评分
- 首次启动下载捆绑本地 LLM 运行时（GGUF）做笔记路由与 feed 清理
- Telegram bot 远程调用本地模型

## 适用场景

- 把网页、文件、邮件汇聚到同一上下文做研究整理
- 写笔记时自动收集并评估网页证据
- 通过 Telegram 在外地远程使用本地模型
- 与信任的同伴私有共享研究引用

## 场景标签

`知识库管理` `RAG` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L3: Subgrapher is a desktop app for building, browsing, and sharing knowledge as semantic references.
> L31: - Downloads the bundled local LLM runtime and GGUF model on first launch, then uses it for note policy routing and 

## 星数曲线

```mermaid
xychart-beta
    title "srimallya/subgrapher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7cefc8b1508b` · [字段定义](../../DATASET.md)*
