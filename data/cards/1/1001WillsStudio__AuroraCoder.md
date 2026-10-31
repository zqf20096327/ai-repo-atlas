# 1001WillsStudio/AuroraCoder

⭐ 20 · Python · MIT · 推送 2026-08-27 · [GitHub](https://github.com/1001WillsStudio/AuroraCoder) · 组织维护 · 中文 README

**自主 AI 编程 agent：Docker 沙箱内读写代码、跑命令、控 GUI**

在 Docker 容器内运行的自主编程 agent，主要调用 DeepSeek V4 Pro（也支持 GLM-5.1、OpenCode Go），通过原生 OpenAI function calling 驱动。它能读取代码库、写代码、执行终端命令、搜索网页、派发子 agent，并经内置 VNC 桌面操作 GUI 应用；GPU 变体支持 NVIDIA 直通以运行 PyTorch/vLLM 本地模型。核心机制包括可变工具响应（每次编辑后重读磁盘、折叠历史状态块）、宽松接收+严格校验的 edit_file 门控，以及只读工具并行执行。提供一键启动器、开发脚本与实验性 npm 安装三种途径；npm 方式无 Docker 隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 可变工具响应：编辑后重读磁盘并折叠历史状态块，模型始终看到当前文件状态
- edit_file 两阶段校验：锚点 ±3 行宽松匹配，任一失败则整批不落盘
- 只读工具（read/grep/浏览器/搜索）并行执行，写工具串行
- Docker 沙箱 + 内置 VNC 桌面 + ToolStore 管理 MCP 服务器与技能

## 适用场景

- 让 agent 在隔离沙箱里自主完成代码修改、命令执行与调试
- 需要 agent 操作 GUI 应用的自动化任务（通过 VNC 桌面观察）
- 用 NVIDIA GPU 直通在本地跑 vLLM 模型配合 agent 工作
- 通过多实例模式并行运行多个 agent

## 场景标签

`编码 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: **AuroraCoder** is a state-of-the-art autonomous AI coding agent powered primarily by **DeepSeek V4 Pro** (GLM-5.1 a
> L84: |⚙️ **Agent Backend**|`http://localhost:8080`|Stateless agent loop + tool execution|
> L86: |🖱️ **VNC Desktop**|`http://localhost:6080`|Live Linux desktop for GUI apps|

## 星数曲线

```mermaid
xychart-beta
    title "1001WillsStudio/AuroraCoder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `c27c5c684e45` · [字段定义](../../DATASET.md)*
