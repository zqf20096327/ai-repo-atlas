# zjunlp/CaKE

⭐ 19 · Python · MIT · 推送 2025-11-17 · [GitHub](https://github.com/zjunlp/CaKE) · 组织维护

**面向多跳推理的知识编辑研究代码（EMNLP 2025 论文配套）**

EMNLP 2025 论文 Circuit-aware Editing Enables Generalizable Knowledge Learners 的官方代码库，目标是改进多跳推理设定下的知识编辑性能。提供基于 conda 环境与 requirements.txt 的安装流程；分析部分从 HoppingTooLate 下载 wikidata 数据，运行脚本过滤数据、生成实体与关系 patch、进行 back-patching 与 cross-patching 实验；编辑实验通过 run.sh 运行。代码构建于 EasyEdit 与 HoppingTooLate 项目之上。

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

- 面向多跳推理场景的知识编辑方法
- 提供 patch_activations 的 back-patching/cross-patching 分析脚本
- 基于 EasyEdit 与 HoppingTooLate 构建

## 适用场景

- 复现论文中的多跳知识编辑实验
- 分析知识回路与实体/关系 patch 的效果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L6: This work aims to improve the knowledge editing performance under the multi-hop reasoning settings.
> L31: We thank for the project of EasyEdit, HoppingTooLate.

## 星数曲线

```mermaid
xychart-beta
    title "zjunlp/CaKE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `dbe2b98df2c9` · [字段定义](../../DATASET.md)*
