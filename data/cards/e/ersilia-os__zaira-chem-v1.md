# ersilia-os/zaira-chem-v1

⭐ 47 · Python · GPL-3.0 · 推送 2026-07-07 · [GitHub](https://github.com/ersilia-os/zaira-chem-v1) · 组织维护

**化学结构的自动机器学习 (Q)SAR 建模库（已归档版本）**

Ersilia 系列工具中面向生物医学问题的自动化机器学习库，本仓库为已归档的 v1 版本（新版另见 zaira-chem 仓库）。针对 (Q)SAR 建模：读取含 SMILES 与活性值两列的表格文件，通过命令行执行 example/split/fit/predict/distill 流水线，自动训练模型并输出分子属性预测概率与性能图表；支持内置 Olinda 管线将模型蒸馏为 ONNX 紧凑版本。以 git clone 加 Linux 安装脚本方式安装，默认创建 Conda 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- fit/predict/distill 命令行流水线自动完成 (Q)SAR 训练与预测
- 读取 SMILES+活性值表格，自动确定分类阈值并输出类别概率
- 内置 Olinda 管线将模型蒸馏为 ONNX 格式并继续用于预测
- 预测同时生成多项性能图表

## 适用场景

- 给定化合物结构与活性数据，训练模型预测药理属性
- 对测试集分子批量预测生物活性概率
- 将训练好的 (Q)SAR 模型压缩为 ONNX 部署

## 场景标签

 · 领域:药物发现/化学信息学

## 证据(README 行号)

> L9: ZairaChem is the first library of Ersilia's family of tools devoted to providing **out-of-the-box** machine learning
> L66: This command will run the full ZairaChem pipeline and produce a model folder with processed data, model checkpoints

## 星数曲线

```mermaid
xychart-beta
    title "ersilia-os/zaira-chem-v1 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-27 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `322b38c912db` · [字段定义](../../DATASET.md)*
