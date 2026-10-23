# nicolas-hbt/pygraft

⭐ 717 · Python · MIT · 推送 2026-01-26 · [GitHub](https://github.com/nicolas-hbt/pygraft) · [官网](https://pygraft.readthedocs.io/en/latest/) · 个人维护

**为科研人员按参数生成合成模式与知识图谱的 Python 库**

开源 Python 库，也是 arXiv 2309.03685 论文的官方实现：按用户在 YAML 配置中指定的参数，在单一流水线中生成合成 schema 与知识图谱（可分别生成或一次生成），生成的资源与具体应用领域无关。schema 与 KG 使用扩展的 RDFS/OWL 构造描述，并通过 owlready2 中的 HermiT DL 推理机校验逻辑一致性（需安装 Java 并设置 JAVA_HOME）。提供 Python API 与 CLI 两种用法，输出 RDF 文件及类/关系信息 JSON。当前仅支持以自生成 schema 为输入，尚不支持任意外部 schema。

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

- 单一流水线内生成 schema 与 KG
- 基于大量用户参数的可调生成过程，使用 RDFS/OWL 构造
- 通过 HermiT DL 推理机保证 schema 与 KG 的逻辑一致性
- 提供 Python API 与 CLI 两种调用方式

## 适用场景

- 在数据敏感或难以获取的领域生成合成知识图谱用于研究
- 为知识图谱相关算法生成不同特性的基准测试数据
- 按指定参数快速构造符合语义网标准的 schema 与 KG

## 场景标签

`知识图谱` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L23: PyGraft is an open-source Python library for generating synthetic yet realistic schemas and (KGs) based on user-spe
> L25: Being able to synthesize schemas and KGs is an important milestone for conducting research in domains where data is
> L75: From a high-level perspective, the entire PyGraft generation pipeline is depicted in Figure 1. In particular, Class

## 星数曲线

```mermaid
xychart-beta
    title "nicolas-hbt/pygraft 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 715 --> 718
    line [716, 717, 717]
```

2026-10-18 716 → 2026-10-23 717（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `18e9045c5828` · [字段定义](../../DATASET.md)*
