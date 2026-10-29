# LNC0831/oh-my-fpga

⭐ 22 · JavaScript · MIT · 推送 2026-06-09 · [GitHub](https://github.com/LNC0831/oh-my-fpga) · [官网](https://synthpilot.dev) · 个人维护 · 中文 README

**给 Claude Code 的 FPGA 方法论 skill 包：13 个工作流编排 SynthPilot 工具**

SynthPilot MCP 服务器的开源配套 skill 包：SynthPilot 向 AI 暴露约 500 个原子工具来驱动 FPGA 工具链（Vivado），本包在其上叠加纯 markdown 的方法论层，把原子工具编排为一句话可触发的工作流，如时序收敛、CDC 审查、约束编写、RTL 到 bitstream 全流程、Zynq SoC 搭建、ILA 上板调试等 13 个 skill。面向使用 Claude Code 的 FPGA 开发者；以 Claude Code 插件或复制 skill 文件夹方式安装。每个 skill 经多 agent 工厂生成并对抗式审查，含零 LLM 的确定性工具名校验；其他 MCP 客户端可通过 SynthPilot 服务端内置的同源 MCP prompts 使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个命名工作流覆盖时序收敛、CDC 审查、全流程、Zynq 搭建、硬件调试等
- 在 SynthPilot 约 500 个原子工具之上提供 markdown 策略层
- skill 由多 agent 工厂生成，经对抗式审查与零 LLM 工具名确定性校验
- 设计原则要求验证优先、不假装通过、最小安全改动优先

## 适用场景

- 让 AI 按专家流程完成 FPGA 时序收敛或 CDC 审查
- 从零编写 XDC 约束并验证
- 一句话驱动 RTL 到 bitstream 的端到端流程
- 搭建 Zynq SoC 或上板抓波形调试

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: A **free, open** companion skill pack for the SynthPilot MCP
> L15: gives it **methodology** — named, opinionated workflows that turn those primitives into
> L31: These skills orchestrate the **SynthPilot** MCP

## 星数曲线

```mermaid
xychart-beta
    title "LNC0831/oh-my-fpga 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `24f402f288b6` · [字段定义](../../DATASET.md)*
