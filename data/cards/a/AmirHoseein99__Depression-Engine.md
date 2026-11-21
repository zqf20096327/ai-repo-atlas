# AmirHoseein99/Depression-Engine

⭐ 20 · Python · 推送 2026-11-08 · [GitHub](https://github.com/AmirHoseein99/Depression-Engine) · 个人维护

**基于语音活动与频谱图的抑郁症检测 Python 包（DAIC-WOZ）**

将研究 notebook 重构为可安装的 Python 包与命令行工具，在 DAIC-WOZ 语料上运行四阶段流水线：扫描原始音频/转写/COVAREP 生成 manifest，训练 CNN+GRU 语音活动检测模型，统计静音特征并做 Welch t 检验与置换检验，再用 2 秒 mel 频谱窗训练 2-D 卷积模型做参与者级抑郁检测。数据集不随仓库分发，需自行申请；训练依赖 TensorFlow；历史结果因缺陷修复不保证复现，无自动化测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CNN+GRU 语音活动检测（26 MFCC+delta，帧级输出）
- 静音统计分析（Welch t 检验、置换检验、逻辑回归分类）
- 2 秒 mel 频谱窗 + Conv2D 抑郁检测，支持种子化集成
- 重构修复了标签对齐、无效层与训练/测试泄漏等缺陷

## 适用场景

- 在 DAIC-WOZ 数据上复现语音与静音的抑郁检测研究
- 分析抑郁组与对照组的静音特征差异
- 作为可安装包与 CLI 运行端到端训练与评估

## 场景标签

 · 领域:医疗健康/语音计算精神病学

## 证据(README 行号)

> L3: Speech-activity and spectrogram based depression detection on the DAIC-WOZ
> L16: 4. **Depression detection** – train a 2-D convolutional model on 2-second mel
> L17:  spectrogram windows and aggregate window scores per participant.

## 星数曲线

```mermaid
xychart-beta
    title "AmirHoseein99/Depression-Engine 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-21"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-11-08 20 → 2026-11-21 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `61427f12a55b` · [字段定义](../../DATASET.md)*
