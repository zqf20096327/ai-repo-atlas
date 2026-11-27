# evo-design/proto-tools

⭐ 145 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/evo-design/proto-tools) · [官网](https://proto.evodesign.org/docs/tools/introduction) · 组织维护

**生成式生物学的计算工具套件：统一 Python 接口调用百余种生物 AI 工具**

Python 包，将结构预测、逆折叠、序列分析、基因注释、构象动力学、基因组打分等大量计算生物学与生物 AI 工具收纳到单一一致接口下，一次 pip install 即可使用。每个工具运行在自动管理的隔离环境中以处理依赖；内置设备管理与 GPU 扇出等基础设施支持连续调用与并行。可作为独立库使用，也可通过托管 MCP 服务器由 AI 助手调用，工具可在本地运行或部署到 Modal 云端。部分工具（如 ESM3、AlphaGenome）需先接受许可条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 Python 接口下整合 16 类工具：结构预测、逆折叠、序列比对、分子对接等
- 每个工具自动隔离环境，依赖由框架管理
- 内置设备管理、GPU 扇出与 ToolPool 并行执行
- 托管 MCP 服务器供 Claude/ChatGPT 等 AI 助手调用工具

## 适用场景

- 运行 AlphaFold、ESM 等模型预测蛋白质 3D 结构
- 从结构出发做逆折叠序列设计或 de novo 结合剂设计
- 在 Modal 云端批量运行多 GPU 推理任务
- 让 AI 助手通过 MCP 检索和调用生物信息学工具

## 场景标签

`科研工具` `推理引擎` · 领域:学习与行业

## 证据(README 行号)

> L25: Welcome! This repository contains the open-source implementation of `proto-tools`, a Python package containing a la
> L27: Every tool runs in its own automatically managed isolated environment, so all dependency wrangling is handled for y
> L215: Our hosted MCP server lets Claude, ChatGPT, and other AI assistants find and run these tools for you. To set up, f

## 星数曲线

```mermaid
xychart-beta
    title "evo-design/proto-tools 星数(近 12 点)"
    x-axis ["2026-10-25", "2026-10-27", "2026-10-30", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-19", "2026-11-23", "2026-11-26", "2026-11-27"]
    y-axis "stars" 135 --> 146
    line [136, 139, 141, 142, 136, 142, 143, 142, 143, 144, 145, 145]
```

2026-10-25 136 → 2026-11-27 145（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `dc0ef74acf62` · [字段定义](../../DATASET.md)*
