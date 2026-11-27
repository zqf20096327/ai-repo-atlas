# directionally-local/autopilot

⭐ 222 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/directionally-local/autopilot) · [官网](https://directionallylocal.com/autopilot) · 组织维护

**终端内开源编码 agent 与 SDK：自带密钥接入 25+ 模型提供方**

运行在终端的编码 agent，提供交互式会话与 headless SDK（createAgentSession API 与 JSONL-over-stdio RPC）两种形态。接入方式为自带密钥（OpenRouter、OpenAI、Anthropic、DeepSeek 等 25+ 提供方）或免费额度；支持本地模型后端（vLLM/OpenAI 兼容服务器）。关键机制包括 plan/edit/auto 三种权限模式、破坏性操作守卫与 /undo 恢复点、沙箱子 agent、SQLite+嵌入的跨会话记忆、LSP/MCP 扩展与每轮计费成本显示。安装方式为 curl 脚本（经 dl 安装器）、npm、Homebrew 或 npx 免安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自带密钥直连所选提供方，调用不经代理；OpenRouter 为推荐默认
- plan/edit/auto 权限模式与凭据文件读取拦截、内网地址访问确认
- 破坏性操作前保存仓库外恢复点，/undo 可还原，/audit 输出风险报告
- 沙箱子 agent、长时无人值守运行（checkpoint 恢复与预算控制）、LSP+MCP 扩展

## 适用场景

- 在终端里让 agent 读取、编辑代码库并执行工具调用
- 用自己的 API key 在本地硬件上运行私有模型驱动编码 agent
- 通过 headless SDK 将 agent 会话嵌入自己的程序或流水线
- 从 Claude Code/Cursor 等导入已有配置与 MCP 服务器迁移使用

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L14:  The open-source coding agent inside dl. It doesn't ask permission.
> L65: - **Headless SDK** — Programmatic `createAgentSession` API and JSONL-over-stdio RPC mode for building on top of aut
> L31: On the free tier, model calls go through Directionally Local's free tier service to its model host; it keeps usage 

## 星数曲线

```mermaid
xychart-beta
    title "directionally-local/autopilot 星数(近 12 点)"
    x-axis ["2026-10-29", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-27"]
    y-axis "stars" 173 --> 226
    line [177, 194, 216, 217, 218, 220, 221, 220, 221, 220, 222, 222]
```

2026-10-29 177 → 2026-11-27 222（+45）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `6b497886d8b3` · [字段定义](../../DATASET.md)*
