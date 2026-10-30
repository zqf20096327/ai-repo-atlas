# W-Shuoyan/OSDEnhancer

⭐ 17 · Python · Apache-2.0 · 推送 2026-06-25 · [GitHub](https://github.com/W-Shuoyan/OSDEnhancer) · 组织维护

**单步扩散实现真实世界时空视频超分辨率的研究代码**

论文《Taming Real-World Space-Time Video Super-Resolution with One-Step Diffusion》的参考实现：输入低分辨率低帧率视频，生成高分辨率高帧率视频。机制包括线性初始化、时间一致性与纹理增强两个 LoRA、带可变形循环块的双向 VAE 解码器；基于 CogVideoX1.5-5B，推理脚本自动从 Hugging Face 加载检查点。以 conda + pip 源码方式安装，推荐使用不少于 80GB 显存的 GPU，支持分块推理处理长视频。作者来自北京交通大学等高校。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单步扩散完成时空视频超分辨率（空间×4 / 时间×2）
- TC 与 TE 两个 LoRA 分治建模帧间动态与纹理恢复
- 基于 CogVideoX1.5-5B，检查点托管于 Hugging Face
- 分块推理（--chunk_length 需满足 8N+1）处理长视频

## 适用场景

- 把低分辨率低帧率真实视频提升为高清高帧率视频
- 复现论文结果或在此方法上做研究改进
- 对比一步扩散与多步扩散在视频超分上的效果

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L17: **In this paper, we propose OSDEnhancer, the first framework that achieves real-world STVSR in one-step diffusion.*
> L19: OSDEnhancer begins with a linear initialization to establish essential spatiotemporal structures and adapt the mode

## 星数曲线

```mermaid
xychart-beta
    title "W-Shuoyan/OSDEnhancer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `c4458c4a7878` · [字段定义](../../DATASET.md)*
