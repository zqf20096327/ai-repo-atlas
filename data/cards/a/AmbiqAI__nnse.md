# AmbiqAI/nnse

⭐ 44 · C · BSD-3-Clause · 推送 2025-11-13 · [GitHub](https://github.com/AmbiqAI/nnse) · 组织维护

**面向 Ambiq 低功耗平台的神经网络语音降噪模型**

基于 RNN 的语音增强（降噪）模型，针对 Ambiq Apollo4 低功耗嵌入式平台优化，模型约 100kB，采样率 16 kHz。提供在 EVB 开发板上编译、部署预训练模型的 make 流程，通过 J-Link 与音频 USB 口连接，用 GUI 工具查看原始与增强后的音频；模型可基于公开语音与噪声数据集重新训练。核心库 ns-nnsp.a 用 C 实现特征提取（40 Mel 频谱）与神经网络推理，可通过 NeuralSPOT 修改重建。运行需 Arm GNU Toolchain 与 Segger J-Link。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RNN 语音降噪模型，约 100kB，16 kHz 采样率
- 提供 Apollo4 EVB 上的 make 编译/部署流程与音频查看 GUI
- ns-nnsp.a C 库封装特征提取与神经网络推理
- 支持基于公开数据集重新训练模型

## 适用场景

- 在 Ambiq Apollo4 开发板上运行低功耗语音降噪
- 采集并对比原始与增强后的麦克风音频
- 基于自己的数据集重新训练语音增强模型

## 场景标签

 · 领域:嵌入式AI/语音处理

## 证据(README 行号)

> L2: NN Speech Enhancement (NNSE) is a speech enhancement model (SE) based on recurrent neural networks (RNN).
> L16: This speech enhancement model is based on 16 kHz sampling rate. The model size is about 100kB.

## 星数曲线

```mermaid
xychart-beta
    title "AmbiqAI/nnse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-28 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9a0817fc3361` · [字段定义](../../DATASET.md)*
