# sparten11740/mc-blockpilot

⭐ 3 · Java · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/sparten11740/mc-blockpilot) · [官网](https://www.curseforge.com/minecraft/mc-mods/blockpilot) · 个人维护

**让 AI agent 通过 MCP 接口查看和操作 Minecraft 的 mod**

客户端 Minecraft mod，为 AI agent 和脚本提供本地、token 高效的游戏接口：通过 stdio 提供 MCP 服务，agent 获得 run（命令脚本）、screenshot、help 三个工具；同时提供 shell/脚本驱动的命令行协议，覆盖感知（look/find/inv）、移动、交互（mine/place/craft）、GUI、输入、截图录制、性能采样等约 80 条命令，支持断言与等待等脚本语义。支持 Fabric/Forge/NeoForge 及无加载器的原版接入方式，仅监听 127.0.0.1 且带 token。面向 AI 驱动的 mod 开发与脚本化冒烟测试。

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

- 通过 stdio 提供 MCP 服务，agent 获得 run/screenshot/help 三个工具
- 约 80 条游戏命令的脚本语言，支持 wait/assert/if/sub 等控制语义
- 支持 Fabric、Forge、NeoForge 及无 mod loader 的 javaagent 接入
- 世界快照保存/恢复、GameTests 运行、MP4 录制与性能采样

## 适用场景

- 开发 mod 时让 AI agent 代为试玩并做冒烟测试
- 用脚本批量自动化采集截图、日志与性能数据
- 在 CI 中运行游戏内测试并断言结果

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L6: A client-side Minecraft mod that lets AI agents and scripts see and play the game through a fast, token-efficient lo
> L30: **MCP, for AI agents.** The launcher serves MCP over stdio. Add it to your agent once; it keeps working through


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `eaa66f76cf93` · [字段定义](../../DATASET.md)*
