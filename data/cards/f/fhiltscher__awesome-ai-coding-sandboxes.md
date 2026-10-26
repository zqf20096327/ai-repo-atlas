# fhiltscher/awesome-ai-coding-sandboxes

⭐ 27 · Python · CC0-1.0 · 推送 2026-09-10 · [GitHub](https://github.com/fhiltscher/awesome-ai-coding-sandboxes) · [官网](https://fhiltscher.github.io/awesome-ai-coding-sandboxes/) · 个人维护

**面向 AI 编程 agent 的沙箱/隔离方案安全态势清单**

策展型 awesome 清单：收录 38 个用于运行 AI 编程 agent（Claude Code、Codex、OpenHands 等）代码的沙箱方案，按安全态势排序——隔离层级（microVM/gVisor/容器/进程）、出站网络管控（deny-default/allowlist/configurable）与密钥处理（brokered/env-in），以对比矩阵呈现并附数据分析。每个单元格可溯源至项目自身文档，矩阵数据由 CI 从单一 JSON 源生成。另列 VM/容器/进程/文件系统与 WebAssembly 四类未入矩阵项目；声明仅读文档不做渗透测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 38 个沙箱方案的对比矩阵：隔离层级、出站管控、密钥处理、许可证
- 矩阵数据由 CI 从 sandboxes.json 单一数据源生成，防止漂移
- 单元格标注来源为项目自身文档，无文档处标 ? 不猜测
- 按 microVM、容器/gVisor、进程/命名空间、文件系统/Wasm 四类组织

## 适用场景

- 为 AI 编程 agent 选型运行其生成代码的沙箱
- 按出站网络与密钥暴露风险筛选隔离方案
- 了解沙箱生态中默认拒绝出站方案的分布情况

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: > A curated list of sandboxing and isolation solutions for running the code of autonomous **AI coding agents** (Clau
> L11: ## Comparison matrix
> L18: |Project|Isolation|Egress control|Secrets|Self-host / Managed|State|License|

## 星数曲线

```mermaid
xychart-beta
    title "fhiltscher/awesome-ai-coding-sandboxes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-26 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `09a49091026d` · [字段定义](../../DATASET.md)*
