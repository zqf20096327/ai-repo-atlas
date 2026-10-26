# richardwhiteii/rlm

⭐ 50 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/richardwhiteii/rlm) · 个人维护

**Claude Code 的 MCP 服务器：把超大上下文作为外部变量处理**

基于递归语言模型（RLM）论文实现的 MCP 服务器，供 Claude Code 使用。核心机制：将大文件加载为外部变量（不进入 prompt），程序化检视结构，按行/字符/段落分块，对分块递归发起子 LLM 查询（支持 max_depth 1-5 递归分解），再聚合结果；另提供 rlm_exec 在沙箱子进程中执行 Python 代码做确定性提取。子查询默认走 Claude Agent SDK（claude-haiku-4-5），可切换 Ollama 本地推理（如 gemma3:27b）。通过 git clone + uv/pip 安装，以 claude mcp add 注册。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 大上下文作为外部变量：加载/检视/分块/子查询/聚合五步流水线
- rlm_sub_query 支持深度 1-5 的递归分层分解
- rlm_exec 沙箱执行 Python 代码做确定性提取，无需 Docker
- 子查询提供 claude-sdk 与 Ollama 两种 provider

## 适用场景

- 让 Claude 分析超大日志或代码库而不撑爆上下文窗口
- 对大型文档做分块摘要、找 bug、安全审计等批量子查询
- 用本地 Ollama 模型零成本处理递归子查询

## 场景标签

 · 领域:LLM 基础设施/上下文管理

## 证据(README 行号)

> L3: Recursive Language Model patterns for Claude Code — handle massive contexts (10M+ tokens) by treating them as extern
> L9: You don't call RLM tools directly. You ask Claude to analyze large files, and Claude uses RLM behind the scenes.
> L104: |`rlm_auto_analyze`|**One-step analysis** — auto-detects type, chunks, and queries|

## 星数曲线

```mermaid
xychart-beta
    title "richardwhiteii/rlm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-26 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9800218341fb` · [字段定义](../../DATASET.md)*
