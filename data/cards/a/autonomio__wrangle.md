# autonomio/wrangle

⭐ 16 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/autonomio/wrangle) · [官网](https://autonom.io) · 组织维护

**科研数据准备工具：YAML 协议+Polars 生成带证据的分析表**

以 YAML 协议声明科研数据准备决策（检查、清洗、匹配、重塑、验证），在原生 Polars 引擎上编译为表达式与 LazyFrame 计划执行，产出经检查的分析表与可复用证据（recipe.yaml、report.txt、含哈希的 receipt.json）。面向研究者、Notebook 与 AI agent 提供同一 CLI/Python 接口，支持 --json 输出与 AGENTS.md 入口。明确边界：不推断科学决策、不建模；本地执行、不访问网络、不接受任意回调；全局连接与分组计算仍可能需要较大内存。

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

- YAML 协议声明式数据准备，编译为 Polars 表达式与 LazyFrame 计划
- 保留 recipe/report/receipt 四类证据文件，含输入输出哈希
- Python、可读 CLI 与 agent 共用同一协议与检查
- 支持 CSV/TSV/Parquet/NDJSON/Excel 及 --execution disk 大文件流程

## 适用场景

- 把仪器测量与元数据文件准备成可审查的分析表
- 在批量研究数据上复用同一准备协议并保留证据
- 让 agent 通过 --json CLI 执行带检查的数据准备

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L139: The same protocol serves shell scripts and agents:
> L148: Agents use `wrangle start ... --json` for the same questions without prompts and
> L190: Installed agents start at `Path(wrangle.__file__).parent / "AGENTS.md"`;

## 星数曲线

```mermaid
xychart-beta
    title "autonomio/wrangle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `31078af0b786` · [字段定义](../../DATASET.md)*
