# H-Ali13381/wakeword-forge

⭐ 24 · Python · Apache-2.0 · 推送 2026-06-11 · [GitHub](https://github.com/H-Ali13381/wakeword-forge) · 个人维护

**本地训练自定义唤醒词并导出 ONNX 检测模型的工具**

面向需要自建唤醒词检测器的开发者：用户录制或导入音频样本，经审核门控流程后训练 WavLM-base 教师模型，蒸馏为约 40K 参数的 RepCNN 学生模型，导出 217 KB 的 wakeword.onnx 及含阈值/EER 的配置 JSON，可用 onnxruntime 加载或 make mic-test 实时验证。数据默认本地存储，不默认上传；训练流水线含指纹化审核门控，样本变更会使先前批准失效。限制：单说话人训练对其他说话人泛化较弱，跨说话人基准数据未发布。以 Python + Make 目标与 Streamlit 仪表盘形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WavLM 教师蒸馏为 ~40K 参数 RepCNN，导出 217 KB ONNX 文件
- 端到端流水线：采样→审核门控→训练→导出→实时验证→验收
- 硬负样本（背景/静音/部分短语/近似词）作为一等训练输入
- 最低 10 正样本、5 负样本即可开始训练

## 适用场景

- 为语音助手训练自定义唤醒词而非固定词表
- 在本地完成音频采集与训练，避免语音数据上传
- 导出小型 ONNX 模型集成到应用或常驻语音守护进程

## 场景标签

 · 领域:语音/音频机器学习

## 证据(README 行号)

> L12: `wakeword-forge` trains a custom wake-word detector for a phrase you choose (`Hey Nova`, `Okay Atlas`, anything). Y
> L55: 6. Export `output/wakeword.onnx`.

## 星数曲线

```mermaid
xychart-beta
    title "H-Ali13381/wakeword-forge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-27 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `eec48611b437` · [字段定义](../../DATASET.md)*
