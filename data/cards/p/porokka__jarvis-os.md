# porokka/jarvis-os

⭐ 25 · Python · MIT · 推送 2026-08-11 · [GitHub](https://github.com/porokka/jarvis-os) · 个人维护

**本地多模型个人 AI 助理系统：语音/Telegram/HUD 交互与家庭自动化**

面向个人用户的完全本地 AI 助理（J.A.R.V.I.S OS）：通过语音唤醒、Next.js 全息 HUD、Telegram、移动端 App 多渠道交互；采用 4-Pass 记忆路由（gemma4）、多模型分层（qwen3/gemma）、ReAct agent 循环与 8-10 步人工审批的 agentic 计划系统执行多步编码任务。记忆层为 MemPalace 向量库 + Obsidian vault + Redis 工作记忆。集成 35+ 技能模块，覆盖编码、git、邮件/电话（Twilio）、FLUX 文生图，以及 Denon/Hue/LG TV 等家庭自动化；可选 Claude API 云端模式（claude_proxy 模拟 Ollama API）。限定 NVIDIA GPU + CUDA、WSL2/Ubuntu、Node.js 20+、Python 3.12+、Ollama、Redis 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4-Pass 记忆路由 + 多模型分层（Fast/Reason/Code/Deep/Cloud）
- 带自愈与版本化的 agentic 计划系统：人工审批 → 分级 staging 管线
- MemPalace 向量记忆 + Obsidian vault（2000+ 记忆）+ Redis 工作记忆
- 35+ 模块化技能：编码/git/邮件/FLUX 文生图/家庭自动化/UE5.8 MCP

## 适用场景

- 用语音或 Telegram 让 AI 助理代我执行多步编码项目并审批结果
- 把 Obsidian 作为长期记忆库做个人助理
- 通过 MCP 控制 Unreal Engine 编辑器与 MetaHuman 表情
- 集中控制家庭影音设备（Denon/Hue/LG TV/Shield）

## 场景标签

`AI 助手` `Agent 记忆` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Just A Rather Very Intelligent System** — A fully local AI assistant with modular skill architecture, agentic plan
> L22: - **Voice I/O** — Wake word "Hey JARVIS", Whisper STT, Kokoro/Orpheus TTS with 5.1 center-channel output
> L38: User Input (Voice / HUD / Telegram / API)

## 星数曲线

```mermaid
xychart-beta
    title "porokka/jarvis-os 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ad16ee881463` · [字段定义](../../DATASET.md)*
