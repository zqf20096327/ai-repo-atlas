# veecle/chiplab

⭐ 18 · MIT · 推送 2026-10-26 · [GitHub](https://github.com/veecle/chiplab) · [官网](https://veecle.ai/) · 组织维护

**让 AI 编码 agent 在虚拟芯片上运行与验证固件的托管 MCP 服务**

由 Veecle GmbH 运营的托管 MCP 服务：AI 编码 agent 通过 HTTP 连接后上传编译好的 ELF 固件，在真实微控制器（当前支持 STM32 与 Nordic 板卡）的虚拟实例上运行，并同步读回 UART 输出；运行时长限定固定虚拟时间。仓库为每块受支持板卡提供按框架分组的示例（bare-metal Rust、Embassy、Zephyr、FreeRTOS、ThreadX），并为 Claude Code、Claude Desktop、Cursor、VS Code、Codex 给出接入配置。需在 veecle.ai 注册免费账号，首次使用经浏览器登录。项目自述处于早期开放开发阶段，当前可跑 Hello world 示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 构建 ELF→上传→虚拟板卡运行→读回 UART 的完整回路
- 支持 bare-metal Rust/Embassy/Zephyr/FreeRTOS/ThreadX 多框架示例
- HTTP MCP 服务器，兼容标准 mcpServers 配置与 Claude Code/Codex 等
- 运行同步返回且限定固定虚拟时间

## 适用场景

- 让 AI 编码 agent 在无实体硬件的情况下验证嵌入式固件
- 在 STM32/Nordic 虚拟板卡上跑通 Hello world 级示例
- 把固件构建-烧录-串口读回的流程交给 agent 驱动

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: Chiplab is a hosted MCP service.
> L9: Your AI coding agent connects to it, uploads compiled firmware, runs it on a virtual instance of a real microcontrol
> L29: Chiplab is an HTTP MCP server at `https://chiplab.veecle.ai/mcp`.

## 星数曲线

```mermaid
xychart-beta
    title "veecle/chiplab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `520532f51020` · [字段定义](../../DATASET.md)*
