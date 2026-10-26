# feibi-mochi/deepseek-harness-control-center

⭐ 75 · JavaScript · MIT · 推送 2026-09-09 · [GitHub](https://github.com/feibi-mochi/deepseek-harness-control-center) · 个人维护 · 中文 README

**DeepSeek Harness 插件：余额/用量/峰谷计费监控与多账户管理**

面向 DeepSeek Harness（DSH）宿主的本地优先插件：在对话输入框旁显示官方 DeepSeek 余额、会话成本估算（本地估算非官方账单）、v4 峰谷时段环形时钟、Z.ai Coding Plan 配额监控，以及第三方 token 用量。支持加密多账户切换（Windows DPAPI / 其他平台 AES-GCM）、低余额提醒、完成提醒、本地用量台账（最长 365 天）、自定义第三方分时计价与官方充值页跳转。通过 dsh plugin 命令从 npm 或 GitHub 安装。限制：钱包 UI 目前以中文为主；成本为本地估算，非官方发票。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 官方 DeepSeek 余额实时刷新与会话成本本地估算（含峰谷分时）
- 加密多账户切换：密钥经 DPAPI/AES-GCM 加密存储，切换后下一请求即生效
- 本地用量台账最长 365 天/2 万事件，不存储提示词或回复
- 低余额与对话完成提醒、浮窗/停靠/缩放等布局控制

## 适用场景

- 对话中随时查看 DeepSeek 余额与本次会话花费
- 在多个 DeepSeek 账户间加密切换并分别计费
- 按峰谷时段与自定义第三方价格核对 API 成本
- 跟踪 Z.ai Coding Plan 的 5 小时与月度配额余量

## 场景标签

 · 领域:LLM 成本监控/账户管理

## 证据(README 行号)

> L9: **DeepSeek Harness monitoring, alerts, recharge, and session control center.**
> L15: > A local-first companion that keeps account status, per-conversation usage, completion reminders, official recharg
> L29: - **Official DeepSeek** — live balance (60s global refresh with fast boot retries), an estimated current-session co

## 星数曲线

```mermaid
xychart-beta
    title "feibi-mochi/deepseek-harness-control-center 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-26 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `320c08fb2c15` · [字段定义](../../DATASET.md)*
