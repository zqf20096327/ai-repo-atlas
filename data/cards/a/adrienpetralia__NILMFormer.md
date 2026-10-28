# adrienpetralia/NILMFormer

⭐ 55 · Python · NOASSERTION · 推送 2026-05-26 · [GitHub](https://github.com/adrienpetralia/NILMFormer) · 组织维护

**给科研者的 NILM Transformer 模型代码库：分解住户总用电为各电器功耗**

ACM SIGKDD 2025 论文 NILMFormer 的官方 PyTorch 代码库，提供序列到序列 Transformer 架构，将住户总用电量分解为各电器的独立功耗（非侵入式负荷监测 NILM）。模型通过分离编码形状、时序动态与内在统计量处理智能电表数据的非平稳性，并用 TimeRPE 时间戳位置编码与统计量回投影处理功率损耗。仓库附带论文实验复现代码与 10 个 PyTorch 实现的 SotA 基线。作者来自巴黎西岱大学与 EDF 研究部门。依赖通过 uv 管理安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 序列到序列 Transformer 架构，针对 NILM 分解任务
- 通过平稳化输入与 TokenStats 处理非平稳性
- TimeRPE 基于时间戳（分钟/小时/日/月）的位置编码
- 附带 10 个 PyTorch 实现的 SotA NILM 基线

## 适用场景

- 复现 KDD 2025 论文的 NILM 实验
- 研究非平稳时序数据的负荷分解方法
- 对比其他 NILM 基线模型的表现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L6: Official PyTorch codebase for **NILMFormer: Non-Intrusive Load Monitoring that Accounts for Non-Stationarity** (ACM 
> L16: We introduce **NILMFormer**, a sequence-to-sequence Transformer-based architecture designed to tackle this problem.
> L62: **TL;DR** : **NILMFormer** is a **sequence-to-sequence Transformer-based architecture** purpose-built for **Non-Int

## 星数曲线

```mermaid
xychart-beta
    title "adrienpetralia/NILMFormer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `1335857e04b9` · [字段定义](../../DATASET.md)*
