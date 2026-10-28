# JasonYANG170/wch-dev-skill

⭐ 24 · C · 推送 2026-10-04 · [GitHub](https://github.com/JasonYANG170/wch-dev-skill) · 个人维护 · 中文 README

**WCH 全系列 MCU 固件开发 AI Skill：让 Agent 生成规范嵌入式代码**

面向沁恒（WCH）微控制器固件开发的 AI Skill 包：通过 git clone 安装到 Claude Code、QwenCode、OpenCode 等 AI Agent 的 skills 目录后，Agent 按九步工作流（识别芯片→匹配 recipes→查 API→避陷阱→验证→执行→构建→调试）生成符合 WCH SDK 规范的代码。覆盖 10 个芯片家族、35+ 芯片型号，含 RISC-V/ARM/ARM7TDMI/8051 四种架构的 API 速查、EXAM 例程与常见陷阱文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 10 个芯片家族、35+ 芯片型号与 4 种架构
- 九步工作流：芯片识别、recipes 匹配、API 查询、陷阱检查、例程适配
- BLE 全角色、以太网、USB-PD、USB 3.0、LCD/NFC 等场景的调用链与代码模板
- 兼容 Claude Code / QwenCode / OpenCode 的 skills 目录规范

## 适用场景

- 让 AI Agent 按 WCH SDK 规范生成指定芯片的固件代码
- 开发 BLE 外设、USB-PD、以太网等嵌入式场景时获取调用链与模板
- 查阅各架构常见错误与陷阱以减少调试成本

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: 统一的 WCH（南京沁恒微电子）全系列微控制器固件开发 AI Skill。让 AI Agent 自动生成符合 WCH SDK 规范的嵌入式代码，覆盖 35+ 芯片家族、10 大架构分组。
> L44: > **Claude Code**
> L75: Skill 定义了一套工作流，AI Agent 在生成固件代码时会遵循：

## 星数曲线

```mermaid
xychart-beta
    title "JasonYANG170/wch-dev-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b95190ff0d99` · [字段定义](../../DATASET.md)*
