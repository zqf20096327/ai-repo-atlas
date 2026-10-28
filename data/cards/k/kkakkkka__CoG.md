# kkakkkka/CoG

⭐ 35 · Python · NOASSERTION · 推送 2026-10-10 · [GitHub](https://github.com/kkakkkka/CoG) · 个人维护

**从语音生成面部、身体与手部动作的多模态动作合成模型**

AAAI-2024 论文 Chain of Generation 的改进版代码：以级联条件控制方式，从语音（及文本对齐、情绪、说话人信息）生成面部、身体和手部动作。基于 BEAT 英语数据集训练，需下载 BEAT 数据并构建缓存；权重通过 Hugging Face Hub 获取。支持训练、推理评测，以及用自己的录音做推理（经 Montreal Forced Aligner 生成 TextGrid 对齐）。输出为 pose/face 的 npy 文件与 json 报告。许可证为 CC BY-NC 4.0。

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

- 从语音生成 face/body/hand 动作
- 级联条件控制架构，含情绪与说话人编码器
- 支持自定义录音推理（Montreal Forced Aligner 对齐）
- 提供训练与评测脚本，输出 report.json

## 适用场景

- 研究者复现或改进语音驱动动作生成方法
- 用自己录制的语音生成对应肢体与面部动作
- 在 BEAT 数据集上训练动作生成模型

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: > *This repo includes an improved version of Chain of Generation: Multi-Modal Gesture Synthesis via Cascaded Conditi
> L65: CoG reads the words tier of a TextGrid. Use Montreal Forced Aligner to make one from a recording. Put each wav and 

## 星数曲线

```mermaid
xychart-beta
    title "kkakkkka/CoG 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-28 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ae08bb24b7d4` · [字段定义](../../DATASET.md)*
