# al-nafisah/fpga-project-analyzer

⭐ 19 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/al-nafisah/fpga-project-analyzer) · [官网](https://al-nafisah.github.io/fpga-project-analyzer/) · 个人维护

**供 AI 编程代理解析与审查 Vivado/Zynq/PYNQ 工程的技能工具**

以 Claude Code 插件与 MCP server 形式提供的 FPGA 工程分析工具：读取 Vivado 工程文件、RTL、约束与 PYNQ 相关文件，生成可下钻的离线 HTML 框图（模块设计→层次→RTL→寄存器，按时钟域着色），并检查时钟域交叉、未约束引脚、复位极性、地址映射、PYNQ bit 文件名错误等问题，定位到 file:line；可压缩失败构建日志并生成 Markdown 设计文档。离线运行，Vivado 可选（缺失时 RTL 仅结构化读取，部分时钟路径可能无法追踪）。支持 Claude Code、Cursor、Codex、Gemini CLI、Copilot 等 MCP/技能型代理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成可点击下钻的离线 HTML 框图，导线按时钟域着色
- 时钟域交叉/未约束引脚/复位极性/地址映射/PYNQ 检查，输出 file:line
- 压缩失败 Vivado/PetaLinux 构建日志为关键行
- 以 Claude Code 插件与 MCP server 分发，离线运行

## 适用场景

- 让 AI 代理解释我的 FPGA 工程结构并画框图
- 审查时钟域交叉等时序报告未暴露的硬件问题
- 诊断 Vivado 构建失败原因并给出修复方案

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3:  An AI agent skill that explains and reviews Vivado, Zynq and PYNQ projects - visually.
> L6: Claude Code plugin
> L7: MCP server
> L45:  Any other MCP-capable agent works the same way. Agents that load `SKILL.md` skills can use `skills/` directly.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8d54b7c5335c` · [字段定义](../../DATASET.md)*
