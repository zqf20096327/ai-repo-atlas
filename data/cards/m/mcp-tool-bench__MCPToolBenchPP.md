# mcp-tool-bench/MCPToolBenchPP

⭐ 46 · Python · MIT · 推送 2026-03-17 · [GitHub](https://github.com/mcp-tool-bench/MCPToolBenchPP) · [官网](https://arxiv.org/abs/2508.07575) · 组织维护

**面向 AI Agent 的 MCP 工具使用能力评测基准**

大规模多领域 AI Agent 工具使用基准：截至 2025 年 7 月收录来自 MCP 与 GitHub 社区 45+ 类别的 4k+ MCP Server，数据集含浏览器、文件系统、搜索、地图、支付、金融六类共 1,509 实例的单步与多步工具调用任务。通过 pip 安装 mcp-marketplace 提供的 MCP 客户端管理 MCP Server，运行 run.py 以 AST 与 Pass@k（LLM-as-judge）指标评测模型，并附各模型性能榜单。README 声明基准仍在开发中，更多领域数据集将陆续发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 收录 4k+ MCP Server、45+ 类别，含 1,509 条单步/多步工具调用任务
- AST 与 Pass@k 双指标评测，LLM-as-judge 判分
- 提供 pip 安装的 mcpm CLI 与 MCP Marketplace 客户端管理服务器
- OneKey MCP Router 单一密钥接入多个商业 MCP

## 适用场景

- 评测 LLM/Agent 在浏览器、文件系统、搜索等场景的工具调用能力
- 对比不同模型的 MCP 工具使用表现
- 搭建可复现的 MCP 工具使用评测流水线

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: MCPToolBench++ is a large-scale, multi-domain AI Agent Tool Use Benchmark. As of July 2025, this benchmark includes 
> L77: python3 run.py --stage tool_call --input_file ./data/browser/browser_single_demo.json --category browser --model qw

## 星数曲线

```mermaid
xychart-beta
    title "mcp-tool-bench/MCPToolBenchPP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-29 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f382ee80137a` · [字段定义](../../DATASET.md)*
