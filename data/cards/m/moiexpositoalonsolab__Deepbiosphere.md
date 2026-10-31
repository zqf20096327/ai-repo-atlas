# moiexpositoalonsolab/Deepbiosphere

⭐ 33 · Python · MIT · 推送 2025-12-01 · [GitHub](https://github.com/moiexpositoalonsolab/Deepbiosphere) · 组织维护

**深度学习绘制植物物种分布图的科研代码库**

开源实现公民科学（GBIF）观测与遥感（NAIP 影像）结合的深度卷积神经网络植物物种分布制图，对应 PNAS 论文。流程覆盖：下载 GBIF 观测数据、清洗并生成配对 NAIP 影像训练/测试数据集、训练深度网络、拟合基线并生成分布地图。安装经 pip，需 Python 3.7+、PyTorch 1.1+、CUDA 10.0+、GCC/C++（编译 inplace-abn）、R 3.4+，并手动配置源码中的路径对象；影像目录占用可达约 500 GiB 存储与大量内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GBIF 公民科学观测数据下载与过滤脚本（GADM 区域、年份参数化）
- 生成 NAIP 影像配对数据集与均匀/空间交叉验证划分
- 训练深度 CNN 模型并拟合基线、输出物种分布地图
- PNAS 论文的开源配套代码

## 适用场景

- 复现论文中的植物物种分布制图流程
- 用其他地区或时间段的 GBIF 数据训练物种分布模型
- 构建公民科学与遥感结合的生态学研究数据集

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # *Deepbiosphere*: Code for Deep learning models map rapid plant species changes from citizen science and remote sen
> L2: Open-source implementation for plant species distribution mapping using citizen science, remote sensing, and deep co

## 星数曲线

```mermaid
xychart-beta
    title "moiexpositoalonsolab/Deepbiosphere 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a82ad2c36a97` · [字段定义](../../DATASET.md)*
