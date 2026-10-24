# scitex-ai/scitex-python

⭐ 86 · Python · AGPL-3.0 · 推送 2026-10-16 · [GitHub](https://github.com/scitex-ai/scitex-python) · [官网](https://scitex.ai) · 组织维护

**面向科研的统一 Python 工具库，含 MCP 工具供 AI agent 开展研究**

SciTeX 生态的编排层 Python 库：在统一命名空间下提供 73 个模块，覆盖实验跟踪、文件 I/O（50+ 格式）、统计检验（23+）、可复现图表、文献检索（本地 CrossRef/OpenAlex）、LaTeX 手稿编译、通知与容器等，可通过 Python API、CLI 和 MCP 三种接口访问，其中 MCP 暴露 323 个工具供 AI agent 调用。Clew 模块构建 SHA-256 哈希链 DAG，将手稿声明链接到源数据做加密验证。全部包以 AGPL-3.0 提供、可自托管，安装推荐 uv（完整 extras 用 pip 需 30–90 分钟），要求 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 73 个模块统一命名空间，Python API / CLI / MCP（323 工具）三接口
- Clew 用 SHA-256 哈希链 DAG 验证手稿声明到源数据的完整性
- scitex.io 支持 50+ 文件格式的读写与格式自动识别
- @scitex.session 装饰器提供自动 CLI、配置冻结与实验输出结构化

## 适用场景

- 科研流程从文献检索、统计分析到手稿编译在一个工具包内完成
- 让 AI agent 通过 MCP 工具执行统计、绘图、文献检索等研究任务
- 对研究产物做哈希链级验证以满足可审计性要求

## 场景标签

 · 领域:科研工具/可复现科学

## 证据(README 行号)

> L28: |3|**AI agents lack context** -- general-purpose LLMs cannot operate across the full research lifecycle without dom
> L123: |**MCP**|`scitex mcp start`|323 tools an AI agent calls directly|
> L125: The Python API is the primary surface; the CLI and MCP server expose the same logic for shells and AI agents. See 

## 星数曲线

```mermaid
xychart-beta
    title "scitex-ai/scitex-python 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 84 --> 87
    line [85, 86, 86]
```

2026-10-18 85 → 2026-10-24 86（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `090ce8b0377f` · [字段定义](../../DATASET.md)*
