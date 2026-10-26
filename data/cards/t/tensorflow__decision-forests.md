# tensorflow/decision-forests

⭐ 692 · Python · Apache-2.0 · 推送 2026-05-19 · [GitHub](https://github.com/tensorflow/decision-forests) · 组织维护

**在 TensorFlow/Keras 中训练、运行与解释决策森林模型的库**

TensorFlow Decision Forests（TF-DF）提供在 TensorFlow/Keras 中训练、服务和解释决策森林模型（随机森林、梯度提升树等）的能力，支持分类、回归与排序任务。底层由 C++ 实现的 Yggdrasil Decision Forests（YDF）驱动，两者模型格式互相兼容。通过 pip 安装，支持 Linux 与 Mac，Windows 需经 WSL+Linux 使用。README 顶部声明建议用户迁移至 YDF，YDF 训练相同模型且功能更多。由 Google 开发者团队开发，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练/运行/解释决策森林模型（Random Forest、GBT 等）
- 支持分类、回归与排序任务
- 基于 Yggdrasil Decision Forests，模型与 YDF 互兼容
- 以 Keras 接口提供，pip 安装，支持 Linux/Mac

## 适用场景

- 在 TensorFlow/Keras 流水线中训练决策森林模型
- 对表格数据做分类、回归或排序
- 需要可解释的树模型并集成到 TF 服务链路

## 场景标签

 · 领域:机器学习/决策森林

## 证据(README 行号)

> L7: **TensorFlow Decision Forests** (**TF-DF**) is a library to train, run and
> L9: models (e.g., Random Forests, Gradient Boosted Trees) in TensorFlow. TF-DF

## 星数曲线

```mermaid
xychart-beta
    title "tensorflow/decision-forests 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 691 --> 693
    line [692, 692]
```

2026-10-18 692 → 2026-10-26 692（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `83280100efd4` · [字段定义](../../DATASET.md)*
