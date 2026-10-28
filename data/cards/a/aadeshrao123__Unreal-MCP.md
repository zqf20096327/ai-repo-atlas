# aadeshrao123/Unreal-MCP

⭐ 39 · C++ · MPL-2.0 · 推送 2026-08-06 · [GitHub](https://github.com/aadeshrao123/Unreal-MCP) · [官网](https://codefizz.dev) · 个人维护

**用 AI 客户端控制 Unreal Engine 5 编辑器的 MCP/CLI 桥**

在 UE5 编辑器内运行 C++ 插件并通过 TCP 暴露 288 个命令，覆盖蓝图、材质、Niagara、StateTree、数据表、Actor、输入、UMG 与性能分析；提供两种入口：npm 安装的 CLI（单二进制）与 pip 安装的 MCP Server（Python 3.10+），可接入 Claude Code、Cursor、Windsurf、VS Code、Gemini CLI、Rider、Zed、Amazon Q 等 MCP 客户端。本仓库为社区版，功能稳定但不再新增子系统；新功能进入商业版 CodeFizz Editor Agent（900+ 命令）。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 288 个命令、15 个类别，覆盖蓝图/材质/Niagara/StateTree/数据表/UMG 等
- CLI 与 MCP Server 两种入口，同一 C++ 插件
- 支持 8 种 MCP 客户端配置（Claude Code/Cursor/Windsurf/VS Code 等）
- 社区版稳定但停止新功能开发，后续进入商业版 CodeFizz Editor Agent

## 适用场景

- 在终端里用自然语言让 AI 创建蓝图、材质和 Niagara 特效
- 用 Cursor/Claude Code 等编辑器代理直接操作 UE 编辑器
- 通过 CLI 批量管理资产与数据表、做性能 trace 分析

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **Control the Unreal Engine 5 editor from Claude Code, Cursor, Windsurf, or any MCP client.**
> L91: The C++ plugin runs inside the editor and exposes 288 commands over TCP. The CLI and MCP server are two different f
> L55: |**Works with**|Claude Code (via Bash)|Claude Code, Cursor, Windsurf, VS Code, Gemini CLI, Rider, Zed, Amazon Q|

## 星数曲线

```mermaid
xychart-beta
    title "aadeshrao123/Unreal-MCP 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 38 --> 41
    line [40, 39, 39]
```

2026-10-18 40 → 2026-10-28 39（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `15c4028dfdcc` · [字段定义](../../DATASET.md)*
