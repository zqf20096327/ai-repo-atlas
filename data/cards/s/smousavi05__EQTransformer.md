# smousavi05/EQTransformer

⭐ 419 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/smousavi05/EQTransformer) · [官网](https://rebrand.ly/EQT-documentations) · 个人维护

**地震信号检测与震相拾取的深度学习 Python 包**

基于注意力机制深度神经网络的地震信号检测器与 P/S 震相拾取器，层级架构针对地震信号设计，在全球地震数据上训练，可同时执行检测与到时拾取，并输出预测概率与模型不确定性估计。Python 3 包还包含连续波形下载、预处理、用预训练模型预测、构建测试新模型和简单震相关联模块。提供原版（优化假阴性率）与保守版（优化假阳性率）两种预训练模型及不同阈值建议。

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

- 同时执行地震检测与 P/S 震相到时拾取，输出概率与不确定性估计
- 全球数据训练的层级注意力网络，提供原版/保守版两种预训练模型
- 含波形下载、预处理、模型训练测试与简单震相关联模块
- 提供 conda / PyPI / 源码多种安装方式，支持 macOS/Windows/Linux

## 适用场景

- 我用它对连续地震波形做自动事件检测和震相拾取
- 我在区域地震目录构建流程中使用预训练模型
- 我基于它训练或微调适合本地数据的拾取模型

## 场景标签

 · 领域:地球物理/地震学

## 证据(README 行号)

> L18: **EQTransformer** is an AI-based earthquake signal detector and phase (P&S) picker based on a deep neural network w
> L20: The **EQTransformer** python 3 package includes modules for downloading continuous seismic data, preprocessing, per

## 星数曲线

```mermaid
xychart-beta
    title "smousavi05/EQTransformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 418 --> 420
    line [419, 419]
```

2026-10-18 419 → 2026-10-22 419（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `39cf8220600f` · [字段定义](../../DATASET.md)*
