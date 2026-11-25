# oraios/serena

⭐ 31,647 · Python · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/oraios/serena) · [官网](https://oraios.github.io/serena) · 组织维护

**给编码 agent 提供语义级代码检索/编辑工具的 MCP 服务器**

Serena 通过 MCP 协议为 AI 编码客户端扩展工具集：基于语言服务器（LSP）或 JetBrains 插件两种后端，提供符号级查找、引用查找、重命名、符号编辑与调试工具，支持 40 余种编程语言，并附带跨会话记忆系统与多层 YAML 配置。README 说明 LLM 负责编排工具调用，Serena 本身不执行生成；主体以 GPL-3.0-or-later 许可，JetBrains 插件后端为付费组件。安装依赖 uv，命令为 uv tool install serena-agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.5 天,年发版 14,244 位贡献者
- 涨星:近 1 天 **+39**(自 20261016 起算)
- 平台:— · 协议:MCP

## 能力要点

- 基于 LSP 的符号级检索与重构工具，支持 40+ 编程语言
- 通过 MCP 协议接入 Claude Code、Codex、JetBrains IDE 等客户端
- JetBrains 插件后端提供移动/内联重构与断点调试能力
- 跨会话记忆系统与多层可组合的 YAML 配置

## 适用场景

- 让编码 agent 在大型代码库中做跨文件重命名与引用查找
- 为现有 MCP 客户端补充 IDE 级代码理解工具
- 多语言 monorepo 中的符号级导航与编辑
- 长期 agent 工作流中跨会话共享项目知识

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L6: * Serena provides essential **semantic code retrieval, editing, refactoring and debugging tools** that are akin to a
> L58: Serena can extend the functionality of your existing AI client via the **model context protocol (MCP)**.
> L66: To connect the Serena MCP server to your client, you either

## 星数曲线

```mermaid
xychart-beta
    title "oraios/serena 星数(近 27 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 30508 --> 31750
    line [30611, 30655, 30678, 30703, 30736, 30766, 30810, 30849, 30875, 30948, 30982, 30678, 31210, 31267, 31301, 31330, 31360, 31377, 31405, 31448, 31482, 31511, 31540, 31556, 31583, 31610, 31647]
```

2026-10-23 30,611 → 2026-11-25 31,647（+1,036）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `1566420cd786` · [字段定义](../../DATASET.md)*
