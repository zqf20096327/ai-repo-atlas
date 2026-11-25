# im4codes/imcodes

⭐ 965 · TypeScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/im4codes/imcodes) · [官网](https://im.codes) · 个人维护

**给 AI coding agent 提供共享记忆、受监督执行与跨 agent 审计的消息层**

IM.codes 将支持的机器注册为受限的 Controlled Nodes，让授权 agent 执行带范围限制的命令、文件传输与 Computer Use 操作，并提供浏览器远程桌面供人接管。它为 Claude Code、Codex、Gemini CLI、Copilot、Cursor、Qwen 等编码 agent 提供统一记忆层（本地存储、可选云同步、pgvector 多语言召回）、托管的 stdio MCP 工具面（记忆检索/写入、agent 消息、cron 调度）、逐轮受监督执行与自动审计返工循环，以及 OpenSpec 变更的端到端交付流水线。README 声明为个人开源项目，无 SLA 与稳定性保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跨 provider 的共享 Agent 记忆：最终输出物化、多语言嵌入召回、自动注入会话
- 托管的 stdio MCP 服务器：memory/Send/Cron 工具绑定运行时会话身份
- 受监督执行：逐轮完成度分类与 supervised_audit 审计返工循环
- OpenSpec Auto Deliver：审计评分与 PASS/REWORK/BLOCKED 门控

## 适用场景

- 离开工位后从手机/网页继续查看和推进 agent 编码会话
- 让多个 agent 复用已完成工作的记忆与项目上下文
- 为 OpenSpec 变更配置带审计与返工门控的自动交付流程
- 团队内共享 workspace 级记忆并审计跨模型工作

## 场景标签

`Agent 记忆` `编码 Agent` `GUI 自动化` · 领域:Agent 开发

## 证据(README 行号)

> L13: Alongside machine control, IM.codes gives coding agents one shared memory layer and one managed MCP tool surface ac
> L52: It is not another AI IDE or a generic remote terminal. It is the messaging, memory, and review layer around termina

## 星数曲线

```mermaid
xychart-beta
    title "im4codes/imcodes 星数(近 9 点)"
    x-axis ["2026-10-23", "2026-10-30", "2026-10-31", "2026-11-08", "2026-11-10", "2026-11-15", "2026-11-18", "2026-11-21", "2026-11-25"]
    y-axis "stars" 960 --> 966
    line [965, 964, 965, 961, 962, 963, 964, 965, 965]
```

2026-10-23 965 → 2026-11-25 965（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `4b43953adb26` · [字段定义](../../DATASET.md)*
