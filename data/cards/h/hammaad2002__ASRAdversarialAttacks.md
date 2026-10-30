# hammaad2002/ASRAdversarialAttacks

⭐ 44 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/hammaad2002/ASRAdversarialAttacks) · 个人维护

**对 ASR 语音识别模型做白盒对抗攻击测试的 Python 库**

面向安全研究者的工具库：对语音转文本模型运行 FGSM、BIM、PGD、CW、Imperceptible 等白盒对抗攻击（均支持定向/非定向模式），生成对抗性音频并测量模型鲁棒性。后端支持 torchaudio wav2vec2 pipeline 与 Hugging Face CTC 模型，Imperceptible 鲁棒模式需 pyroomacoustics 房间模拟。要求 Python 3.10+ 与 PyTorch 2.x，CUDA/CPU 可选；附基准脚本与 LibriSpeech 上的评测结果。README 含仅限授权评估的使用声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 种攻击（FGSM/BIM/PGD/CW/Imperceptible），均支持定向与非定向
- 支持 torchaudio wav2vec2 与 Hugging Face CTC 两种后端
- Imperceptible 攻击带 RoomSimulator 鲁棒模式
- 跨平台测试（Linux/macOS/Windows）并报告分支覆盖率

## 适用场景

- 评估自家 ASR 模型对对抗样本的鲁棒性
- 复现文献中的音频对抗攻击做研究对比
- 生成对抗性音频用于防御方法训练与评测

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L12: This package tests an ASR (speech-to-text) model against well-known white-box adversarial attacks.
> L40: ## Supported attacks

## 星数曲线

```mermaid
xychart-beta
    title "hammaad2002/ASRAdversarialAttacks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ceeabe2c176c` · [字段定义](../../DATASET.md)*
