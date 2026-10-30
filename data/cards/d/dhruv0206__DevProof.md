# dhruv0206/DevProof

⭐ 19 · TypeScript · NOASSERTION · 推送 2026-05-19 · [GitHub](https://github.com/dhruv0206/DevProof) · 个人维护

**面向开发者的 GitHub 仓库 AI 评分与开源议题搜索平台**

DevProof 是一个 Web 平台（Next.js 前端 + FastAPI 后端）：粘贴 GitHub 仓库 URL，由 AI 引擎（Google Gemini）扫描代码库，从 Features、Architecture、Intent、Forensics 四个维度生成 0-100 的 Technical Depth Score，并划分 ELITE/ADVANCED 等层级。另提供基于 Pinecone 向量库的 43 万+开源 issue 语义搜索，以及通过 GitHub OAuth 登录保存评分、生成分享页面与 README 徽章的认证开发者档案。无需注册即可获取评分。本地运行需 Python 3.11+、Node.js 18+、PostgreSQL 及 Pinecone/Google AI/GitHub API 密钥。许可证为 BSL 1.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四维度 AI 代码分析并输出 0-100 技术深度评分（TDS）
- 43 万+开源 issue 的自然语言语义搜索
- GitHub 登录后可保存评分、生成分享页面与 README 徽章
- 提供公开 API：扫描、审计、缓存评分与议题搜索

## 适用场景

- 量化评估自己或他人 GitHub 仓库的技术深度
- 用自然语言寻找可参与的开源贡献议题
- 构建带可分享评分徽章的开发者作品集

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: Score any GitHub repo with AI-powered code analysis. Get a Technical Depth Score, share it, and build a verified dev
> L20: Paste a GitHub URL on the landing page. The AI engine scans the codebase and scores it across 4 buckets:
> L51: |**AI**|Google Gemini (embeddings + code analysis)|

## 星数曲线

```mermaid
xychart-beta
    title "dhruv0206/DevProof 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3de179b75d72` · [字段定义](../../DATASET.md)*
