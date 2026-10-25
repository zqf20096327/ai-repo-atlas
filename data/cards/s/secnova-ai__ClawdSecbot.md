# secnova-ai/ClawdSecbot

⭐ 93 · Go · GPL-3.0 · 推送 2026-07-23 · [GitHub](https://github.com/secnova-ai/ClawdSecbot) · [官网](https://bot.secnova.ai) · 组织维护 · 中文 README

**本地 AI Bot 终端 agent 的安全防护层：代理、沙箱与审计**

面向桌面与 WebUI 场景的 Bot 型终端 AI agent（如 Openclaw）安全防护软件：位于 Bot 与 LLM 服务之间，拦截 API 流量、用 LLM/ReActAgent 分析与 guard 技能做允许/阻断/脱敏/确认决策；提供资产发现、风险评估、OS 级沙箱（macOS Seatbelt / Linux LD_PRELOAD / Windows MinHook）、OpenAI 兼容协议转换（支持 8 家 LLM 提供商）与审计日志。架构为 Flutter 前端 + Go 共享库（FFI），SQLite 存储，插件化支持不同 Bot 类型。Windows 侧需管理员权限（UAC 拒绝即退出）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Bot↔LLM 流量代理，对输入/ToolCall/输出做允许、阻断、脱敏或确认决策
- OS 级沙箱强制：macOS Seatbelt / Linux LD_PRELOAD hook / Windows MinHook，旁路自动恢复
- OpenAI 兼容协议翻译，支持 8 家 LLM 提供商（含流式、推理、工具调用）
- 插件化 BotPlugin 接口与完整审计日志（请求、工具调用、风险、token 用量）

## 适用场景

- 我在本机跑 Openclaw 等 AI Bot，想拦截危险操作再做提示词注入与风险检测
- 想给 Bot 进程加 OS 级沙箱并留存完整审计记录
- 想用浏览器远程管理部署在 Linux 上的 Bot 安全策略

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: ClawSecbot monitors and secures local AI Bot agents (such as Openclaw) running on your machine. It acts as a protec
> L31: ClawSecbot sits between the Bot and LLM provider. It checks user input, ToolCall, ToolCallResult, and final output 

## 星数曲线

```mermaid
xychart-beta
    title "secnova-ai/ClawdSecbot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 92 --> 95
    line [94, 93, 93]
```

2026-10-18 94 → 2026-10-25 93（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ad2c1c5114ca` · [字段定义](../../DATASET.md)*
