# graniet/kheish

⭐ 221 · Rust · Apache-2.0 · 推送 2026-07-26 · [GitHub](https://github.com/graniet/kheish) · [官网](https://kheish.ai) · 个人维护

**长时运行工具型 AI agent 的守护进程式控制平面**

Rust 实现的持久化 agent 运行时与控制平面：调用方（CLI/Slack/webhook/代码）仅提交请求，由守护进程执行并管理会话，运行可在进程重启、审批挂起等中断后从日志恢复。支持 Anthropic/OpenAI/Google/xAI 多提供商路由、多 agent 编排、经纪式短期凭证租约、屏幕/摄像头/麦克风等观测源采集，以及 MCP 工具与 HTTP/SSE 运维接口。通过 cargo 构建单一二进制作为服务端与客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用与执行分离：运行由守护进程持有，调用方崩溃不影响
- 日志化状态与检查点，重启后恢复运行与审批门
- 多提供商路由（Anthropic/OpenAI/Google/xAI）与 MCP 工具
- 经纪式运行时凭证与签名追加式审计记录

## 适用场景

- 需要跨重启、跨审批等待长期运行的 agent 工作流
- 从 Slack、webhook、CLI 等多入口提交并由统一控制平面管理 agent
- 对 agent 外部操作做凭证隔离与审计

## 场景标签

 · 领域:AI agent 基础设施

## 证据(README 行号)

> L5:  Persistent agent runtime and control plane for long-lived, tool-using AI workflows.
> L90: Kheish is organized as a Rust workspace centered around a daemon control plane, a provider-agnostic runtime, an orc

## 星数曲线

```mermaid
xychart-beta
    title "graniet/kheish 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 220 --> 222
    line [221, 221]
```

2026-10-18 221 → 2026-10-22 221（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `dc8ee296804b` · [字段定义](../../DATASET.md)*
