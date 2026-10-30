# actionagentai/openclaw-dashboard

⭐ 18 · TypeScript · MIT · 推送 2026-04-20 · [GitHub](https://github.com/actionagentai/openclaw-dashboard) · 组织维护

**OpenClaw AI 网关的 Web 可视化管理面板，全程支持语音输入**

基于 React/Next.js 的自托管仪表盘，将 OpenClaw AI 网关的 35+ CLI 命令映射为 12 个 UI 页面，覆盖网关健康、流式聊天、Agent 管理、会话、模型、语音 STT、节点、技能、渠道、定时任务、配置与日志。通过 WebSocket v3 JSON 协议直连网关，提供 80+ 方法的 TypeScript 类型化 RPC 客户端，自身不存储数据。浮动麦克风按钮（Cmd+Shift+M）可在任意输入框注入语音转写文本。运行需 Node.js >= 20 与已启动的 OpenClaw 网关。

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

- 每个 CLI 命令对应一个可视化页面（12 页）
- WebSocket v3 协议直连网关，80+ RPC 方法全 TypeScript 类型化
- Speech-to-text everywhere：浮动麦克风向任意输入框注入转写文本
- 零数据库：纯 WebSocket 客户端，数据全部存于 OpenClaw

## 适用场景

- 不敲命令行即可管理自托管的 OpenClaw 网关
- 在网页上与网关 Agent 流式对话并管理会话与技能
- 扫码登录 WhatsApp 等消息渠道并查看其状态

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: A React/Next.js visual dashboard for the OpenClaw AI gateway. Every CLI command represented as a visual UI page, wit
> L9: OpenClaw is a self-hosted AI assistant gateway with 35+ CLI commands, 50+ skills, and 20+ messaging channel integrat
> L31: - **Real-time WebSocket** — Direct connection to the OpenClaw gateway protocol (v3)

## 星数曲线

```mermaid
xychart-beta
    title "actionagentai/openclaw-dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e1c63017d817` · [字段定义](../../DATASET.md)*
