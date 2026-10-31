# nongjun/feishu-cursor-claw

⭐ 14 · Python · MIT · 推送 2026-07-12 · [GitHub](https://github.com/nongjun/feishu-cursor-claw) · 个人维护 · 中文 README

**把飞书变成 Cursor AI 远程遥控器的中继服务**

通过 WebSocket 长连接将飞书消息转发到本机 Cursor Agent CLI 的中继服务：在手机上发文字、语音、图片，Mac 上的 Cursor 即执行写代码、审文档、管理文件等任务。语音转文字采用火山引擎豆包 STT 为主、本地 whisper-cpp 为回退；包含 OpenClaw 风格的身份与记忆系统（FTS5 BM25 + 向量混合检索）、定时任务、心跳机制与项目路由。运行要求 macOS（Apple Silicon）、Bun、Cursor IDE 及 Agent CLI，需配置飞书自建应用与 Cursor API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 飞书 WebSocket 长连接远程驱动本机 Cursor Agent CLI，支持文字/语音/图片多模态输入
- 两级语音转文字：火山引擎豆包 STT 主路径 + 本地 whisper-cpp 回退
- 身份与记忆系统：.mdc 规则注入、FTS5 BM25 + 向量混合检索、增量索引与心跳机制
- AI 可创建 cron 定时任务，支持多工作区路由与会话续接

## 适用场景

- 不在电脑前时用飞书消息远程让 Cursor 写代码或改代码
- 高管/知识工作者通过 IM 与 AI 共创文档、审阅战略、管理知识库
- 给 AI 助手配置持久人格与长期记忆，跨会话延续工作上下文

## 场景标签

`编码 Agent` `AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: Phone (Feishu) ──WebSocket──→ feishu-cursor ──Cursor CLI──→ Local Cursor IDE
> L11: Cursor Agent CLI is incredibly powerful, but you need to be at your desk to use it. **feishu-cursor** bridges that 
> L62: git clone https://github.com/nongjun/feishu-cursor-claw.git

## 星数曲线

```mermaid
xychart-beta
    title "nongjun/feishu-cursor-claw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7c43388fa8cc` · [字段定义](../../DATASET.md)*
