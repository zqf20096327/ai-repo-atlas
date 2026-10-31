# ThorstenDoherr/searchengine

⭐ 14 · xBase · MIT · 推送 2026-09-25 · [GitHub](https://github.com/ThorstenDoherr/searchengine) · 个人维护

**Windows 下的数据库模糊匹配工具：按地址等模糊准则匹配大型数据**

以 Visual FoxPro（部分 C 实现）编写的启发式匹配引擎，用于对大型数据库按公司名、街道、城市等模糊准则做实体匹配。核心机制是基于词频的注册表字典（低频词权重高）、字段权重与阈值组合的搜索策略，并支持多次搜索运行（基础搜索加针对缺漏、拼写错误等的专门运行）。附带 SEML 目录（STATA/Python 脚本）在匹配后用机器学习方法精炼结果。文档含手册、背景论文与演示幻灯片，安装说明见 doc/searchengine.md。仅限 Windows 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于词频注册表的启发式匹配，支持字段权重、阈值及权重分布选项（log/softmax/offset）
- 多轮搜索策略：基础搜索加针对数据特例的专门运行
- SEML 目录提供 STATA（seml.do）与 Python（seml.py）脚本做匹配后的机器学习精炼
- 基于 ParallelFox 的多进程并行加速，Visual FoxPro Advanced 取消 2GB 表大小限制

## 适用场景

- 对含地址、公司名的大型数据库做实体解析与重复项匹配
- 处理有拼写错误、缺漏地址字段、名称噪声的数据匹配
- 匹配后用 SEML 脚本进一步精炼结果

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L2: **SearchEngine** is a tool written in Foxpro and to a small but decisive part in C. It implements heuristic matching
> L182: - SEML directory contains sample code showing how to implement a ML algorithm based on https://github.com/Thorsten

## 星数曲线

```mermaid
xychart-beta
    title "ThorstenDoherr/searchengine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ef700c7988aa` · [字段定义](../../DATASET.md)*
