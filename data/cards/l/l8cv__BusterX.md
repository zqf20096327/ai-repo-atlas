# l8cv/BusterX

⭐ 51 · Python · BSD-3-Clause · 推送 2026-06-16 · [GitHub](https://github.com/l8cv/BusterX) · 组织维护

**面向科研者的 MLLM 跨模态 AIGC 内容检测与解释方法族**

BusterX / BusterX++ 是基于多模态大模型（MLLM）的 AI 生成内容检测与解释方法族：BusterX 针对视频伪造检测与解释，BusterX++ 扩展为图像+视频的统一跨模态检测。随项目发布 2026/06 修订版，基座更新为 Qwen3.5，并在 Hugging Face 上配套发布训练数据集（GenBuster-200K/Unified）与评测基准（GenBuster-Bench/Bench++）。环境用 uv 管理，默认 CUDA 12.x；提供 DAPO/GSPO 训练脚本与基准评测脚本，默认超参面向 8×H100 80GB。训练基于 ms-swift 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BusterX++：图像+视频统一跨模态 AIGC 检测与解释
- 配套发布 GenBuster-200K 训练数据集与 GenBuster-Bench/Bench++ 评测基准
- 提供 DAPO 与 GSPO 两种训练脚本及 rollout server 模式
- 2026/06 修订版基座模型更新为 Qwen3.5

## 适用场景

- 在自建或公开基准上评测 AIGC 检测模型
- 复现或扩展 MLLM 视频伪造检测研究
- 构建图像+视频跨模态检测自定义基准

## 场景标签

`模型评测` `科研工具` `多模态` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L14: BusterX is a family of MLLM-based methods for detecting and explaining AI-generated content. The project includes:
> L16: - **BusterX++**: Towards Unified Cross-Modal AI-Generated Content Detection and Explanation with MLLM
> L17: - **BusterX**: MLLM-Powered AI-Generated Video Forgery Detection and Explanation

## 星数曲线

```mermaid
xychart-beta
    title "l8cv/BusterX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `946ed0358953` · [字段定义](../../DATASET.md)*
