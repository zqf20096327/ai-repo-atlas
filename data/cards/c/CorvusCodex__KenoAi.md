# CorvusCodex/KenoAi

⭐ 22 · Python · MIT · 推送 2025-11-24 · [GitHub](https://github.com/CorvusCodex/KenoAi) · 个人维护

**用机器学习预测下一期 Keno 开奖号码的 Python 脚本**

KenoAi 是一个基于 TensorFlow/Keras 的 Keno 彩票号码预测脚本：读取 data.txt 中的历史开奖记录（逗号分隔、降序排列、无空格），训练模型后向控制台输出预测的下一期 20 个号码。依赖 numpy、tensorflow、keras、art，通过 pip 安装。README 声明针对 CUDA、Threadripper 与多 GPU 优化，并链接了付费的 Windows 编译版应用。免责声明明确 Keno 结果本质随机，预测不保证准确，代码仅供教育与研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 data.txt 历史开奖数据并训练模型
- 输出预测的下一期 20 个号码
- 基于 TensorFlow/Keras，依赖通过 pip 安装

## 适用场景

- 我有 Keno 历史开奖数据，想跑一个 ML 脚本生成下期号码预测
- 学习/研究彩票号码预测的机器学习实现

## 场景标签

 · 领域:彩票预测/机器学习

## 证据(README 行号)

> L2: KenoAi is a keno prediction artificial intelligence that uses machine learning to predict numbers of next draw in ki
> L38: Once you have the data file, you can run the `KenoAi` script to train the model and generate predictions. The scrip

## 星数曲线

```mermaid
xychart-beta
    title "CorvusCodex/KenoAi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `1cfbf49297fe` · [字段定义](../../DATASET.md)*
