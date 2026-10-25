# kaistmm/seed-pytorch

⭐ 62 · Python · 推送 2025-11-03 · [GitHub](https://github.com/kaistmm/seed-pytorch) · 组织维护

**面向科研的说话人嵌入扩散增强框架，提升恶劣声学下的鲁棒性**

KAIST 团队发表的 Interspeech 2025 论文官方实现：用扩散模型对预训练说话人识别模型（ResNetSE34V2、ECAPA-TDNN、WavLM-ECAPA 等）提取的说话人嵌入进行去噪精炼，训练时对干净/带噪嵌入前向加噪再重建，推理时经扩散过程重新生成嵌入，无需说话人标签且不改动现有识别流水线。提供训练/评估命令、预训练权重、嵌入提取与权重前缀修复工具。要求 Linux、CUDA 12.5、ffmpeg，输入建议 16kHz 单声道 PCM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扩散模型将带噪说话人嵌入重建为鲁棒嵌入，训练无需说话人标签
- 支持 ResNetSE34V2 / ECAPA-TDNN / WavLM-ECAPA 等多种骨干，可扩展到语音识别、表情识别、人脸识别等表示模型
- 提供官方预训练权重与从自有音频提取嵌入的命令
- 附带 model_params_tool.py 修复 state_dict 前缀冲突以接入自有骨干权重

## 适用场景

- 在实际环境噪声下提升说话人验证系统的鲁棒性
- 复现论文训练与评估流程（VC-Mix / VoxSRC23 鲁棒性基准）
- 将自己训练的表示模型骨干接入 SEED 框架做嵌入增强

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: **SEED** is a first diffusion-based embedding enhancement framework designed to improve speaker representation robus
> L14: *A primary challenge when deploying speaker recognition systems in real-world applications is performance degradati

## 星数曲线

```mermaid
xychart-beta
    title "kaistmm/seed-pytorch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 60 --> 63
    line [61, 62, 62]
```

2026-10-18 61 → 2026-10-25 62（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4a1fe1622457` · [字段定义](../../DATASET.md)*
