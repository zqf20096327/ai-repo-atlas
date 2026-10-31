# ivan-magda/swift-claw

⭐ 15 · Swift · MIT · 推送 2026-10-30 · [GitHub](https://github.com/ivan-magda/swift-claw) · 个人维护

**单二进制 Swift 常驻个人 AI 助手，经 Telegram 交互**

纯 Swift 实现的常驻守护进程 clawd，将私有 Telegram 机器人与用户自选的任意 OpenAI 兼容端点配对，提供持久记忆（SQLite）、定时与主动任务、语音转写、Markdown 技能文件、MCP 工具接入，以及 Codex 编码任务委派。工具调用经策略引擎管控：文件写入、代码执行等需在 Telegram 中点按审批，web_fetch 设有 SSRF 门。密钥以 AES-GCM 加密存储，仅允许清单内 Telegram ID 会话。macOS/Linux 通过安装脚本或源码构建部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 Swift 二进制守护进程，状态存储于本机 SQLite 与 Markdown
- 任意 OpenAI 兼容端点，clawd auth login 可用 ChatGPT 订阅运行模型
- 工具调用需 Telegram 点按审批，含 SSRF 门与提示注入防护
- SKILL.md 技能文件与 MCP 服务器工具接入

## 适用场景

- 在 Telegram 中长期使用记住我个人偏好的 AI 助手
- 让助手按日程自动执行并从纠错反馈中学习
- 把编码任务委派给本机 Codex 并在聊天中审批

## 场景标签

`AI 助手` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: **Your always-on personal AI assistant. One pure-Swift daemon on hardware you own.**
> L15: `clawd` pairs a private Telegram bot with the LLM of your choice. It remembers what you
> L43: - **Bring your own model.** Any OpenAI-compatible endpoint works, and `clawd auth login`

## 星数曲线

```mermaid
xychart-beta
    title "ivan-magda/swift-claw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `897657270730` · [字段定义](../../DATASET.md)*
