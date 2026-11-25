# ozgurcd/gograph

⭐ 232 · Go · MIT · 推送 2026-11-23 · [GitHub](https://github.com/ozgurcd/gograph) · [官网](https://gograph.identuum.ai) · 个人维护

**为 Go 编码 agent 提供本地确定性代码结构分析的 MCP 引擎**

在本地为 Go 仓库构建结构图（调用图、接口实现、影响分析、符号查询），可选 type-checked CHA/SSA 精确增强；通过 CLI 与内置 MCP server 两种方式供编码 agent 使用，无需嵌入向量或托管代码索引。默认索引仅解析源码不执行目标代码；精确模式会调用本机 Go 工具链（可能按 GOPROXY 策略联网），cgo 包还会调用 C 编译器。支持 Homebrew 与 go install 安装，遥测数据仅存本地 .gograph/ 目录。

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

- CLI 与 MCP server 双入口，MCP 无需预构建即可在内存建图
- 确定性结构查询：调用者/被调用者、影响分析、符号定位
- 可选 --precise 类型检查增强（CHA/SSA），离线时回退 AST 图
- 机器可读验证谓词（symbol_exists、call_edge_exists 等）与 JSON 输出

## 适用场景

- 让 Claude Code 等编码 agent 在重构前查询调用关系与影响面
- 在 CI 中以 --strict 模式校验精确索引未回退
- 用 validate 谓词检查架构约束（如 imports_only_from）
- 本地离线环境下做 Go 代码导航与热点分析

## 场景标签

 · 领域:开发者工具/代码分析

## 证据(README 行号)

> L49: `gograph` builds a local structural graph of your Go repository, with optional
> L50: type-checked CHA/SSA enrichment. Its CLI and MCP workflows help coding agents
> L85:  with `run 'gograph build' first`. The MCP server needs no build step:

## 星数曲线

```mermaid
xychart-beta
    title "ozgurcd/gograph 星数(近 6 点)"
    x-axis ["2026-10-23", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-23", "2026-11-25"]
    y-axis "stars" 229 --> 233
    line [230, 231, 230, 231, 232, 232]
```

2026-10-23 230 → 2026-11-25 232（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `2f662deebdb9` · [字段定义](../../DATASET.md)*
