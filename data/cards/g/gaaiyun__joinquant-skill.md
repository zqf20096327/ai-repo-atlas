# gaaiyun/joinquant-skill

⭐ 88 · Python · NOASSERTION · 推送 2026-10-12 · [GitHub](https://github.com/gaaiyun/joinquant-skill) · 个人维护 · 中文 README

**给 Coding Agent 用的聚宽量化策略 API 知识库与代码检查工具**

面向 Cursor、Claude Code、Codex 等 coding agent 的 JoinQuant 平台技能包：包含 14 类聚宽 API reference、5 个策略骨架模板、AST 静态 lint 脚本、API 搜索 CLI、9 个因子示例与本地因子研究模块，并可将搜索/生成/lint 暴露为 MCP 工具。定位是让 Agent 写策略前先查证 API、避免编造函数与混用运行环境；仓库不实现回测引擎，lint 通过不能证明无未来数据或策略有效，收益与实盘验证仍需在聚宽平台完成。CLI 无需第三方依赖，可选依赖含 jqdatasdk、MCP SDK 等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 类 API reference 按任务路由加载，附带 API 原始文档搜索
- strategy_lint.py 做 AST 静态检查已知错误与可疑 API
- 5 类策略骨架模板 CLI 生成（单股/多因子/ETF轮动/动量/均值回归）
- MCP server 暴露 jq_* 工具（搜索、lint、骨架生成、研报 prompt）

## 适用场景

- 让 Cursor/Claude Code 等 Agent 生成可在聚宽运行的策略代码
- 对已有聚宽策略做本地静态检查后再回平台回测
- 从自持研报 PDF 提取文本并生成策略候选代码（LLM 调用由用户完成）
- 本地配合 jqdatasdk 做因子 IC 与分组收益研究

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L19: 给 Coding Agent 使用的聚宽（JoinQuant）API 知识库、策略骨架与代码检查工具。
> L23: 本仓库把聚宽 API 资料、策略骨架、静态检查、因子示例、研报解析流程和 MCP 工具放在同一个 skill 中。Agent 可以按任务加载所需资料，人也可以直接使用其中的 CLI。
> L266: `cwd` 必须指向完整仓库。如果客户端找不到 `python`，先运行 `python -c "import sys; print(sys.executable)"`，再把输出的绝对路径填入 `command`。服务会暴露 A

## 星数曲线

```mermaid
xychart-beta
    title "gaaiyun/joinquant-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 86 --> 89
    line [87, 88, 88]
```

2026-10-18 87 → 2026-10-26 88（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `c98883e3f2ee` · [字段定义](../../DATASET.md)*
