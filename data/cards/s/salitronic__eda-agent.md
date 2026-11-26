# salitronic/eda-agent

⭐ 401 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/salitronic/eda-agent) · [官网](https://salitronic.com/eda-agent) · 个人维护

**让 AI 通过 MCP 驱动 Altium Designer 实时编辑电路设计的服务器**

一个 MCP 服务器，使 AI 或任何 MCP 兼容客户端能够操作正在运行的 Altium Designer 会话，KiCad 与 EasyEDA Pro 作为可选后端。通过 Altium 脚本引擎内的 DelphiScript 轮询循环和基于文件的 IPC 保持实时连接，AI 读取当前打开的设计、回答问题并就地修改。默认后端提供约 600 个工具，覆盖原理图、PCB、元件库、项目和设计代理操作；附带 Altium 内状态窗口与本地 Web 仪表盘（设计审查、lint 审计、交叉探测）。README 标注为实验性，部分工具可能使脚本引擎崩溃，建议先备份设计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 默认 Altium 后端约 600 个工具，覆盖原理图/PCB/库/项目自动化
- 批量调用机制：一次请求最多 200 个条目、合并为一个撤销步骤
- design_lint_report 一次 IPC 通过运行 31 项审计检查
- GUI 驱动能力：通过菜单/对话框/OCR 操作无 API 的 Altium 功能

## 适用场景

- 从文字规格生成原理图与制造文件（Gerber、BOM、pick-and-place）
- 对话式设计审查与引导式重构，边看 AI 边改设计
- 对打开的工程做 BOM 查询、网络连接性问答
- 原理图与 PCB 网表交叉核对，发现 ECO 漂移

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: MCP server that lets an AI (or any MCP-compatible client) **interact with a live Altium Designer session**, with KiC
> L39: - `eda-agent` (Python, launched by your MCP client) sends commands via file-based IPC

## 星数曲线

```mermaid
xychart-beta
    title "salitronic/eda-agent 星数(近 25 点)"
    x-axis ["2026-10-24", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26"]
    y-axis "stars" 260 --> 413
    line [272, 275, 278, 280, 289, 296, 299, 302, 304, 272, 328, 340, 349, 355, 357, 364, 365, 370, 373, 379, 382, 390, 392, 393, 401]
```

2026-10-24 272 → 2026-11-26 401（+129）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `76bd3ad82c55` · [字段定义](../../DATASET.md)*
