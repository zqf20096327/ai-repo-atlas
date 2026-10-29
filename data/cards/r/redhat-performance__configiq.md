# redhat-performance/configiq

⭐ 21 · TypeScript · 推送 2026-10-28 · [GitHub](https://github.com/redhat-performance/configiq) · [官网](https://configiq.xyz) · 组织维护

**面向工程师的 LLM 推理容量规划与 GPU 成本建模工具**

Red Hat 性能团队维护的 Next.js Web 应用：提供 GPU 显存与成本估算、批量/量化下的详细选型建议、KV Cache 计算器、GPU 参数对比、云/本地/混合成本节省分析、多模型层级路由经济性与多节点集群成本估算。基于经验训练的性能包络分类器（Triton FIL 服务）为已测模型-硬件组合提供验证数据，后端依赖 AISimulators 与 aicostings REST API。需 Node.js>=20.19.0 与 npm>=10 从源码运行，另有 configiq.xyz 在线版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GPU 显存与成本快速估算及批量/量化详细选型建议
- KV Cache 内存分解与容量分析
- GPU 跨内存/吞吐/成本/可用性对比
- 经验训练的性能包络分类器（Triton FIL 服务）提供已测模型-硬件验证

## 适用场景

- 为 LLM 推理服务选型 GPU 并估算成本
- 分析 KV Cache 显存占用与并发容量
- 比较云/本地/混合部署的成本节省与多节点集群成本

## 场景标签

 · 领域:LLM 推理基础设施/性能工程

## 证据(README 行号)

> L3: LLM inference sizing, GPU comparison, and cost modeling for engineers and infrastructure teams.
> L26: ConfigIQ maintains empirically trained performance-envelope classifiers for
> L27: supported model and hardware pairs. The classifiers are built from sanitized,

## 星数曲线

```mermaid
xychart-beta
    title "redhat-performance/configiq 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8cd098e17c89` · [字段定义](../../DATASET.md)*
