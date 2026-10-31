# Razee4315/NetLogo-MCP

⭐ 27 · Python · MIT · 推送 2026-08-01 · [GitHub](https://github.com/Razee4315/NetLogo-MCP) · [官网](https://razee4315.github.io/NetLogo-MCP/) · 个人维护

**让 AI 助手通过对话创建、运行、分析 NetLogo 仿真的 MCP 服务器**

面向 Claude Code、Cursor、Windsurf 等 11 种 MCP 客户端的 NetLogo 桥接服务器：AI 通过 25 个工具用自然语言编写 NetLogo 模型（含滑块/开关等界面组件）、运行仿真并以 markdown 表格收集逐 tick 数据、执行 BehaviorSpace 并行参数扫描、导出视图 PNG、检索并安全运行 CoMSES 同行评审模型库中的模型。默认以 GUI 模式启动 NetLogo 窗口，也支持 CI/服务器用的 headless 模式。前提为 Python 3.10+、JDK 11+ 与手动下载的 NetLogo 7.0+，Docker 镜像内置 headless NetLogo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25 个 MCP 工具：建模、运行、BehaviorSpace 参数扫描、视图导出、世界状态检查
- CoMSES Net 集成：搜索并运行最大同行评审 ABM 模型库中的模型
- GUI/headless 双模式，JVM 惰性启动（首次调用 30-60 秒）
- 内置 NetLogo 原语与 6→7 过渡指南作为 MCP 资源

## 适用场景

- 用自然语言让 AI 生成并运行捕食者-猎物等个体基建模仿真
- 在 CI 或服务器上无头跑 BehaviorSpace 参数扫描实验
- 教学或研究中通过对话检索和复现 CoMSES 上的 ABM 模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: The first MCP (Model Context Protocol) server for NetLogo — enabling AI assistants to create, run, and analyze agen
> L12: **Works with:** Claude Code, Claude Desktop, Cursor, Windsurf, VS Code (Copilot), Cline, Continue, Roo Code, Zed, O
> L26:  You → AI Assistant → NetLogo MCP Server → NetLogo (GUI or headless JVM)

## 星数曲线

```mermaid
xychart-beta
    title "Razee4315/NetLogo-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fd7f9c6e1361` · [字段定义](../../DATASET.md)*
