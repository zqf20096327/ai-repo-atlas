# matthewmcq/upscalemp3_v2

⭐ 26 · Jupyter Notebook · MIT · 推送 2026-09-08 · [GitHub](https://github.com/matthewmcq/upscalemp3_v2) · [官网](https://huggingface.co/spaces/matthewmcq/upscalemp3_v2/tree/main) · 个人维护

**去除 MP3 压缩伪影的深度学习音频修复模型**

基于小波 U-Net（Daubechies db4、5 层分解、门控跳跃连接、残差学习、12.6M 参数）的音频修复模型：输入 MP3 压缩音频，输出去伪影的 44.1kHz/16-bit 高保真音频。训练用 MedleyDB 2.0 与 MUSDB18-HQ，通过随机比特率（64-256 kbps）MP3 退化仿真学习映射。提供预训练权重（Hugging Face 下载）、推理脚本与训练/微调流程；长音频用 Hann 窗 overlap-add 分段处理。限制：未优化实时处理、低于 64 kbps 恢复有限、主要面向音乐非语音。

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

- Wavelet U-Net（db4 小波 + 门控跳跃连接 + 残差学习，12.6M 参数）
- 训练管线模拟 64-256 kbps 多档 MP3 退化
- 长音频 Hann 窗 overlap-add 分段处理，支持可配置重叠率
- 提供预训练权重与训练/微调完整流程

## 适用场景

- 修复低比特率 MP3 音乐的压缩伪影
- 将 MP3 收藏恢复为 CD 音质 WAV
- 基于自有数据重新训练以覆盖其他比特率或音频类型

## 场景标签

 · 领域:音频处理/深度学习

## 证据(README 行号)

> L3: A deep learning model for removing MP3 compression artifacts and restoring audio quality using a Wavelet U-Net archi
> L9: upscalemp3_v2 uses a Wavelet U-Net architecture to learn the mapping between MP3-compressed audio and original high-

## 星数曲线

```mermaid
xychart-beta
    title "matthewmcq/upscalemp3_v2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a2e194d2e803` · [字段定义](../../DATASET.md)*
