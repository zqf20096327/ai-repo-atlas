# fxxkrlab/ADMINCHAT_PANEL

⭐ 16 · Python · NOASSERTION · 推送 2026-04-10 · [GitHub](https://github.com/fxxkrlab/ADMINCHAT_PANEL) · 组织维护 · 中文 README

**Telegram 客服平台：多 Bot 池消息转发 + Web 管理面板 + FAQ/AI 自动回复**

面向需要运营 Telegram 客服的管理员：将 Bot 私聊与群组 @提及消息转发到 Web 面板，客服在浏览器实时回复。功能含多 Bot 池（Redis 令牌桶限流与故障转移）、FAQ 引擎（5 种匹配模式 + 8 种回复模式，其中 5 种涉及 AI/RAG）、RAG 知识库检索（对接 Dify Knowledge API + pgvector）、AI Provider 五种认证方式（API Key/OpenAI OAuth/Claude OAuth/Claude Session Token/Gemini OAuth）、沙箱化插件系统（ACP 架构 + Ed25519 签名验证）、三级角色权限与审计日志。后端 Python/FastAPI，前端 React/TypeScript，数据层 PostgreSQL + Redis，Docker Compose 一键部署。README 标注 2026 版权与 'Vibe Coded'。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Bot 池管理，Redis 令牌桶限流与故障转移
- FAQ 引擎：5 种匹配模式 + 8 种回复模式（含 RAG/AI 兜底/AI 润色等）
- 五种 AI Provider 认证方式，OAuth Token 每 5 分钟自动刷新
- 沙箱化插件系统：热更新、命名空间隔离、Ed25519 签名验证、ACP Market

## 适用场景

- 运营团队在 Web 面板统一接收并回复多个 Telegram Bot 的用户消息
- 通过 FAQ 规则与 AI/RAG 自动回答常见问题
- 统计未匹配的遗漏知识点以补充 FAQ 规则
- 通过插件系统扩展面板功能

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L32: **Telegram 双向消息转发 Bot + Web 客服管理面板** &mdash; 一站式 Telegram 客户服务解决方案，支持多 Bot 池管理、FAQ 自动回复引擎（5 种匹配模式 + 8 种回复模式）、RAG 知识
> L36: ADMINCHAT Panel 是一个功能完备的 Telegram 客服管理系统。它将 Telegram Bot 收到的私聊消息和群组 @提及 消息统一转发到 Web 管理面板，让管理员/客服人员可以在浏览器中实时查看并回复用户消
> L79: 用户消息 → FAQ 匹配 → 直接返回预设答案（不调 AI）

## 星数曲线

```mermaid
xychart-beta
    title "fxxkrlab/ADMINCHAT_PANEL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `da845a9c40b3` · [字段定义](../../DATASET.md)*
