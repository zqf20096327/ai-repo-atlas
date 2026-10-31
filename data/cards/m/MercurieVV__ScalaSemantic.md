# MercurieVV/ScalaSemantic

⭐ 22 · Scala · MIT · 推送 2026-10-29 · [GitHub](https://github.com/MercurieVV/ScalaSemantic) · [官网](https://mercurievv.github.io/ScalaSemantic/) · 个人维护

**给 AI 编码代理的 Scala 语义分析 MCP 服务器**

基于 SemanticDB 编译器输出的 MCP server，向 AI 编码代理（Claude Code、Codex、Gemini CLI、Cline 等）提供编译器解析级的 Scala 事实：精确符号查找、find-usages、类层次、隐式解析与调用路径，替代 grep 文本搜索。支持 Scala 2.13.* 与 3.*.*，兼容任何 sbt/Mill/Gradle 项目。提供 curl/PowerShell 一键安装脚本，仅需 java；可选安装 guard hook 拦截对 .scala 文件的 grep/cat/Read 并引导代理使用 MCP 工具，默认不安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个 MCP 工具：find_symbol、find_usages、class_hierarchy、resolve_implicits、call_path 等
- 数据来自编译器生成的 SemanticDB，非文本搜索
- 一键安装脚本支持 Unix 与 PowerShell，可选 Claude guard hook
- 官方测量称语义工具比 grep 节省约 90% token

## 适用场景

- 在 Claude Code 等 MCP 代理中查询 Scala 方法的精确调用者
- 解析 trait 的全部子类型或 given 隐式实例
- 追踪方法间调用路径与隐式解析链

## 场景标签

 · 领域:开发者工具/代码智能

## 证据(README 行号)

> L8: **ScalaSemantic** is an MCP server that gives AI coding agents compiler-resolved Scala facts — exact symbols, types,
> L10: Works with Scala 2.13.* and 3.*.*, any sbt/Mill/Gradle project, and any MCP-compatible agent (Claude Code, Codex, G

## 星数曲线

```mermaid
xychart-beta
    title "MercurieVV/ScalaSemantic 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-31 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `efeb99d71330` · [字段定义](../../DATASET.md)*
