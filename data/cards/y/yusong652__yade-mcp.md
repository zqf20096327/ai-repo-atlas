# yusong652/yade-mcp

⭐ 15 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/yusong652/yade-mcp) · [官网](https://pypi.org/project/yade-mcp/) · 个人维护 · 中文 README

**让 AI agent 通过 MCP 直接运行 YADE 离散元仿真的服务器**

基于 Model Context Protocol 的 MCP server，将 Claude Code、Codex CLI、Gemini CLI 等 agent 客户端接入开源离散元引擎 YADE：提供 7 个工具，包括浏览与 BM25 检索 YADE Python API、在活动的 YADE 进程中执行 Python、以后台任务提交长仿真并查询/中断任务、读取控制台输入。执行类工具需在 YADE 内安装 yade-mcp-bridge 并在会话中启动（默认监听 9002 端口）。任务脚本、输出与状态跨会话留档，支持 Docker 容器场景绑定全部接口。需 Python 3.10+ 与已安装的 YADE。

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

- 在活动 YADE 进程中执行 Python，状态跨调用保持，仿真运行中可读中间结果
- 后台任务生命周期：提交、追踪输出、在迭代边界中断、修复后重交，任务排队逐个执行
- 无需 bridge 的离线 API 文档工具：类树遍历与 BM25 关键词检索
- 任务历史跨会话留档；控制台输入可进入 agent 上下文

## 适用场景

- 用自然语言让 agent 搭建三轴压缩等 DEM 仿真并绘图
- 让 agent 排队提交多阶段仿真流水线并跟踪各任务状态
- 在 YADE 控制台与 agent 之间并行协作、排查报错

## 场景标签

 · 领域:科学计算/岩土工程 DEM 仿真

## 证据(README 行号)

> L16: **yade-mcp** connects AI agents to YADE, the open-source discrete element method engine, through the Model Context 
> L49: - **An AI agent**: Claude Code, Codex CLI, Gemini CLI, or any MCP-capable client

## 星数曲线

```mermaid
xychart-beta
    title "yusong652/yade-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cdb7db2f756b` · [字段定义](../../DATASET.md)*
