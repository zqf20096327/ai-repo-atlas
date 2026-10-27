# maja601/EuroCrops

⭐ 226 · Jupyter Notebook · CC-BY-SA-4.0 · 推送 2026-03-11 · [GitHub](https://github.com/maja601/EuroCrops) · 组织维护

**欧盟各国自报农作物数据集集合，含 HCAT 分类体系**

EuroCrops 是汇总欧盟各成员国公开的自报农作物申报数据的矢量数据集集合，覆盖奥地利、德国、法国等 16 个参与国。项目由德国宇航中心（DLR）代表联邦经济事务与气候行动部资助。核心机制是提出 HCAT（分层农作物与农业分类体系），将各国原始作物命名统一为机器可读分类（EC_hcat_n 属性与 10 位 HCAT 编码），并为每个地块附加手工标注的近似 NUTS3 区域属性，用于训练/验证/测试集的空间划分。矢量数据经 Zenodo 分发，仓库内含各国 CSV 映射文件与 HCAT.csv；许可为 CC BY-SA 4.0。README 提示关注 EuroCrops 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-SA-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合欧盟 16 国公开自报农作物申报矢量数据
- HCAT 分层分类体系统一各国作物命名（10 位编码）
- 附带 NUTS3 区域属性用于数据集空间划分
- 矢量数据经 Zenodo 分发，当前版本为 Version 11

## 适用场景

- 训练农作物类型分类或监测模型的数据来源
- 跨国家比较欧盟农业申报数据的统一分类研究
- 遥感（如 Sentinel-2）与地块矢量数据结合的分析

## 场景标签

 · 领域:农业遥感/开放数据集

## 证据(README 行号)

> L9: EuroCrops is a dataset collection combining all publicly available self-declared crop reporting datasets from countr

## 星数曲线

```mermaid
xychart-beta
    title "maja601/EuroCrops 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 225 --> 227
    line [226, 226]
```

2026-10-18 226 → 2026-10-27 226（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4af5efb3a1d6` · [字段定义](../../DATASET.md)*
