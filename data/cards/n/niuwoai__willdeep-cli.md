# niuwoai/willdeep-cli

⭐ 17 · Rust · NOASSERTION · 推送 2026-10-31 · [GitHub](https://github.com/niuwoai/willdeep-cli) · [官网](https://willdeep.com) · 个人维护 · 中文 README

**自托管可审计 AI Coding Agent，改动可追溯、子 Agent 退出码裁决**

Rust 实现的自托管 AI 编程 Agent：单个二进制内含常驻 Runtime Daemon，撑起 TUI、浏览器与手机三端界面，任务跨轮次、跨重启持续运行。每行改动归属到具体 Agent 与工具调用，子 Agent 工作由 Runtime 执行验证命令、以退出码裁决，另有五层闸门（工作区策略、静态规则、AI 判官、OS 围栏、hooks）、检查点回退、带 token 预算与验收清单的长任务目标。支持 OpenAI Chat Completions、Responses、Anthropic Messages 三种线格式接入任意端点，用量与反馈账本存本地。边界：不含 Computer Use/Browser Use，Web 模式单用户无应用层鉴权，OS 围栏不限制读取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Diff 快照将每行改动归属到 Agent 与工具调用，可导出审计报告
- 子 Agent 验证由 Runtime 执行、退出码为唯一裁决，测试块逐字比对防作弊
- 常驻 Daemon 任务跨重启累计，/goal 带 token 预算与验收清单
- 五层闸门：工作区策略/静态规则/AI 判官/macOS Seatbelt 与 Linux bubblewrap 围栏/hooks

## 适用场景

- 在数据不出机房的环境里用自有 GPU 与开源权重跑编程 Agent
- 需要向安全评审逐条交代 Agent 改动与审批记录的团队
- 把小模型编派为子 Agent 干活、用退出码验证产出
- 长任务跑在后台，终端/浏览器/手机三端接管与审批

## 场景标签

`编码 Agent` `多智能体` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L5: 自托管的 AI Coding Agent。模型可以不出国，每一行改动能追溯到是哪个 Agent、哪次工具调用改的，小模型交上来的活由退出码裁决而不是自我声明，检查点回退把对话和文件一起退回去。目标（`/goal`）是带 token 
> L7: > **WillDeep** is a self-hosted AI coding agent for people who have to answer for what the agent did: every changed 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-01 · 置信度 high · 依据 README sha `0d9b650adb2a` · [字段定义](../../DATASET.md)*
