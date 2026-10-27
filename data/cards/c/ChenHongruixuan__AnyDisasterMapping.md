# ChenHongruixuan/AnyDisasterMapping

⭐ 75 · Python · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/ChenHongruixuan/AnyDisasterMapping) · [官网](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6725082) · 组织维护

**遥感灾害制图统一基准与深度学习训练评测框架**

论文配套官方代码库，统一了遥感灾害制图领域常用基准与代表性深度学习模型，覆盖建筑损毁评估、洪水制图、滑坡分割、野火分析四类任务。提供一致的训练与评测流水线：YAML 配置驱动训练（train.py）、按实验目录评测（test.py），按灾种组织数据准备脚本与模型库（SegFormer、SAM/SAM2、DINOv3、ChangeMamba 等），预训练权重需另行下载到本地 pretrained_weight/ 目录，部分模型的 CUDA 索引与可选内核编译有专门说明。供研究者复现论文结果、在统一协议下评测模型并在此基础上扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一四类灾害任务（损毁/洪水/滑坡/野火）的基准与模型实现
- YAML 配置驱动的训练与评测流水线（train.py / test.py）
- 聚合 SegFormer、SAM/SAM2、DINOv3、ChangeMamba 等模型库及权重下载指引
- 按灾种组织的数据准备脚本与架构/扩展文档

## 适用场景

- 复现灾害制图综述论文中报告的结果
- 在统一协议下对比不同灾害制图模型的性能
- 以现成基线为起点开发自己的灾害制图方法

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L25: One of our key motivations is that current disaster mapping research is highly fragmented: benchmarks, tasks, and m
> L27: This repo unifies widely used disaster mapping benchmarks and representative deep learning models across major rese
> L33: It is designed to help researchers:

## 星数曲线

```mermaid
xychart-beta
    title "ChenHongruixuan/AnyDisasterMapping 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 73 --> 76
    line [74, 75, 75]
```

2026-10-18 74 → 2026-10-27 75（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `636d110e42f1` · [字段定义](../../DATASET.md)*
