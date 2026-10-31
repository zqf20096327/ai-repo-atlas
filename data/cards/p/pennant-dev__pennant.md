# pennant-dev/pennant

⭐ 14 · Swift · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/pennant-dev/pennant) · [官网](https://pennant.dev) · 个人维护

**Mac/iPhone 本地优先的 AI agent 应用：定时任务、审批与电脑操作**

面向终端用户的 agentic 应用：以自然语言下达任务，支持定时 job（cron）、自主目标、在 Chrome 标签与后台操作 Mac（computer use）、编码运行（Claude Code 或自带引擎、以独立 GitHub App 开 PR）、带出处的记忆（本地嵌入模型跑在 Mac GPU）与设备端语音对话。发送/付费/不可逆删除须先经审批卡，Mac 与 iPhone 均可批准。模型任选：OpenAI/Anthropic/Google 等预设、任意 OpenAI 兼容端点、LM Studio/vLLM 本地或 Apple 端上模型。无账号、无遥测，数据存本地单一目录；Apache-2.0。要求 macOS 15+，iPhone 应用需 iOS 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 发送、花费、不可逆删除等动作强制经审批卡，Mac/iPhone 均可批准
- 本地优先：无账号、无遥测，密钥存 Keychain，本地模型时数据不出 Mac
- 本地嵌入模型驱动的带出处记忆与语义检索
- 兼容 SKILL.md 技能格式，可链接现有 Claude Code 技能与 MCP 服务器目录

## 适用场景

- 让 agent 按日程自动处理收件箱分诊、发帖、看护生产环境并修代码
- 通过 iPhone 远程批准 Mac 上 agent 的待审动作
- 用自选模型（含本地 LM Studio/vLLM）驱动编码、电脑操作与研究任务

## 场景标签

`AI 助手` `编码 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Pennant is a free, open-source AI agent that lives on your Mac, with an iPhone companion. Give it jobs in plain word
> L36: - **One chat with Pennant.** The Mac and iPhone apps open on a single conversation with Pennant. It answers what's 
> L71: - **Any model.** Presets for OpenAI, Anthropic, Google, xAI, Mistral, DeepSeek, OpenRouter, Groq and more, any

## 星数曲线

```mermaid
xychart-beta
    title "pennant-dev/pennant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `661c138cc3f0` · [字段定义](../../DATASET.md)*
