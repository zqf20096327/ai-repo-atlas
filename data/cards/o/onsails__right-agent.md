# onsails/right-agent

⭐ 36 · Rust · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/onsails/right-agent) · [官网](https://right-agent.ai/) · 个人维护

**通过 Telegram 对话驱动的沙箱化 AI agent 运行器**

用户在 Telegram 中以消息方式驱动 AI agent：为每个 agent 分配独立沙箱，凭证保存在沙箱之外，模型无法读取凭证字节或携带其访问外网。当前每个 agent 运行于 Claude Code（claude -p），因此需要 Claude 订阅，README 声明多提供商支持在开发中。通过 install.sh 脚本安装 CLI，运行 right up 启动，随后在 Telegram 中管理 agent、通过 /mcp 与 /providers 打开控制面板。基于 microsandbox 与 process-compose 构建，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个 agent 独立沙箱，凭证存于沙箱外，模型无法读取
- Telegram 消息界面管理 agent，/mcp 与 /providers 控制面板
- 当前运行于 Claude Code（claude -p），需 Claude 订阅，多提供商支持开发中

## 适用场景

- 在手机上通过 Telegram 指挥 agent 执行任务
- 给 agent 真实凭证但不暴露凭证本身给模型
- 需要限制 agent 网络与权限访问的场景

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: right agent is an ai agent you run by messaging it. you give it real credentials
> L16: > today every agent runs on Claude Code (`claude -p`), so you need a Claude

## 星数曲线

```mermaid
xychart-beta
    title "onsails/right-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 34 --> 37
    line [35, 36, 36]
```

2026-10-18 35 → 2026-10-27 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fbd8d20557c6` · [字段定义](../../DATASET.md)*
