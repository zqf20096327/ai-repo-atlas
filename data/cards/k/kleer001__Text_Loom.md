# kleer001/Text_Loom

⭐ 23 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kleer001/Text_Loom) · 个人维护

**面向文本处理的节点式可视化编程工具，LLM 集成**

以字符串与字符串列表为基础数据类型的节点式文本处理工具：通过连接节点构建工作流（读文件→查询 LLM→拆分/合并→保存），提供五种界面——终端 TUI、Web GUI、Python REPL、FastAPI、批处理。内置 MCP 服务器，可让 LLM 助手以对话方式创建并执行工作流；支持主流 LLM API 与本地模型，可离线自托管（<50MB）。安装需 Python 3.8+，GUI 模式另需 Node.js 18+ 与 npm。

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

- 节点式文本工作流：创建文本→读文件→查询 LLM→拆分/合并列表→循环→保存
- 五种界面共用同一核心：TUI/GUI/REPL/API/批处理
- 内置 MCP 服务器，LLM 助手可对话式创建与执行工作流
- 自托管离线运行，占用 <50MB

## 适用场景

- 可视化搭建 LLM 提示工程与文本处理流水线
- 批量处理工单分类、联系人清洗、日志分析、合同条款提取
- 通过 MCP 让 AI 助手代为构建并执行工作流

## 场景标签

`工作流自动化` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L57: ## LLM Integration (MCP)
> L86: **LLM Integration** — Native support for major LLM providers and local models.

## 星数曲线

```mermaid
xychart-beta
    title "kleer001/Text_Loom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ca9f5918d2de` · [字段定义](../../DATASET.md)*
